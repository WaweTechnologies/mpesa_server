from flask import Flask, request, jsonify, Response, abort
from flask_ngrok import run_with_ngrok
import requests
from flask_mpesa import MpesaAPI
import time
import json
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
# run_with_ngrok(app)

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
    app.run('0.0.0.0', port=5002, debug=True)