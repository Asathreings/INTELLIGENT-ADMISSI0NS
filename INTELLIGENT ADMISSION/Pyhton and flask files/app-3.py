import flask
from flask import Flask, render_template, request
import pickle
import numpy as pd
#import sklearn

app = Flask(__name__)


model = pickle.load(open('lr.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/getdata', methods=['POST'])
def pred():
    grescore = int(request.form['GRE Score'])
    print(grescore)
    toeflscore= int(request.form['TOEFL Score'])
    print(toeflscore)
    university = int(request.form['University Rating'])
    print(university)
    sop= float(request.form['SOP'])
    print(sop)
    lor= float(request.form['LOR'])
    print(lor)
    cgpa = float(request.form['CGPA'])
    print(cgpa)
    research = int(request.form['Research'])
    print(research)
    final_features = [[grescore, toeflscore, university, sop, lor, cgpa, research]]

    print(final_features)
    prediction = model.predict(final_features)
    print(type(prediction))
    t = prediction[0]
    print(t)
    if t > 0.80:
        prediction_text = 'Eligible to admit'
    else:
        prediction_text = 'Not eligible to admit'
    print(prediction_text)
    return render_template('newresults.html', prediction_results=prediction_text)


if __name__ == "__main__":
    app.run()
