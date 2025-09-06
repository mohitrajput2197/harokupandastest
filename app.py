from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # This will prove that pandas was installed correctly
    return f"Hello, Heroku! Pandas version: {pd.__version__}"