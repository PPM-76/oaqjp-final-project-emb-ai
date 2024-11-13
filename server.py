from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initialiase the application
app = Flask(__name__)

@app.route('/emotionDetector')
def request_analyser():
    ''' Request sentiment analysis to the EmotionDetection package
    '''
    # Request and parse the URL key "textToAnalyze" to get the user input
    text_to_analyse = request.args.get('textToAnalyze')
    # call the analysis function. text_analysed  is a dictionary
    text_analysed = emotion_detector(text_to_analyse)
    # Build response
    # get dominant emotion and remove it from the dictionary
    dominant_emotion = text_analysed.pop('dominant_emotion')
    # iterate over the remainder of the dictionary to construct the emotion string.
    emotion_str = ", ".join(f"'{key}' : {value}" for key, value in text_analysed.items())
    # Build the response to provide to the user
    response_to_user = (
        f'For the given statement, the system response is {emotion_str}.' 
        f' The dominant emotion is <b>{dominant_emotion}</b>.'
        )

    return response_to_user

@app.route('/')
def render_page_index():
    ''' Start the rendering of the main application page in Flask.
    ''' 
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='localhost', port=5000)

    