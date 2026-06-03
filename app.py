import json
import os
import sqlite3
import urllib.error
import urllib.request
from datetime import datetime

from dotenv import load_dotenv
from flask import (
    Flask,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()


app = Flask(__name__)
app.secret_key = os.urandom(24)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Global Ritual Settings
ritual_settings = {
    "temperature": 0.7,
    "thinking_tokens": "medium",
    "system_instruction": "You are a 400-year-old linguist who finds modern digital communication amusingly primitive. Your tone is academic, deeply ironic, and peppered with archaic vocabulary. You do not explain your jokes; if the user doesn't get it, that's part of the ritual.",
}

DATABASE = "arcane_engine.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.before_request
def require_login():
    allowed_routes = ["login", "static"]
    if request.endpoint not in allowed_routes and "username" not in session:
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "Unknown Wizard").strip()
        password = request.form.get("password", "")
        if not username:
            username = "Anonymous Scholar"

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user:
            if check_password_hash(user["password_hash"], password):
                session["username"] = username
                session["user_id"] = user["id"]
                return redirect(url_for("home"))
            else:
                return render_template("login.html", error="Incorrect incantation.")
        else:
            hashed_pw = generate_password_hash(password)
            cursor.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, hashed_pw),
            )
            db.commit()
            session["username"] = username
            session["user_id"] = cursor.lastrowid
            return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/grimoire")
def grimoire():
    return render_template("grimoire.html")


@app.route("/library")
def library():
    return render_template("library.html")


@app.route("/rituals")
def rituals():
    return render_template("rituals.html")


@app.route("/magical_surge")
def magical_surge():
    return render_template("magical_surge.html")


@app.route("/history", methods=["GET"])
def get_history():
    db = get_db()
    scope = request.args.get("scope", "personal")

    if scope == "all":
        cursor = db.execute(
            "SELECT h.*, u.username FROM history h JOIN users u ON h.user_id = u.id ORDER BY h.id DESC"
        )
    else:
        cursor = db.execute(
            "SELECT * FROM history WHERE user_id = ? ORDER BY id DESC",
            (session.get("user_id", 0),),
        )

    rows = cursor.fetchall()

    history_list = []
    for row in rows:
        history_list.append(
            {
                "text": row["text"],
                "timestamp": row["timestamp"],
                "verdict": row["verdict"],
                "sarcasm_score": row["sarcasm_score"],
                "irony_score": row["irony_score"],
                "analysis": row["analysis"],
                "username": row["username"]
                if scope == "all"
                else session.get("username"),
            }
        )

    if scope == "personal":
        mastery = len(history_list)
        if mastery < 5:
            rank = "Novice Diviner"
        elif mastery < 20:
            rank = "Adept Seer"
        else:
            rank = "Senior Inquisitor"

        sarcasm_sum = sum(h["sarcasm_score"] for h in history_list)
        success_rate = int((sarcasm_sum / mastery) if mastery > 0 else 0)

        stats = {
            "mastery": mastery,
            "rank": rank,
            "success_rate": success_rate,
            "daily_streak": 1,
        }
    else:
        stats = None

    return jsonify({"history": history_list, "stats": stats})


@app.route("/settings", methods=["GET"])
def get_settings():
    return jsonify(ritual_settings)


@app.route("/settings", methods=["POST"])
def update_settings():
    data = request.json
    if "temperature" in data:
        ritual_settings["temperature"] = float(data["temperature"])
    if "thinking_tokens" in data:
        ritual_settings["thinking_tokens"] = data["thinking_tokens"]
    if "system_instruction" in data:
        ritual_settings["system_instruction"] = data["system_instruction"]
    return jsonify({"status": "success", "settings": ritual_settings})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"error": "Text is required."}), 400

    prompt = f"""{ritual_settings["system_instruction"]}

Analyze the following text for sarcasm:

TEXT: {text}

Respond ONLY with a valid JSON object, no markdown, no extra text. Use this exact structure:
{{
  "verdict": "SARCASTIC" or "GENUINE",
  "sarcasm_score": <integer 0-100>,
  "confidence_score": <integer 0-100>,
  "irony_score": <integer 0-100>,
  "analysis": "<One sentence (less than 15 words) analysis in a dry, deadpan, slightly sarcastic tone — as if reluctantly pointing out the obvious>",
  "tags": ["<tag1>", "<tag2>", "<tag3>"]
}}"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "response_mime_type": "application/json",
            "temperature": float(ritual_settings["temperature"]),
        },
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            text_response = result["candidates"][0]["content"]["parts"][0]["text"]

            # Remove any markdown JSON wrapping just in case
            clean_json = (
                text_response.strip()
                .removeprefix("```json")
                .removesuffix("```")
                .strip()
            )

            try:
                parsed = json.loads(clean_json)
                db = get_db()
                db.execute(
                    "INSERT INTO history (user_id, text, timestamp, verdict, sarcasm_score, irony_score, analysis) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (
                        session.get("user_id", 0),
                        text,
                        datetime.now().strftime("%d %b %Y").upper(),
                        parsed.get("verdict", "UNKNOWN"),
                        parsed.get("sarcasm_score", 0),
                        parsed.get("irony_score", 0),
                        parsed.get("analysis", ""),
                    ),
                )
                db.commit()
            except Exception as e:
                print("Could not insert history into DB:", e)

            return clean_json, 200, {"Content-Type": "application/json"}
    except urllib.error.HTTPError as e:
        print(f"HTTPError calling Gemini API: {e.code} {e.reason}")
        print(e.read().decode("utf-8"))
        return jsonify({"error": "Failed to analyze text via Gemini API."}), 500
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
