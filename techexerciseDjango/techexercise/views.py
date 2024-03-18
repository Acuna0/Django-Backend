from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response

# Create your views here.

class TestView(APIView):
    def get(self, request):
        test = {
            'name': 'etes'
        }
        output = [{
            "email": output.email,
            "name": output.name
        } for output in TestObject.objects.all()]
        return Response(output)
    
    def post(self, request):
        userManager = UserManager.create_user(date=request.data)
        if userManager.is_valid(raise_exception=True):
            userManager.save()
            return Response(userManager.data)