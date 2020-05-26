from flask import Flask
from flask_cors import CORS
import angles_derivator

app = Flask(__name__)
CORS(app)

@app.route('/')
def calculate():
    return {
        "angles": angles_derivator.calculate()
    }