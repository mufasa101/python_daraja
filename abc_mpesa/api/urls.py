from django.contrib import admin
from django.urls import path, include
from abc_mpesa.api.views import lipaMpesaOnlineCallbackUrlAPIView

urlpatterns = [
    path("lnm/", lipaMpesaOnlineCallbackUrlAPIView.as_view(), name="lnm-callbackurl"),
]
