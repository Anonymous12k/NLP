import random
text = "I love programming in Python because it is fun and versatile."
words = text.split()
pos_tags = ['NOUN', 'VERB', 'ADJ', 'ADV', 'PRON', 'DET', 'ADP', 'CONJ', 'PRT', 'NUM', 'X', '.']
transition_probs = {
    'NOUN': {'NOUN': 0.1, 'VERB': 0.2, 'ADJ': 0.1, 'ADV': 0.1, 'PRON': 0.1, 'DET': 0.1, 'ADP': 0.1, 'CONJ': 0.05, 'PRT': 0.05, 'NUM': 0.05, 'X': 0.05, '.': 0.05},
    'VERB': {'NOUN': 0.1, 'VERB': 0.2, 'ADJ': 0.1, 'ADV': 0.1, 'PRON': 0.1, 'DET': 0.1, 'ADP': 0.1, 'CONJ': 0.05, 'PRT': 0.05, 'NUM': 0.05, 'X': 0.05, '.': 0.05},
    'ADJ': {'NOUN': 0.1, 'VERB': 0.1, 'ADJ': 0.2, 'ADV': 0.1, 'PRON': 0.1, 'DET': 0.1, 'ADP': 0.1, 'CONJ': 0.05, 'PRT': 0.05, 'NUM': 0.05, 'X': 0.05, '.': 0.05},
    'ADV': {'NOUN': 0.1, 'VERB': 0.1, 'ADJ': 0.1, 'ADV': 0.2, 'PRON': 0.1, 'DET': 0.1, 'ADP': 0.1, 'CONJ': 0.05, 'PRT': 0.05, 'NUM': 0.05, 'X': 0.05, '.': 0.05},
    'PRON': {'NOUN': 0.1, 'VERB': 0.1, 'ADJ': 0.1, 'ADV': 0.1, 'PRON': 0.2, 'DET': 0.1, 'ADP': 0.1, 'CONJ': 0.05, 'PRT': 0.05, 'NUM': 0.05, 'X': 0.05, '.': 0.05},
    'DET': {'NOUN': 0.1, 'VERB': 0.1, 'ADJ': 0.1, 'ADV': 0.1, 'PRON': 0.1, 'DET': 0.2, 'ADP': 0.1, 'CONJ': 0.05, 'PRT': 0.05, 'NUM': 0.05, 'X': 0.05, '.': 0.05},
    'ADP': {'NOUN': 0.1, 'VERB': 0.1, 'ADJ': 0.1, 'ADV': 0.1, 'PRON': 0.1, 'DET': 0.1, 'ADP': 0.2, 'CONJ': 0.05, 'PRT': 0.05, 'NUM': 0.05, 'X': 0.05, '.': 0.05},
    'CONJ': {'NOUN': 0.1, 'VERB': 0.1, 'ADJ': 0.1, 'ADV': 0.1, 'PRON': 0.1, 'DET': 0.1, 'ADP': 0.1, 'CONJ': 0.2, 'PRT': 0.05, 'NUM': 0.05, 'X': 0.05, '.': 0.05},
    'PRT': {'NOUN': 0.1, 'VERB': 0.1, 'ADJ': 0.1, 'ADV': 0.1, 'PRON': 0.1, 'DET': 0.1, 'ADP': 0.1, 'CONJ': 0.05, 'PRT': 0.2, 'NUM': 0.05, 'X': 0.05, '.': 0.05},
    'NUM': {'NOUN': 0.1, 'VERB': 0.1, 'ADJ': 0.1, 'ADV': 0.1, 'PRON': 0.1, 'DET': 0.1, 'ADP': 0.1, 'CONJ': 0.05, 'PRT': 0.05, 'NUM': 0.2, 'X': 0.05, '.': 0.05},
    'X': {'NOUN': 0.1, 'VERB': 0.1, 'ADJ': 0.1, 'ADV': 0.1, 'PRON': 0.1, 'DET': 0.1, 'ADP': 0.1, 'CONJ': 0.05, 'PRT': 0.05, 'NUM': 0.05, 'X': 0.2, '.': 0.05},
    '.': {'NOUN': 0.1, 'VERB': 0.1, 'ADJ': 0.1, 'ADV': 0.1, 'PRON': 0.1, 'DET': 0.1, 'ADP': 0.1, 'CONJ': 0.05, 'PRT': 0.05, 'NUM': 0.05, 'X': 0.05, '.': 0.2}
}
def pos_tag(text):
    tagged_words = []
    prev_pos = None
    for word in text:
        if prev_pos is None:
            pos = random.choice(pos_tags)
        else:
            pos = random.choices(pos_tags, weights=list(transition_probs[prev_pos].values()))[0]
        tagged_words.append((word, pos))
        prev_pos = pos
    return tagged_words
tagged_text = pos_tag(words)
for word, pos in tagged_text:
    print(f"{word}/{pos}", end=" ")
print()
