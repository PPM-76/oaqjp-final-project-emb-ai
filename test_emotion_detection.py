import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_dominant_emotion(self):
        resp1 = emotion_detector('I am glad this happened')
        self.assertEqual(resp1['dominant_emotion'],'joy')   
    def test_dominant_emotion(self):
        resp2 = emotion_detector('I am really mad about this')
        self.assertEqual(resp2['dominant_emotion'],'anger')    
    def test_dominant_emotion(self):
        resp3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(resp3['dominant_emotion'],'disgust')
    def test_dominant_emotion(self):
        resp4 = emotion_detector('I am so sad about this')
        self.assertEqual(resp4['dominant_emotion'],'sadness')
    def test_dominant_emotion(self):
        resp5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(resp5['dominant_emotion'],'fear')

unittest.main()