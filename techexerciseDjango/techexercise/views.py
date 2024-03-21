from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializers import *

# Create your views here.

class TestView(APIView):
    def get(self, request):
        # output = [{
        #     "id": output.id,
        #     "pokemonName": output.pokemonName,
        #     "HPpts": output.HPpts,
        #     "ATTACKpts": output.ATTACKpts,
        #     "DEFENSEpts": output.DEFENSEpts,
        #     "SPEEDpts": output.SPEEDpts,
        #     "SPATTACKpts": output.SPATTACKpts,
        #     "SPDEFENSEpts": output.SPDEFENSEpts,
        # } for output in Pokemon.objects.all()]
        # return Response(output)

        requestData = request.query_params['email']
        output = [{
            "id": output.id,
            "pokemonID": output.pokemonID,
            "email": output.email,
        } for output in pokemonUserCollection.objects.filter(email=requestData)]
        pokemonNames = []
        for value in output:
            pokemon = value['pokemonID'].pokemonName
            pokemonNames.append(pokemon)
        jsonData = {"pokemonNames": pokemonNames}
        return Response(jsonData)
    
    def post(self, request):
        # userManager = UserManager.create_user(date=request.data)
        # if userManager.is_valid(raise_exception=True):
        #     userManager.save()
        #     return Response(userManager.data)
        
        pokemonUserCollectionSerializer = PokemonUserCollectionSerializer(data=request.data)
        if pokemonUserCollectionSerializer.is_valid(raise_exception=True):
            pokemonUserCollectionSerializer.save()
            return Response(pokemonUserCollectionSerializer.data)
        
class Loginview(APIView):
    def get(self, request):
        return Response("no GET method logic, but working fine", status=200)
        # return Response(request.GET.get("email"), status=200)


    def post(self, request):
        jsonData = request.data
        email = jsonData["email"]
        password = jsonData["password"]
        output = Users.objects.filter(email=email, password=password)
        if not output:
            print("empty, no account found")
            return Response("false", status=403)
        else:
            print("not empty")
            return Response("true", status=202)
    # {"email":"test@email.com","password":"password"}
        
class SignupView(APIView):
    def get(self, request):
        return Response("no GET method logic, but working fine", status=200)

    def post(self, request):
        print(request.data)
        userSignupSerializer = UserSignupSerializer(data=request.data)
        if userSignupSerializer.is_valid(raise_exception=True):
            userSignupSerializer.save()
            return Response("User Created", status=200)
        
class DeleteView(APIView):
    def get(self, request):
        return Response("no GET method logic, but working fine", status=200)

    def post(self, request):
        jsonData = request.data
        email = jsonData["email"]
        pokemonName = jsonData["pokemonName"]
        pokemonQuery = Pokemon.objects.filter(pokemonName=pokemonName)
        for value in pokemonQuery:
            pokemonID = value.id
        pokemonUserCollection.objects.filter(id__in=list(pokemonUserCollection.objects.values_list('pk', flat=True)[:1]), pokemonID=pokemonID, email=email).delete()
        return Response()
