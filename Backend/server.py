from flask import Flask
from flask_cors import CORS
# from ta_patterns import get_pattern_names
from retracement_values import get_retracement_values
from datetime import date

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def gold_info():
    # pattern_names = get_pattern_names()
    return get_retracement_values()
  