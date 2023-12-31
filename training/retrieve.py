import gensim.downloader
from gensim.models import KeyedVectors
import numpy as np
import json

#Load pre-trained word vectors
glove_vectors = gensim.downloader.load('glove-wiki-gigaword-100')

# Sample query and results
# query = "How to draw a line"
with open('./temp/matplotlib.json', 'r') as f:
    result_dict = json.load(f)
# result_dict = {
#     'plot a pie chart': 'matplotlib.pyplot.pie',
#     'plot a bar chart': 'matplotlib.pyplot.bar',
#     'plot a line chart': 'matplotlib.pyplot.plot',
#     # 'add an axes to the current figure or retrieve an existing axes': 'matplotlib.pyplot.axes',
#     # 'add a subplot to the current figure.': 'matplotlib.pyplot.subplot',
#     'clear the current axes': 'matplotlib.pyplot.cla',
# }
# Tokenize and obtain word embeddings for each sentence
def get_sentence_embedding(sentence):
    words = sentence.lower().split()  # Tokenization might need further adjustments
    vectors = [glove_vectors[word] for word in words if word in glove_vectors]
    return np.mean(vectors, axis=0) if vectors else np.zeros(glove_vectors.vector_size)

def convert_to_declarative(question):
    question_words = ['who', 'what', 'when', 'where', 'why', 'how', 'is', 'are', 'am', 'was', 'were', 'do', 'does', 'did', 'can', 'could', 'will', 'would', 'shall', 'should']
    
    question = question.rstrip('?')
    words = question.split()
    words = [word for word in words if word.lower() not in question_words]

    declarative = ' '.join(words)
    return declarative

result_embeddings = [get_sentence_embedding(result) for result in result_dict.keys()]

while True:
    # Calculate cosine similarity between query and each result
    query = input('Please enter a question: ')
    if not query: break
    query_declared = convert_to_declarative(query)
    query_embedding = get_sentence_embedding(query_declared)
    similarity_scores = [np.dot(query_embedding, result_emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(result_emb)) for result_emb in result_embeddings]

    # Rank results based on similarity scores
    ranked_results = sorted(zip(result_dict.keys(), similarity_scores), key=lambda x: x[1], reverse=True)

    # Print ranked results
    print(f'Query: {query}\nReturn results:\n')
    display_num = min(5, len(ranked_results))
    for idx, (result, score) in enumerate(ranked_results[:display_num]):
        print(f"#{idx}: {result_dict[result]} ({result}, {score})")
    print('*' * 50 + '\n')
