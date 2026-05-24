import pandas as pd
import emoji
import nltk
from nltk.corpus import stopwords
import re

# Download stopwords list if not already present
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

def clean_text(text):
    if not isinstance(text, str):
        return text
    
    # 1. Remove all emojis
    text = emoji.replace_emoji(text, replace='')
    
    # 2. Remove stop words
    words = text.split()
    cleaned_words = []
    for word in words:
        # Check stripping basic punctuation to see if it's a stop word
        clean_word = re.sub(r'^\W+|\W+$', '', word).lower()
        if clean_word not in stop_words:
            cleaned_words.append(word)
            
    return ' '.join(cleaned_words)

# Read the original CSV
input_file = 'sarcasm_training_data_1000.csv'
df = pd.read_csv(input_file)

# Apply the cleaning function to the comment_text column
df['comment_text'] = df['comment_text'].apply(clean_text)

# Overwrite the cleaned CSV
output_file = 'sarcasm_training_data_1000_cleaned.csv'
df.to_csv(output_file, index=False)
print(f"Data cleaned successfully and saved to {output_file}")
