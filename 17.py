from nltk.corpus import wordnet

# Function to print synsets and their definitions
def print_synsets(word):
    synsets = wordnet.synsets(word)
    if not synsets:
        print(f"No synsets found for '{word}'")
        return

    for synset in synsets:
        print(f"Synset: {synset.name()}")
        print(f"Definition: {synset.definition()}")
        print(f"Examples: {synset.examples()}")
        print()
word = "car"
print_synsets(word)
