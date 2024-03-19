import openai

# Set your API key
api_key = "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"
openai.api_key = api_key

# Define a prompt
prompt = "Once upon a time"

# Generate text based on the prompt
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100
)

# Print the generated text
print(response['choices'][0]['text'].strip())
