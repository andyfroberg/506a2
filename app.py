#!/usr/bin/python3

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home page'

@app.route('/andrewfroberg')
def name():
    return 'Hello world from Andrew Froberg'

@app.route('/datetime')
def time():
    return f'The current time is: {str(datetime.now())[:16]}.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
