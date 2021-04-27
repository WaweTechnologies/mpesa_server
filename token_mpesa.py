from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
import requests
from requests.auth import HTTPBasicAuth
import base64
import datetime


def getToken():
    consumer_key = "aGhPIiqKd0woACQIu0Wdez9xw8l4oR43"
    consumer_secret = "SYYixpy9HBHNjW0X"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    access_token = mpesa_access_token['access_token']

    return access_token


def get_password():
    currentDT = datetime.datetime.now()
    shortcode = str(174379)
    timestamp = str(currentDT.strftime("%Y%m%d%H%M%S"))
    print(timestamp)
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    strencode = shortcode + passkey + timestamp
    passbytes = bytes(strencode, 'utf-8')
    base64_bytes = base64.b64encode(passbytes)

    #print(base64_bytes)
    password = base64_bytes.decode('utf-8')
    print(password)
    return password

get_password()

