from flask import Flask,jsonify,request,Response
from flask import request
from sklearn import linear_model
import os
import json
import pickle
app = Flask(__name__)
linReg = pickle.load(open('predict.pkl', 'rb'))
print('after model loaded')

@app.route('/predict', methods=['POST'])
def get_prediction():
    req_body = request.get_json(force=True)
    param1 = req_body['Size']
    param2 = req_body['Bedrooms']
    param3 = req_body['Age']
    param4 = req_body['Bathrooms']
    # Predict
    pred = linReg.predict([[param1, param2, param3,param4]])
    result = pred[0]
    msg = {
            "message": "Price is %s" % (result)
        }
    resp = Response(response=json.dumps(msg),
                        status=200,\
                        mimetype="application/json")
    return resp
if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0',port=5000)