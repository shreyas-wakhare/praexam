#2 MORPHOLOGY

import pandas as pd

# Function to get user input as a list
def get_list_input(prompt_text):
    items = input(prompt_text)
    return [item.strip() for item in items.split(',') if item.strip()]

# Function to delete suffix from a word
def delete_suffix(word, suffixes):
    # Sort suffixes by length (longest first) to avoid wrong cuts
    for suffix in sorted(suffixes, key=len, reverse=True):
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

# ========== PART 1: DEMO with SAMPLE DATA ==========

print("\n=== DEMO with SAMPLE DATA ===\n")

# Sample fixed root words
root_words_sample = ["play", "jump", "talk"]

# Sample fixed suffixes
suffixes_sample = ["ing", "ed", "s"]

# ADD TABLE (Sample)
add_table_sample = []
for root in root_words_sample:
    new_words = {suffix: root + suffix for suffix in suffixes_sample}
    add_table_sample.append({"Root": root, **new_words})

add_table_sample_df = pd.DataFrame(add_table_sample)

# Sample words with suffixes
words_with_suffixes_sample = ["playing", "jumped", "talks", "plays", "talked", "jumping"]

# DELETE TABLE (Sample)
delete_table_sample = []
for word in words_with_suffixes_sample:
    root = delete_suffix(word, suffixes_sample)
    delete_table_sample.append({"Word with Suffix": word, "Root after Deletion": root})

delete_table_sample_df = pd.DataFrame(delete_table_sample)

# Show sample outputs
print("=== SAMPLE ADD TABLE ===")
print(add_table_sample_df)

print("\n=== SAMPLE DELETE TABLE ===")
print(delete_table_sample_df)

# ========== PART 2: USER INPUT ==========

print("\n\n=== NOW YOUR TURN: Provide YOUR OWN INPUT ===\n")

# Step 1: User input root words
root_words_user = get_list_input("Enter root words separated by commas (e.g., play,jump,talk): ")

# Step 2: User input suffixes
suffixes_user = get_list_input("Enter suffixes to add separated by commas (e.g., ing,ed,s): ")

# ADD TABLE (User Input)
add_table_user = []
for root in root_words_user:
    new_words = {suffix: root + suffix for suffix in suffixes_user}
    add_table_user.append({"Root": root, **new_words})

add_table_user_df = pd.DataFrame(add_table_user)

# Step 3: User input words with suffixes
words_with_suffixes_user = get_list_input("Enter words with suffixes separated by commas (e.g., playing,jumped,talks): ")

# DELETE TABLE (User Input)
delete_table_user = []
for word in words_with_suffixes_user:
    root = delete_suffix(word, suffixes_user)
    delete_table_user.append({"Word with Suffix": word, "Root after Deletion": root})

delete_table_user_df = pd.DataFrame(delete_table_user)

# Show user outputs
print("\n=== YOUR ADD TABLE ===")
print(add_table_user_df)

print("\n=== YOUR DELETE TABLE ===")
print(delete_table_user_df)

