from rest_framework import serializers
from abc_mpesa.models import lipaMpesaOnline


class lipaMpesaOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = lipaMpesaOnline
        fields = 'id'