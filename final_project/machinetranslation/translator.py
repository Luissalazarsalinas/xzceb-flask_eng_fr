import json
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(APIKEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2022-08-28',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

def english_to_french(englishtext):
    """This Funtion translate from English to French"""
    #write the code here
    try:
        translate = LANGUAGE_TRANSLATOR.translate(
            text = englishtext, 
            model_id = "en-fr").get_result()
        
        french_text = translate.get("translations")[0]["translation"] 
        return french_text
    except ApiException as aex:
        return aex.message 

def french_to_english(frenchtext):
    """ This Funtion translate from French to English"""
    #write the code here
    try:
        translate = LANGUAGE_TRANSLATOR.translate(
            text = frenchtext, 
            model_id = "fr-en").get_result()
        english_text = translate.get("translations")[0]["translation"] 
        return english_text
    except ApiException as aex:
        return aex.message