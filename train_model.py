import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

def main():
    print("Loading data...")
    # Read the cleaned dataset
    df = pd.read_csv('sarcasm_training_data_1000_cleaned.csv')
    
    # Drop rows with missing values in comment_text
    df = df.dropna(subset=['comment_text'])
    
    X = df['comment_text']
    y = df['is_sarcastic']
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Vectorizing text...")
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    print("Training Logistic Regression model...")
    # Initialize and train the Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train_vec, y_train)
    
    print("Evaluating model...")
    # Predict on the test set
    y_pred = model.predict(X_test_vec)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the vectorizer and model for later use
    joblib.dump(vectorizer, 'vectorizer.pkl')
    joblib.dump(model, 'sarcasm_model.pkl')
    print("Model and vectorizer saved to 'sarcasm_model.pkl' and 'vectorizer.pkl'")

if __name__ == "__main__":
    main()
