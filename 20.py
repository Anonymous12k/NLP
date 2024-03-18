from collections import Counter
import math

# Sample documents
documents = [
    "machine learning is the study of computer algorithms that improve automatically through experience and by the use of data",
    "data science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data",
    "natural language processing is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language",
    "artificial intelligence is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals",
]

# Tokenize the documents
tokenized_documents = [doc.split() for doc in documents]

# Compute document frequencies (DF)
document_frequencies = Counter()
for doc in tokenized_documents:
    document_frequencies.update(set(doc))

# Compute inverse document frequencies (IDF)
num_documents = len(tokenized_documents)
inverse_document_frequencies = {term: math.log(num_documents / (document_frequencies[term] + 1)) for term in document_frequencies}

# Compute TF-IDF vectors for each document
tfidf_vectors = []
for doc in tokenized_documents:
    term_frequencies = Counter(doc)
    tfidf_vector = {term: term_frequencies[term] * inverse_document_frequencies[term] for term in term_frequencies}
    tfidf_vectors.append(tfidf_vector)

# Sample query
query = "machine learning algorithms"

# Compute TF-IDF vector for the query
query_terms = query.split()
query_vector = {term: query_terms.count(term) * inverse_document_frequencies[term] for term in query_terms}

# Compute cosine similarity between query and documents
def cosine_similarity(vec1, vec2):
    numerator = sum(vec1.get(term, 0) * vec2.get(term, 0) for term in set(vec1) & set(vec2))
    denominator = math.sqrt(sum(val**2 for val in vec1.values())) * math.sqrt(sum(val**2 for val in vec2.values()))
    return numerator / denominator if denominator != 0 else 0

# Rank documents based on cosine similarity
document_scores = [(idx, cosine_similarity(query_vector, doc_vec)) for idx, doc_vec in enumerate(tfidf_vectors)]
sorted_documents = sorted(document_scores, key=lambda x: x[1], reverse=True)

# Print ranked documents
for idx, score in sorted_documents:
    print(f"Document {idx + 1}: {documents[idx]} (Score: {score})")
