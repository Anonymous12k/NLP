import re

def pos_tag(text):
    tagged_words = []
    for word in text.split():
        if re.match(r'\b(?:is|am|are|was|were)\b', word, re.IGNORECASE):
            tagged_words.append((word, 'VERB'))
        elif re.match(r'\b(?:the|a|an)\b', word, re.IGNORECASE):
            tagged_words.append((word, 'DET'))
        elif re.match(r'\b(?:\d+|\d*\.\d+)\b', word):
            tagged_words.append((word, 'NUM'))
        elif re.match(r'\b(?:[A-Z]\.)+', word):
            tagged_words.append((word, 'NOUN'))
        else:
            tagged_words.append((word, 'UNK'))  # Unknown POS
    return tagged_words

text = "I am learning Python and it is fun."
tagged_text = pos_tag(text)

for word, pos in tagged_text:
    print(f"{word}/{pos}", end=" ")
print()
