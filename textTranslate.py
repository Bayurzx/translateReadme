from dotenv import load_dotenv
import os
import requests, json


def main(text, to_lang_arr):
    global translator_endpoint
    global cog_key
    global cog_region

    try:
        # Get Configuration Settings
        load_dotenv()
        cog_key = os.getenv('COG_SERVICE_KEY')
        cog_region = os.getenv('COG_SERVICE_REGION')
        translator_endpoint = 'https://api.cognitive.microsofttranslator.com'
        # translator_endpoint = os.getenv('TRANSLATOR_ENDPOINT')


        translation = Translate(text, to_lang_arr)
        return translation
        

    except Exception as ex:
        print(ex)


def Translate(text, to_lang_arr):
    # make the array unique and remove "en"
    to_lang_arr = set(to_lang_arr)
    to_lang_arr = list(to_lang_arr)

    # Use the Translator translate function
    path = '/translate'
    url = translator_endpoint + path

    # Build the request
    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': to_lang_arr
    }

    headers = {
        'Ocp-Apim-Subscription-Key': cog_key,
        'Ocp-Apim-Subscription-Region': cog_region,
        'Content-type': 'application/json'
    }

    body = [{
        'text': text
    }]

    # Send the request and get response
    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()
    # print("response", response)
    

    new_res = {_abc['to']: _abc["text"]
               for _abc in response[0]['translations']}

    return new_res

if __name__ == "__main__":
    main(text, to_lang_arr)
