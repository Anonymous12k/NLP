from nltk.corpus import wordnet
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

# Sample sentence
sentence = "I went to the bank to deposit my money."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Perform word sense disambiguation for each token
for token in tokens:
    synset = lesk(tokens, token)
    if synset:
        print(f"Token: {token}, Synset: {synset}, Definition: {synset.definition()}")
    else:
        print(f"No synset found for token: {token}")

