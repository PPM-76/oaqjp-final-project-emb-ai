# import json to convert the response text into a dictionary
import json
# import the Python requests libary to send client's request to the server
import requests


def emotion_detector(text_to_analyse):
    ''' emotion_detector use Watson NLP Library to asses the emotion of a provided string.
        Argument: (str) - text to analyse
        Output: (dict) -  dict with emotions (keys) and scores (values) and key with max score  
    '''
    # URL to IBM Watson NP cloud library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Header to specify the model ID to be used
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # json input payload to Watson NLP lib.
    input_json = {"raw_document": { "text": text_to_analyse }}
    
    # Send POST request to the Watson NLP API
    response = requests.post(url,json=input_json,headers=header)
    # Convert the text response into a dictionary
    formatted_response = json.loads(response.text)

    # Extract the sub-dictionary containing the emotion scores
    dict_response = formatted_response['emotionPredictions'][0]['emotion']
    
    # get key with maximum score using max function
    max_score_emotion = max(dict_response, key=dict_response.get)
    
    # Add max emotion name to dictionary
    dict_response['dominant_emotion'] =  max_score_emotion
    
    # Return the dictionary containing the emotion scores from the requests' object "response"
    return dict_response
    

    




 #Output: (Dict) -  label and score.
 #                         label is the emtion class.
 #                         score is  the confidence. Score range = [0,1], with 1 max confidence.   
 #   '''