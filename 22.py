import nltk
nltk.download('stopwords')
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Sample text
text = "John went to the store. He bought some milk. The milk was delicious."

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Tokenize each sentence into words
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_sentences = [[word for word in sentence if word not in stop_words] for sentence in tokenized_sentences]

# Build a dictionary to store referents
referents = {}

# Iterate through each sentence to resolve references
for i, sentence in enumerate(filtered_sentences):
    for j, word in enumerate(sentence):
        if word == 'he' or word == 'she' or word == 'it' or word == 'they':
            if j > 0:
                # Check for possessive pronoun
                if sentence[j - 1] == "'s":
                    referents[(i, j)] = sentence[j - 2]
                else:
                    referents[(i, j)] = sentence[j - 1]
            else:
                if i > 0:
                    referents[(i, j)] = filtered_sentences[i - 1][-1]

# Replace pronouns with referents
resolved_text = text
for (i, j), referent in referents.items():
    resolved_text = resolved_text.replace(filtered_sentences[i][j], referent)

print("Original text:")
print(text)
print("\nReference resolved text:")
print(resolved_text)
