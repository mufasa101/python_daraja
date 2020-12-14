from rest_framework.generics import CreateAPIView
from abc_mpesa.models import lipaMpesaOnline
from abc_mpesa.api.serializers import lipaMpesaOnlineSerializer 
# from rest_framework.permissions import IsAdminUser


class lipaMpesaOnlineCallbackUrlAPIView(CreateAPIView):
    queryset = lipaMpesaOnline.objects.all()
    serializer_class = lipaMpesaOnlineSerializer
    # permission_classes = [IsAdminUser]
    
    def create(self,request):
        print(request.data,"This is a request data")
