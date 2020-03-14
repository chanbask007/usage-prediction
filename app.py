#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 01:27:30 2020

@author: chanbas
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime
import pickle


app = Flask(__name__)
model= pickle.load(open('model.pkl','rb'));

@app.route('/')
def welcome():
    return "hello world..!!"
#
# @app.route('/<string:name>')
# def hello_world(name):
#     now = datetime.datetime.now()
#     is_new_year= now.month==1 and now.day==1
#     return render_template("index.html", is_new_year= is_new_year)

# @app.route('/hello',methods=["post"])
# def hello():
#     name= request.form.get("name");
#     return render_template("hello.html", name=name)
#
@app.route('/predict', methods=["POST","GET"])
def predict_api():
    now = datetime.strptime('2019-09-06 8:01:30', "%Y-%m-%d %H:%M:%S")
    timestamp = datetime.timestamp(now)
    prediction=model.predict([[240.4,1.02,16.45,0.92,timestamp]])

    print(prediction)
    return render_template("prediction.html",prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
