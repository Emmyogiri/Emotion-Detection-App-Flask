"""
This module defines the Flask server for the Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector", template_folder = 'templates')

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET", "POST"])
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    text_to_detect = request.args.get('textToAnalyze')
    if not text_to_detect:
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_detect)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is \
    'anger': {anger},'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}.\
    The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
