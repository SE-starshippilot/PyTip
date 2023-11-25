import socket
import numpy as np
import gensim.downloader

# def get_sentence_embedding(sentence):
#     words = sentence.lower().split()  # Tokenization might need further adjustments
#     vectors = [glove_vectors[word] for word in words if word in glove_vectors]
#     return np.mean(vectors, axis=0) if vectors else np.zeros(glove_vectors.vector_size)

def convert_to_declarative(question):
    question_words = ['who', 'what', 'when', 'where', 'why', 'how', 'is', 'are', 'am', 'was', 'were', 'do', 'does', 'did', 'can', 'could', 'will', 'would', 'shall', 'should']
    
    question = question.rstrip('?')
    words = question.split()
    words = [word for word in words if word.lower() not in question_words]

    declarative = ' '.join(words)
    return declarative

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established from {client_address}")

        while True:
            query = client_socket.recv(1024).decode("utf-8").strip()
            if query == "":
                print(f'Exit')
                break
            print(f"Received message: {query}")
            # query_declared = convert_to_declarative(query)
            # query_embedding = get_sentence_embedding(query_declared)
            # similarity_scores = [np.dot(query_embedding, result_emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(result_emb)) for result_emb in result_embeddings]

            # # Rank results based on similarity scores
            # ranked_results = sorted(zip(result_dict.keys(), similarity_scores), key=lambda x: x[1], reverse=True)

            # # Print ranked results
            # message = [f'Query: {query}\nReturn results:']
            # for idx, (result, score) in enumerate(ranked_results):
            #     message.append(f"#{idx}: {result_dict[result]} ({result}, {score})")
            # message.append('*' * 50 + '\n')
            # message = '\n'.join(message)
            # client_socket.sendall(message.encode("utf-8"))


        client_socket.close()
        break

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Localhost
    PORT = 8080  # Replace with your desired port number
    #Load pre-trained word vectors
    # glove_vectors = gensim.downloader.load('glove-wiki-gigaword-100')

    # result_dict = {
    #     'plot a pie chart': 'matplotlib.pyplot.pie',
    #     'plot a bar chart': 'matplotlib.pyplot.bar',
    #     'plot a line chart': 'matplotlib.pyplot.plot',
    #     # 'add an axes to the current figure or retrieve an existing axes': 'matplotlib.pyplot.axes',
    #     # 'add a subplot to the current figure.': 'matplotlib.pyplot.subplot',
    #     'clear the current axes': 'matplotlib.pyplot.cla',
    # }
    # # Tokenize and obtain word embeddings for each sentence
    # result_embeddings = [get_sentence_embedding(result) for result in result_dict.keys()]
    start_server(HOST, PORT)
