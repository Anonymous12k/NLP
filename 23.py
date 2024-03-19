from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def text_coherence(text):
    # Tokenize the text into sentences
    sentences = text.split('.')

    # Remove empty strings
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    if len(sentences) < 2:
        return 0.0  # Not enough sentences for comparison

    # Create a CountVectorizer to convert sentences to vectors
    vectorizer = CountVectorizer().fit_transform(sentences)

    # Calculate cosine similarity between consecutive sentences
    similarity_matrix = cosine_similarity(vectorizer[:-1], vectorizer[1:])

    # Average the cosine similarity scores
    coherence_score = similarity_matrix.mean()

    return coherence_score

# Example text
text = """
Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans using natural language. NLP techniques are used to analyze, understand, and generate human language, enabling computers to understand human speech and text.

NLP has many applications, including machine translation, speech recognition, sentiment analysis, and text summarization. These applications rely on NLP algorithms to process and understand human language, making NLP an essential component of many AI systems.

While NLP has made significant advancements in recent years, challenges remain in areas such as understanding context, dealing with ambiguity, and handling languages with complex grammar and syntax. Researchers continue to work on improving NLP techniques to overcome these challenges and make AI systems more effective in understanding and interacting with human language.
"""

coherence_score = text_coherence(text)
print("Coherence Score:", coherence_score)
