from flask import Flask, request, jsonify
import gensim.downloader
from gensim.models import KeyedVectors
import numpy as np

app = Flask(__name__)

# Load pre-trained word vectors
glove_vectors = gensim.downloader.load('glove-wiki-gigaword-100')

# Sample results
result_dict = {
    'plot a pie chart': 'matplotlib.pyplot.pie',
    'plot a bar chart': 'matplotlib.pyplot.bar',
    'plot a line chart': 'matplotlib.pyplot.plot',
    'clear the current axes': 'matplotlib.pyplot.cla'
}

# Tokenize and obtain word embeddings for each sentence
def get_sentence_embedding(sentence):
    words = sentence.lower().split()
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

@app.route('/query', methods=['POST'])
def process_query():
    data = request.get_json()
    if data and 'query' in data:
        query = data['query']
        query_declared = convert_to_declarative(query)
        query_embedding = get_sentence_embedding(query_declared)
        similarity_scores = [np.dot(query_embedding, result_emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(result_emb)) for result_emb in result_embeddings]

        # Rank results based on similarity scores
        ranked_results = sorted(zip(result_dict.keys(), similarity_scores), key=lambda x: x[1], reverse=True)

        # Prepare response
        ranked_results = [{'function': result_dict[result], 'score': score} for result, score in ranked_results]

        return jsonify({'results': ranked_results})

    return jsonify({'error': 'Invalid input'})

if __name__ == '__main__':
    app.run(port=8080)  # Run Flask app on port 8080
