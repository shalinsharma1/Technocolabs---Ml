# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:50:58 2020

@author: Shalin
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('blood_donation.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    if(prediction==0):
        return render_template('home.html', prediction_text="The donor will not give blood")
    else:
        return render_template('home.html', prediction_text="The donor will give blood")


if __name__ == "__main__":
    app.run()