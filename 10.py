def transform_tag(sentence, rules):
    tagged_words = []
    for word in sentence.split():
        tagged_words.append((word, 'UNK'))  # Initialize all words as unknown POS
    for rule in rules:
        for i in range(len(tagged_words)):
            word, pos = tagged_words[i]
            if rule[0](word):
                tagged_words[i] = (word, rule[1])  # Apply transformation rule
    return tagged_words

# Define transformation rules
rules = [
    (lambda word: word.endswith('ing'), 'VERB'),  # Words ending with 'ing' are verbs
    (lambda word: word.isdigit(), 'NUM'),         # Words consisting of digits are numbers
    (lambda word: word.isupper(), 'NOUN')         # Words in all uppercase are nouns
]

# Example sentence
sentence = "He is learning Python and it is fun."

tagged_text = transform_tag(sentence, rules)

for word, pos in tagged_text:
    print(f"{word}/{pos}", end=" ")
print()
