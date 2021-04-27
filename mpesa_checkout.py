# import the Flask Framework
import flask
import requests
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


# Create the context (endpoint/URL) which will be triggered when the request
# hits the above specified port. This will resolve to a URL like
# 'http://address:port/context'. E.g. the context below would
# resolve to 'http://127.0.0.1:80/mpesa/b2c/v1' on the local computer. Then
# the Handler will handle the request received via the given URL.

# You may create a separate URL for every endpoint you need

@app.route('/mpesa', methods=["POST", "GET"])
def listenLNM():
    # save the data
    # request_data = request.data
    BusinessShortCode = flask.request.args.get('BusinessShortCode')
    Password = flask.request.args.get('Password')
    Timestamp = flask.request.args.get('Timestamp')
    Amount = flask.request.args.get('Amount')
    PartyA = flask.request.args.get('PartyA')
    PartyB = flask.request.args.get('PartyB')
    Phonenumber = flask.request.args.get('Phonenumber')
    CallBackURL = flask.request.args.get('CallbackURL')
    AccountReference = flask.request.args.get('AccountReference')
    TransactionDesc = flask.request.args.get('TransactionDesc')


    access_token = "rGjeBha3PM7JERCAdY2STTX7slD5"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": BusinessShortCode,
        "Password": Password,
        "Timestamp": Timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": Amount,
        "PartyA": PartyA,
        "PartyB": PartyB,
        "PhoneNumber": Phonenumber,
        "CallBackURL": CallBackURL,
        "AccountReference": AccountReference,
        "TransactionDesc": TransactionDesc
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

    # Perform your processing here e.g. print it out...

    # Prepare the response, assuming no errors have occurred. Any response
    # other than a 0 (zero) for the 'ResultCode' during Validation only means
    # an error occurred and the transaction is cancelled
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": "1234567890"
    };

    # Send the response back to the server
    return jsonify({'message': message}), 200


# Change this part to reflect the API you are testing
@app.route('/mpesa/b2b/v1')
def listenB2b():
    request_data = request.data
    print(request_data)
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": "1234567890"
    };

    return jsonify({'message': message}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)