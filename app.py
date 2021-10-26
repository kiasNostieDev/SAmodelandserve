from flask import Flask
app = Flask(__name__)

@app.route('/')
def isItUp():
    return 'Shining as a sunlight'