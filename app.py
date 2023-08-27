from flask import Flask, render_template, request, jsonify
import numpy as np
from fastai.vision import *
import pickle 
import io
from fastai.text import *
import os
from fastai import learner
from fastai.vision.all import *
import PIL
import torchvision.transforms as T
import requests

from flask import Flask, render_template, request, jsonify
import numpy as np
from fastai.vision import *
import pickle 
import io
from fastai.text import *
import os
from fastai import learner
from fastai.vision.all import *
import PIL
import torchvision.transforms as T
import requests

#from flask import Flask, render_template, request, jsonify
#import os
import openai  # Import the OpenAI Python library
import pickle

# Set your OpenAI GPT-3 API key
openai.api_key = "OpenAI API Key"  # Replace with your actual API key

cwd = os.getcwd()
path = cwd

app = Flask(__name__)

# Load your AI model
model = load_learner("all.pkl", cpu=True, pickle_module=pickle)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/upload', methods=["POST"])
def upload():
    if request.method == 'POST':
        file = request.files['image'].read()
        open('facebook.jpg', 'wb').write(file)
        # ... (existing code)

        prediction = "some value"

        # Chatbot interaction
        chat_prompt = f"Describe {prediction}."
        chat_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=chat_prompt,
            max_tokens=100
        )
        disease_description = chat_response.choices[0].text.strip()

        # ... (existing code)

        return render_template('results.html', prediction=prediction, sources=sources, rec=rec, rec2=rec2,
                               rec3=rec3, rec4=rec4, rec5=rec5, disease_description=disease_description)

if __name__ == '__main__':
    app.run(debug=True)
