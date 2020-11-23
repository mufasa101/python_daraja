import requests
from requests.auth import HTTPBasicAuth
import mpesa_keys


def generate_access_token():
    consumer_key = mpesa_keys.consumer_key
    consumer_secret = mpesa_keys.consumer_secret

    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    # access_token = r.json()['access_token']

    json_response = r.json()
    my_access_token = json_response['access_token']

    return my_access_token
