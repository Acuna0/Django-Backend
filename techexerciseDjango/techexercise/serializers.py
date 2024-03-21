from rest_framework import serializers
from . models import *

# Create your models here.

class PokemonUserCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = pokemonUserCollection
        fields = ["id", "pokemonID", "email"]

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["email", "password"]

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["first_name", "last_name", "email", "password"]

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "first_name", "last_name", "email", 
#                   "createdOn", "createdBy", "modifedOn", "modifedBy", 
#                   "modifedOn", "isSuperuser", "lastLogin"]