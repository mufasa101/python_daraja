from rest_framework.generics import CreateAPIView
from abc_mpesa.models import lipaMpesaOnline
from abc_mpesa.api.serializers import lipaMpesaOnlineSerializer 
from rest_framework.permissions import AllowAny


class lipaMpesaOnlineCallbackUrlAPIView(CreateAPIView):
    queryset = lipaMpesaOnline.objects.all()
    serializer_class = lipaMpesaOnlineSerializer
    permission_classes = [AllowAny]
    
    def create(self,request):
        print(request.data,"This is a request data")
        
        """
        {'Body':
            {'stkCallback':
             {
                'CheckoutRequestID': 'ws_CO_DMZ_401669274_11032019190235305',
                'MerchantRequestID': '19927-3244045-1',
                'ResultCode': 0,
                'ResultDesc': 'The service request is processed successfully.',
                'CallbackMetadata': {
                                        'Item': [
                                                {'Name': 'Amount', 'Value': 1.0},
                                                {'Name': 'MpesaReceiptNumber', 'Value': 'NCB1FW1DFZ'},
                                                {'Name': 'Balance'},
                                                {'Name': 'TransactionDate', 'Value': 20190311190244},
                                                {'Name': 'PhoneNumber', 'Value': 254718821114}
                                                ]
                                    }
                                    }
                }
        }
        """
        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        print(merchant_request_id, "This is the merchant request id")
        result_code = request.data["Body"]["stkCallback"]["ResultCode"]
        result_description = request.data["Body"]["stkCallback"]["ResultDesc"]
        amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0][
            "Value"
        ]
        print(amount, "this should be an amount")
        mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"][
            "Item"
        ][1]["Value"]
        print(mpesa_receipt_number, "this should be an mpesa_receipt_number")

        balance = ""
        transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"][
            "Item"
        ][3]["Value"]
        print(transaction_date, "this should be an transaction_date")

        phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][
            4
        ]["Value"]
        print(phone_number, "this should be an phone_number")
