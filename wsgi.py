from flask import Flask, jsonify
import random
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 6)
    return jsonify({'roll': random_number, "date": datetime.datetime.now()})
