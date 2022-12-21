"""translator.py"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#apikey = 'Y0SD8n3YC9Rc9tLsxmayTRXbstmrCuTPXaaJIwOgQFUS'
#url = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/f21c9f56-e19a-435a-88ef-ca23002507b0'

#
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)



def englishToFrench(englishText):
    """A dummy docstring."""
    #write the code here
    model_id = 'en-fr'
    text_to_translate = englishText

    # Translate
    french_text = language_translator.translate(
    text=text_to_translate,
    model_id=model_id).get_result()

    return french_text['translations'][0]['translation']

def frenchToEnglish(frenchText):
    """A dummy docstring."""
    #write the code here
    model_id = 'fr-en'
    text_to_translate = frenchText

    # Translate
    english_text = language_translator.translate(
    text=text_to_translate,
    model_id=model_id).get_result()
    return english_text['translations'][0]['translation']

#Print results
print(englishToFrench("hi"))
