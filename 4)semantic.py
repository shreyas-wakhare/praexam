#4) SEMANTIC RELATIONSHIP

import nltk
from nltk.corpus import wordnet as wn
import pandas as pd

# Download WordNet data (only needed once)
nltk.download('wordnet')
nltk.download('omw-1.4')

# Function to find semantic relations
def find_semantic_relations(word):
    synsets = wn.synsets(word)
    relations = []
    for syn in synsets:
        for lemma in syn.lemmas():
            relations.append(("Synonym", lemma.name()))
        for hypernym in syn.hypernyms():
            relations.append(("Hypernym (more general)", hypernym.name().split('.')[0]))
        for hyponym in syn.hyponyms():
            relations.append(("Hyponym (more specific)", hyponym.name().split('.')[0]))
    return relations

# ========== PART 1: DEMO with SAMPLE WORD ==========

print("\n=== DEMO with SAMPLE WORD ===\n")

# Sample word
sample_word = "dog"

# Find relations for sample word
sample_relations = find_semantic_relations(sample_word)

# Display in table
sample_df = pd.DataFrame(sample_relations, columns=["Relation Type", "Related Word"])
print("Sample Word: ", sample_word)
print("\nSemantic Relations:")
print(sample_df)

# ========== PART 2: USER INPUT ==========

print("\n\n=== NOW YOUR TURN: Provide YOUR OWN WORD ===\n")

# User input
user_word = input("Enter a word to find its semantic relations: ")#CAR

# Find relations for user word
user_relations = find_semantic_relations(user_word)

# Display in table
user_df = pd.DataFrame(user_relations, columns=["Relation Type", "Related Word"])
print("\nYour Word: ", user_word)
print("\nSemantic Relations:")
print(user_df)
