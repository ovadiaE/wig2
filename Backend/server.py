from flask import Flask
from ta_patterns import get_pattern_names
from retracement_values import get_retracement_values

app = Flask(__name__)

@app.route("/", methods=['GET'])
def gold_info():
    pattern_names = get_pattern_names()
    retracement_values = get_retracement_values()
    return {'pattern names': pattern_names, 'retracement values': retracement_values}