from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/api/message', methods=['POST'])
def message():
    data = request.get_json()
    user_input = data.get('input')
    # Process the user input and generate a response
    response = f"Received: {user_input}"
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)
