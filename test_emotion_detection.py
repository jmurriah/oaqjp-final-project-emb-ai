from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], 'joy')