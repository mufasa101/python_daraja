import requests
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token
import mpesa_keys


my_access_token = generate_access_token()
access_token = my_access_token
def register_url():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {"ShortCode": mpesa_keys.short_code,
            "ResponseType": "Completed",
               "ConfirmationURL": "https://fullstackdjangotest.com/confirmation",
               "ValidationURL": "https://fullstackdjangotest.com/validation_url"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

# register_url()
def simulate_c2b_transaction():
  api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
  headers = {"Authorization": "Bearer %s" % my_access_token}
  request = { "ShortCode":mpesa_keys.short_code,
    "CommandID":"CustomerPayBillOnline",
    "Amount":"1",
    "Msisdn": mpesa_keys.test_mssdn,
    "BillRefNumber":"123344" }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)


simulate_c2b_transaction()
