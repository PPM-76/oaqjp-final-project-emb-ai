# import the Python requests libary to send client's request to the server
import requests

def emotion_detector(text_to_analyse):
    ''' emotion_detector use Watson NLP Library to asses the emotion of a provided string.
        Argument: (str) - text to analyse
        Output: (str) -  text including sentiment   
    '''
    # URL to IBM Watson NP cloud library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Header to specify the model ID to be used
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # json input payload to Watson NLP lib.
    input_json = {"raw_document": { "text": text_to_analyse }}
    
    # Send POST request to the Watson NLP API
    response = requests.post(url,json=input_json,headers=header)
    
    # Return the raw text extracted from the requests' object "response"
    return response.text





 #Output: (Dict) -  label and score.
 #                         label is the emtion class.
 #                         score is  the confidence. Score range = [0,1], with 1 max confidence.   
 #   '''