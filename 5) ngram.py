#5 Implement N-Gram Model 


import nltk
from nltk.util import ngrams
import pandas as pd

# Download punkt (tokenizer) - only needed once
nltk.download('punkt')

# Function to create N-Grams
def generate_ngrams(text, n):
    tokens = nltk.word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return n_grams

# ========== PART 1: DEMO with SAMPLE TEXT ==========

print("\n=== DEMO with SAMPLE TEXT ===\n")

# Sample text
sample_text = "Natural Language Processing is fascinating."

# Choose N
sample_n = 2   # Bigram for demo

# Generate N-Grams for sample
sample_ngrams = generate_ngrams(sample_text, sample_n)

# Display in table
sample_df = pd.DataFrame(sample_ngrams, columns=[f"Word {i+1}" for i in range(sample_n)])
print(f"Sample Text: \"{sample_text}\"")
print(f"\n{sample_n}-Grams (Bigram) List:")
print(sample_df)

# ========== PART 2: USER INPUT ==========

print("\n\n=== NOW YOUR TURN: Provide YOUR OWN TEXT ===\n")

# User input
user_text = input("Enter your text: ")#YOUTUBE HELP ME TO LEARN AI FOR EFFICENTLY!
user_n = int(input("Enter N (for N-Gram, e.g., 2 for bigram, 3 for trigram, etc.): "))#3

# Generate N-Grams for user input
user_ngrams = generate_ngrams(user_text, user_n)

# Display in table
user_df = pd.DataFrame(user_ngrams, columns=[f"Word {i+1}" for i in range(user_n)])
print(f"\nYour Text: \"{user_text}\"")
print(f"\n{user_n}-Grams List:")
print(user_df)
