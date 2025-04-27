#3 POS TAGGING

import nltk
import pandas as pd

# Download necessary data (only first time)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Function to perform POS tagging
def pos_tagging(text):
    tokens = nltk.word_tokenize(text)      # Step 1: Tokenize the sentence
    tagged = nltk.pos_tag(tokens)           # Step 2: POS tagging
    return tagged

# ========== PART 1: DEMO with SAMPLE SENTENCE ==========

print("\n=== DEMO with SAMPLE SENTENCE ===\n")

# Sample sentence
sample_text = "The quick brown fox jumps over the lazy dog."

# Perform POS tagging on sample
sample_pos_tags = pos_tagging(sample_text)

# Display results in table
sample_df = pd.DataFrame(sample_pos_tags, columns=["Word", "POS Tag"])
print("Sample Sentence: ", sample_text)
print("\nPOS Tags:")
print(sample_df)

# ========== PART 2: USER INPUT ==========

print("\n\n=== NOW YOUR TURN: Provide YOUR OWN SENTENCE ===\n")

# User input
user_text = input("Enter a sentence for POS tagging: ")#I love learning Natural Language Processing with you tube!

# Perform POS tagging on user input
user_pos_tags = pos_tagging(user_text)

# Display results in table
user_df = pd.DataFrame(user_pos_tags, columns=["Word", "POS Tag"])
print("\nYour Sentence: ", user_text) #I love learning Natural Language Processing with books!
print("\nPOS Tags:")
print(user_df)
