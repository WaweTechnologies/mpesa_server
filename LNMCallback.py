from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
import requests
from flask_mpesa import MpesaAPI
import time
import json
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
#run_with_ngrok(app)


def getToken():
    consumer_key = "aGhPIiqKd0woACQIu0Wdez9xw8l4oR43"
    consumer_secret = "SYYixpy9HBHNjW0X"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    access_token = mpesa_access_token['access_token']

    return access_token


@app.route("/checkout")
def checkout():
    access_token = getToken()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": "174379",
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjEwNDIyMTYwMTMw",
        "Timestamp": "20210422160130",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": "254791802040",
        "PartyB": "174379",
        "PhoneNumber": "254791802040",
        "CallBackURL": "http://b4f17ae728e2.ngrok.io",
        "AccountReference": "Test",
        "TransactionDesc": "Test"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)
    return str(response)


@app.route("/", methods=['POST', 'GET'])
def callback():
    # get json data set to this route
    json_data = request.get_json()
    # get result code and probably check for transaction success or failure
    #result_code = json_data["Body"]["stkCallback"]["ResultCode"]
    # message = {
     #    "ResultCode": 0,
    #    "ResultDesc": "success",
    #    "ThirdPartyTransID": "h234k2h4krhk2"
    #}
    #print(json_data)
    # if result code is 0 you can proceed and save the data else if its any other number you can track the transaction
    # return jsonify(message), 200
    return json_data
    '''result = requests.get(api_url)
    print(result)'''


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)