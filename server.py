from logging import debug
from os import name
from flask import Flask, render_template, request, jsonify
import util


app = Flask(__name__)


@app.route('/get_column_names')
def get_column_names():
    response = {'Columns': util.column_names()}
    return response

@app.route('/predict_bike_price',methods=['POST'])
def predict_bike_price():
    kms_driven = float(request.form['KMS_DRIVE'])
    age = float(request.form['AGE'])
    power = float(request.form['POWER'])
    bike_name = request.form['BIKE_NAME']
    city = request.form['CITY'] 
 
    
    response = jsonify({'estimated_price': util.get_predicted_price(kms_driven, age, power, bike_name, city)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


app.run(host='127.0.0.1', port=5000)