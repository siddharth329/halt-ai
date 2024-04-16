# import json
# import time
#
# from .utils import *
# from image.models import File
#
#
# def get_llm_response_langchain(text):
#     context = ''
#     rule_files = File.objects.all().values()
#
#     start_time = time.time()
#     for file in list(rule_files):
#         context = context + '\n\n' + file['content_extracted']
#     end_time = time.time()
#     print(f'Content Extraction: {end_time - start_time} seconds')
#
#     start_time = time.time()
#     vector_index = embedding_generation(context)
#     prompt = set_prompt()
#     llm = build_model(temperature=0.0)
#     chain = load_chain(llm, prompt)
#     end_time = time.time()
#     required_vector = required_doc(text, vector_index)
#     print(f'Chain Generation: {end_time - start_time} seconds')
#
#     return json.loads(response_generator(chain, required_vector, text)['output_text'])
