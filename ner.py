import spacy

nlp = spacy.load('en_core_web_sm')

text = input("Enter a sentence: ")

doc = nlp(text)

for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")