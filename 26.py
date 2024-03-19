from transformers import pipeline

# Load the translation pipeline
translator = pipeline("translation_en_to_fr")

# English text to translate
english_text = "Hello, how are you?"

# Translate English text to French
french_translation = translator(english_text)

# Print the translated text
print(french_translation[0]['translation_text'])
