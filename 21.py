import nltk
from nltk import pos_tag, RegexpParser
from nltk.tokenize import word_tokenize

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog"

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Perform Part-of-Speech (POS) tagging
tagged_tokens = pos_tag(tokens)

# Define a grammar for noun phrases
grammar = r"""
  NP: {<DT>?<JJ>*<NN>} # Chunk sequences of DT, JJ, NN
      {<NNP>+}        # Chunk consecutive proper nouns
"""

# Create a parser using the defined grammar
parser = RegexpParser(grammar)

# Parse the tagged tokens to extract noun phrases
parsed_sentence = parser.parse(tagged_tokens)

# Extract noun phrases and their meanings
noun_phrases = []
for subtree in parsed_sentence.subtrees():
    if subtree.label() == 'NP':
        noun_phrases.append(' '.join([token for token, tag in subtree.leaves()]))

# Display the extracted noun phrases
print("Noun Phrases:", noun_phrases)
