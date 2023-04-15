import flask
from flask import Flask,render_template,request
import pickle
import numpy as np

from flask_ngrok import run_with_ngrok
import warnings

warnings.filterwarnings ('ignore')

app= Flask(__name__)
run_with_ngrok(app)

model = pickle.load(open('ANN_model.pkl', 'rb'))


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['GET', "POST"])
def predict():
    input_values = [float(x) for x in request.form.values()]
    inp_features = [input_values]
    print(inp_features )
    prediction = model.predict(inp_features)
    if prediction == 1:
        return render_template('index.html', prediction_text='you are eligible to admit')
    else:
        return render_template('index.html', prediction_text='you are Not eligible to admit')


app.run()
