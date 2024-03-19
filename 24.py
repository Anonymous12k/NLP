import nltk
nltk.download('nps_chat')
import nltk
from nltk.corpus import nps_chat

# Load the nps_chat corpus
chat_posts = nps_chat.xml_posts()

# Define a function to extract dialog acts from a given post
def extract_dialog_act(post):
    return post.get('class')

# Extract dialog acts from the nps_chat corpus
dialog_acts = [extract_dialog_act(post) for post in chat_posts]

# Print the dialog acts for the first few posts
for i, dialog_act in enumerate(dialog_acts[:10]):
    print(f"Post {i+1}: {dialog_act}")
