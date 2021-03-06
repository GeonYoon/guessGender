from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from .permissions import AnonPermissionOnly
from prediction import server_predictor

def most_common(lst):
    return max(set(lst), key=lst.count)

class FormAPIView(APIView):
    #authentication_classes      = []
    permission_classes          = []
   
    def post(self, request, *args, **kwargs):
        data = request.data
        about1 = data.get("about1");
        about2 = data.get("about2");
        nbcm, mnbcm, lcm = server_predictor.get_prediction(about1,about2)
        most_common_gender = most_common([nbcm,mnbcm,lcm])
        return Response({"nbcm_gender" : nbcm, "mnbcm_gender":mnbcm, "lcm_gender":lcm, "most_common_gender" : most_common_gender}, status=200)

    
        
        
