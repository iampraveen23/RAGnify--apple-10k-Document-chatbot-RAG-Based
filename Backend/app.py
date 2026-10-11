'''
    REAL TIME JOB
    1.create a flask function that takes question from postman
    2.read the question from json
    3.Load local faiss db
    4.Ask the question to the faiss db and get relevant chunks
    5.make a prompt with the relevant chunks and question
    6.send the prompt to the open ai llm model 
    7.get responses from op ai and return to postman or ui in json format 
 
'''

from flask import Flask, request, jsonify
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from google import genai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# load API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("Gemini_api_key")
                                      
@app.route('/ask', methods=['POST'])
def f1():
    # Step 1: Receive JSON data
    data = request.get_json()

    if not data or not data.get('question'):
        return jsonify({'error': 'Please provide a question'}), 400

    # Step 2: Extract the question
    question = data['question']

    # Step 3: Load embeddings and FAISS index
    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-mpnet-base-v2'
    )

    my_vector_stores = FAISS.load_local(
        'faiss_db',
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Step 4: Retrieve relevant chunks
    docs = my_vector_stores.similarity_search(question)
    chunks = [doc.page_content for doc in docs]

    # Step 5: Create the prompt
    my_prompt = f"""
    Answer the question using ONLY the provided context.
    If the context does not contain the answer, say:
    "I could not find the answer in the provided context."
    Do not use outside knowledge.

    Question: {question}
    Context:{chunks}

    """

    # Step 6: Call the Gemini API
    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=my_prompt
    )

    answer = response.text

    # Step 7: Return the answer as JSON
    return jsonify({'result': answer})


if __name__ == '__main__':
    app.run(debug=True)
