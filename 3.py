import nltk
from nltk.stem import PorterStemmer

# Download the NLTK data (if not already downloaded)
nltk.download('punkt')

# Initialize the PorterStemmer
stemmer = PorterStemmer()

# Example words to perform morphological analysis
words = ["running", "flies", "calves", "better"]

# Perform stemming on each word
for word in words:
    stemmed_word = stemmer.stem(word)
    print(f"Original: {word} | Stemmed: {stemmed_word}")
