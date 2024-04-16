# # Libraries
# from langchain_google_genai import ChatGoogleGenerativeAI, HarmCategory, HarmBlockThreshold
# from langchain import PromptTemplate
# from langchain.chains.question_answering import load_qa_chain
# from langchain.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.vectorstores import Chroma
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
#
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
#
# def file_load(filename):
#     loader = PyPDFLoader(filename)
#     doc = loader.load()
#     return doc
#
#
# def context_generator(doc):
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=200)
#     context = "\n\n".join(str(p.page_content) for p in doc)
#     texts = text_splitter.split_text(context)
#     return [context, texts]
#
#
# def embedding_generation(texts):
#     embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv('API_KEY_XXX'))
#     vector_index = Chroma.from_texts(texts, embeddings).as_retriever()
#     return vector_index
#
#
# def set_prompt():
#     prompt_template = """
#     I am using this model in a machine which defines whether a person is revealing any information to the other person in their chat.
#     I will provide you with some rules and the text of the chat to check whether the chat is within the organizations policy boundations.
#     The chat of the user here is with any large language model available in the market.
#
#     Note: If the information contains dummy parameters enclosed in <> (angular) brackets then allow the request as the real data is already been replaced with placeholder and the part is safe.
#
#     Output format should be a json object and should have two parameters.
#     First parameter is `flag` which is 0 if request is safe and within bounds of the rules otherwise is 1
#     Second parameter is an array `errors` which is blank if request is safe and if the request is not safe, then it should add element in the array for each rule broken.
#     If there are multiple errors then create an element in array for every error in the errors array and do not concatenate 2 violations in one.
#     If error is there, then simplify the error into multiple statements and make each statement the part of array.
#     No need to give markdowns for json in the start and end.
#
#     Rules:
#     {context}
#
#     Text to check:
#     {question}
#     """
#     prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
#     return prompt
#
#
# def build_model(temperature):
#     model = ChatGoogleGenerativeAI(model="gemini-pro",
#                                    google_api_key=os.getenv('API_KEY_XXX'),
#                                    temperature=temperature,
#                                    safety_settings={
#                                        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
#                                        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
#                                        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
#                                        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE
#                                    })
#     return model
#
#
# def load_chain(model, prompt):
#     chain = load_qa_chain(model,
#                           chain_type="stuff",
#                           prompt=prompt)
#     return chain
#
#
# ##############################################
# # To be ran with every request
# ##############################################
#
# def required_doc(question, vector_index):
#     required_vector = vector_index.get_relevant_documents(question)
#     return required_vector
#
#
# def response_generator(chain, required_vector, question):
#     response = chain({"input_documents": required_vector, "question": question}, return_only_outputs=True)
#     return response
