import re

# Sample text
text = "The quick brown fox jumps over the lazy dog."

# Define a regular expression pattern
pattern = r"\b\w{4}\b"  # Match 4-letter words

# Use re.findall() to find all occurrences of the pattern in the text
matches = re.findall(pattern, text)

# Print the matched words
print("Matched words:", matches)

# Use re.search() to search for the pattern in the text
search_result = re.search(pattern, text)

# Print the first match found
if search_result:
    print("First match found:", search_result.group())
else:
    print("No match found.")
