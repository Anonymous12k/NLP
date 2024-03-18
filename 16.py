import spacy
nlp = spacy.load("en_core_web_sm")
text = "Apple is a great company, headquartered in Cupertino, California. " \
       "It was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976."
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
