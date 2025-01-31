""" API for emotion detection engine """

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detect():
    """Endpoint for emotion detection, pass 'textToAnalyze' as argument"""

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    # Error handling for invalid input
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. the dominant emotion is : {response['dominant_emotion']}."


@app.route("/")
def render_index_page():
    """Landing page, default index"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
