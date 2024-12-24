# Import the Flask class from the flask module
from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector

# Create an instance of the Flask class, passing in the name of the current module
app = Flask("EmotionDetection")

@app.route("/emotionDetector/")
@app.route("/emotionDetector/<string:emotion>")
def emotion_detection(emotion = None):
    # Function that handles requests to the root URL
    emotions = emotion_detector(emotion)
    
    if emotions["dominant_emotion"] == None:
        return "Invalid text! Please try again!"

    res = "For the give statement, the system response is "
    for  key in emotions:
        if (key != "dominant_emotion"):
            res += " '" + key + "': " + str(emotions[key]) + ", "
    res = res[:-2]
    res += ". The dominant emotion is <b>" + emotions["dominant_emotion"] + "</b>."

    return res
