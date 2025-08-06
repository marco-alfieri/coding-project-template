"""
Author:  Marco Alfieri date: 06/07/2025 - 15:50
Flask web server for detecting emotions in user-provided text.

This module exposes an endpoint '/emotionDetector' which accepts text input
and returns the intensity of five emotions along with the dominant one.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET", "POST"])
def emo_detector():
    """
    Web API endpoint for detecting emotions in a given text input.

    Accepts a text string via GET request (query parameter 'textToAnalyze'),
    sends it to the emotion detection model, and returns a formatted string
    displaying the intensity of five emotions and the dominant one.

    Returns:
        str: Formatted result of detected emotions or an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement '{text_to_analyze}', the system detected: "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the index.html homepage.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

