'''server app'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

'''route'''

@app.route("/emotionDetector")
def sent_analyzer():
    '''function to call emotion_detector in order to analyze'''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is not None:
        return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear':{response['fear']}, 'joy':{response['joy']} and 'sadness':{response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    '''rendering index.html'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
