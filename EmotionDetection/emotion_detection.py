import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_json, headers=header)
    formatted_response = json.loads(response.text)

    # Extract emotions and their scores from the 'emotionPredictions' list
    if response.status_code == 200:
        emotion_predictor = formatted_response.get('emotionPredictions', [])
        emotions = emotion_predictor[0].get('emotion', {})
        
        # Extract and return the result with error handling
        result = {
            'anger': emotions.get('anger'),
            'disgust': emotions.get('disgust'),
            'fear': emotions.get('fear'),
            'joy': emotions.get('joy'),
            'sadness': emotions.get('sadness'),
            'dominant_emotion': max(emotions, key=emotions.get)
            }
    
    elif response.status_code == 400:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }
    return result