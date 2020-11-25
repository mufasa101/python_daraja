
import requests
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token
from encode import generate_password 
from utils import get_timestamp 
import mpesa_keys
# print(decoded_password)
  # With cUrl, you can just pass the correct header with each request
my_access_token = generate_access_token()
formatted_time = get_timestamp()
decoded_password = generate_password(formatted_time)
# print(my_access_token,"This is an access token")
def lipa_na_mpesa():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": mpesa_keys.business_code,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": mpesa_keys.phone_number,
        "PartyB":mpesa_keys.business_code,
        "PhoneNumber": mpesa_keys.phone_number,
        "CallBackURL": "https://fullstackdjangotest.com",
        "AccountReference": "BBC-17-a",
        "TransactionDesc": "Pay rent"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)
lipa_na_mpesa()

