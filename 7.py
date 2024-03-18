import nltk
nltk.download('averaged_perceptron_tagger')
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Sample text
text = "I love programming in Python because it is fun and versatile."

# Tokenize the text into words
words = word_tokenize(text)

# Perform part-of-speech tagging
pos_tags = pos_tag(words)

# Print the part-of-speech tags
print(pos_tags)
