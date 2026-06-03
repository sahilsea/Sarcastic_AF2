import joblib
import pandas as pd
import sys
import os

# Ensure the model and vectorizer exist
if not os.path.exists('sarcasm_model.pkl') or not os.path.exists('vectorizer.pkl'):
    print("Error: Model or vectorizer not found. Please run train_model.py first.")
    sys.exit(1)

# Load the vectorizer and model
vectorizer = joblib.load('vectorizer.pkl')
model = joblib.load('sarcasm_model.pkl')

def predict_sarcasm(text):
    # Vectorize the input text
    text_vec = vectorizer.transform([text])
    
    # Predict the class
    prediction = model.predict(text_vec)[0]
    
    # Get prediction probabilities
    probabilities = model.predict_proba(text_vec)[0]
    confidence = max(probabilities) * 100
    
    # Output formatting
    result = "Funny / Sarcastic" if prediction == 1 else "Not Funny / Not Sarcastic"
    return result, confidence

def main():
    print("--- Sarcasm & Funniness Predictor ---")
    print("Type your text below (or type 'quit' to exit):")
    
    while True:
        try:
            user_input = input("\n> ")
            if user_input.lower() in ['quit', 'exit']:
                print("Exiting. Have a great day!")
                break
            
            if not user_input.strip():
                continue
                
            result, confidence = predict_sarcasm(user_input)
            print(f"Prediction: {result} (Confidence: {confidence:.2f}%)")
            
        except KeyboardInterrupt:
            print("\nExiting. Have a great day!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
