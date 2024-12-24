import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = json_data, headers = header)  # Send a POST request to the API with the text and headers
    formatted = json.loads(response.text)
    emotions = formatted['emotionPredictions'][0]['emotion']
    #print(emotions)
    key_value_max = max(zip(emotions.values(), emotions.keys()))[1]
    #print(key_value_max)
    emotions.update( {"dominant_emotion" : key_value_max})
    #print(emotions)
    return emotions
