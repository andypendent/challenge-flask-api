"""Flask html app"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)