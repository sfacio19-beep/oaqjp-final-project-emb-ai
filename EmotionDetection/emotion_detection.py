import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)

    # Parse the JSON response
    response_dict = json.loads(response.text)

    # Extract the emotions dictionary
    emotions = response_dict['emotionPredictions'][0]['emotion']

    # Find the dominant emotion (the one with the highest score)
    dominant_emotion = max(emotions, key=emotions.get)

    # Add dominant_emotion to the output dictionary
    emotions['dominant_emotion'] = dominant_emotion

    return emotions
