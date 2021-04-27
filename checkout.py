from flask import Flask, request, jsonify, Response, abort
from flask_ngrok import run_with_ngrok
import requests
from flask_mpesa import MpesaAPI
import time
import json
from requests.auth import HTTPBasicAuth
import datetime
import base64



app = Flask(__name__)
# run_with_ngrok(app)

def get_password(timestamp):
    shortcode = str(174379)
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    strencode = shortcode + passkey + timestamp
    passbytes = bytes(strencode, 'utf-8')
    base64_bytes = base64.b64encode(passbytes)
    password = base64_bytes.decode('utf-8')
    return password


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
    currentDT = datetime.datetime.now()
    timestamp = currentDT.strftime("%Y%m%d%H%M%S")
    access_token = getToken()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": "174379",
        "Password": 'MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjEwNDI3MDc1NTM2',
        "Timestamp": '20210427075536',
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": "254791802040",
        "PartyB": "174379",
        "PhoneNumber": "254791802040",
        "CallBackURL": "http://35b4f3f4def0.ngrok.io/callback",
        "AccountReference": "Test",
        "TransactionDesc": "Test"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)
    return str(response)


@app.route("/callback", methods=['POST'])
def callback():
    # get json data set to this route
    if request.method == "POST":
        print("received hook")
        json_data = request.json()
        print(json_data)
        return Response(status=200)
    else:
        abort(400)


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)