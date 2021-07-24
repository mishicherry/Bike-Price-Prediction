import pickle
import json
import numpy as np

_data_columns = None
_model = None

def get_predicted_price(kms_driven, age, power, bike_name, city):
    input = np.zeros(len(_data_columns))
    input[0] = kms_driven
    input[1] = age
    input[2] = power

    bike_name = _data_columns.index(bike_name)
    input[bike_name] = 1

    city = _data_columns.index(city)
    input[city] = 1
    
    return _model.predict([input])[0][0]

def load_artifacts():
    global _data_columns
    global _model
    
    print('Loading Artifacts...')

    with open('./columns.json','r') as f:
        _data_columns = json.load(f)['data_columns']

    with open('./bike_prediction.pickle','rb') as f:
        _model = pickle.load(f)

    print('Artifacts...Loaded')


def column_names():
    return _data_columns
    

load_artifacts()
print(get_predicted_price(9900, 5, 200, 'bajaj pulsar ns200', 'bangalore'))
#print(column_names())