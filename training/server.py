from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        data = request.get_json()
        search_term = data.get('searchTerm')
        print(f"Received message: {search_term}")
        return {'message': 'Data received successfully'}, 200
    else:
        return 'Invalid request', 400

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)