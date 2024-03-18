import random

# Sample text
text = "I love programming in Python because it is fun and versatile."

# Tokenize the text into words
words = text.split()

# Create a dictionary to store bigrams
bigrams = {}
for i in range(len(words) - 1):
    bigram = (words[i], words[i + 1])
    if bigram not in bigrams:
        bigrams[bigram] = []
    if i + 2 < len(words):
        bigrams[bigram].append(words[i + 2])

# Generate text using the bigram model
def generate_text(start_word, num_words):
    current_word = start_word
    text = [current_word]
    for _ in range(num_words - 1):
        next_word_candidates = bigrams.get((current_word,), [])
        if not next_word_candidates:
            break
        next_word = random.choice(next_word_candidates)
        text.append(next_word)
        current_word = next_word
    return " ".join(text)

# Generate text using the bigram model starting with a given word
start_word = "I love programming in Python because it is fun and versatile."
num_words = 10
generated_text = generate_text(start_word, num_words)
print(generated_text)
