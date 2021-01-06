"""Flask app"""

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    message = '<h1>Home page</h1>'
    return message

@app.route('/status', methods=['GET'])
def status():
    message = jsonify({'status' : 'Alive!'}), 400
    return message

@app.route('/login', methods=['POST'])
def login():
    request.json['username']
    message = f'Login success for user {username} with password of length: !'
    return message

@app.route('/predict', methods=['GET'])
def predict():
    message = '<h1>predict</h1>'
    return message

if __name__ == '__main__':
    app.run(debug=True)