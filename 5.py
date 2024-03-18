import nltk
from nltk.stem import PorterStemmer

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# List of words to perform stemming on
words = ["running", "flies", "calves", "better"]

# Perform stemming on each word
stemmed_words = [stemmer.stem(word) for word in words]

# Print the original words and their stemmed forms
for original, stemmed in zip(words, stemmed_words):
    print(f"Original: {original} | Stemmed: {stemmed}")
