import os
import json
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

from .utils import fine_tuning_prompt_generator, rules_extraction_prompt_generator, fine_tuning_content_prompt_generator
from image.models import File


def get_llm_response_gemini(text):
    api_key = os.getenv('API_KEY_XXX')
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    context = ''
    rule_files = File.objects.all().filter(active=True).values()
    for file in list(rule_files):
        context = context + '\n\n' + file['content_extracted']

    response = model.generate_content(fine_tuning_prompt_generator(text, context),
                                      safety_settings={
                                          HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                                          HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                                          HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                                          HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE
                                      })
    llm_response = response.text
    print(llm_response)
    llm_response_json = json.loads(llm_response)
    return llm_response_json


def get_extracted_content_from_file(text):
    api_key = os.getenv('API_KEY_XXX')
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(rules_extraction_prompt_generator(text),
                                      safety_settings={
                                          HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                                          HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                                          HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                                          HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE
                                      })
    llm_response = response.text
    return llm_response


def fine_tuning_extracted_contents_from_file(text, fine_tuning_prompt):
    api_key = os.getenv('API_KEY_XXX')
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(fine_tuning_content_prompt_generator(text, fine_tuning_prompt),
                                      safety_settings={
                                          HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                                          HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                                          HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                                          HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE
                                      })
    llm_response = response.text
    return llm_response
