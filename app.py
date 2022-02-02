"""Main script, uses other modules to generate sentences."""
from flask import Flask
from histogram import create_histogram_dict
from sample import weighted_word


app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    histogram = create_histogram_dict('example_txt/example1.txt')
    return histogram


@app.route("/")
def home():
    histogram = before_first_request()
    word = weighted_word(histogram)
    """Route that returns a web page containing the generated text."""
    return word


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True, port=5001)
