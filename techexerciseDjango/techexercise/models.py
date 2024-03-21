import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone

class CustomUserManager(UserManager):
    def _create_user(self, first_name, last_name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, password=password, **extra_fields)
        # user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, first_name=None, last_name=None, email=None, password=None, **extra_fields):
        return self._create_user(first_name, last_name, email, password, **extra_fields)
    
    def create_superuser(self, first_name=None, last_name=None, email=None, password=None, **extra_fields):
        return self._create_user(first_name, last_name, email, password, **extra_fields)
    
class PokemonManager():
    def changeRelationship(self, pokemonID):
        if pokemonID == None:
            raise ValueError("error has occured")
        else:
            pokemonUserCollection = self.model(pokemonID=pokemonID)
            pokemonUserCollection.save()

    def addPokemon(self, pokemonID=None):
        if pokemonID == None:
            raise ValueError("error has occured")
        else:
            pokemonUserCollection = self.model(pokemonID=pokemonID)
            pokemonUserCollection.save()
        return pokemonUserCollection

    def removePokemon(self, pokemonID=None):
        return self.changeRelationship(pokemonID)


    
# class User(AbstractBaseUser, PermissionsMixin):
#     id = models.AutoField(primary_key=True, editable=False)
#     first_name = models.CharField(max_length=75, blank=True, default='')
#     last_name = models.CharField(max_length=75, blank=True, default='')
#     email = models.EmailField(max_length=150, blank=True, default='', unique=True)

#     createOn = models.DateTimeField(default=timezone.now)
#     createdBy = models.CharField(max_length=3, default=0)
#     modifedOn = models.DateTimeField(blank=True, null=True)
#     modifiedBy = models.CharField(max_length=3, blank=True, null=True, default='')

#     isSuperuser = models.BooleanField(default=False)
#     lastLogin = models.DateTimeField(blank=True, null=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []
class Users(AbstractBaseUser):
    id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=75, blank=True, default='')
    last_name = models.CharField(max_length=75, blank=True, default='')
    email = models.EmailField(max_length=150, blank=True, default='', unique=True)
    password = models.CharField(max_length=50, default='', null=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

class TestObject(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    pokemonName = models.CharField(max_length=100, blank=False, default='')
    HPpts = models.CharField(max_length=10, blank=False, default='100000')
    ATTACKpts = models.CharField(max_length=10, blank=False, default='100000')
    DEFENSEpts = models.CharField(max_length=10, blank=False, default='100000')
    SPEEDpts = models.CharField(max_length=10, blank=False, default='100000')
    SPATTACKpts = models.CharField(max_length=10, blank=False, default='100000')
    SPDEFENSEpts = models.CharField(max_length=10, blank=False, default='100000')

class pokemonUserCollection(models.Model):
    id = models.AutoField(primary_key=True)
    pokemonID = models.ForeignKey("Pokemon", on_delete=models.CASCADE)
    email = models.EmailField(max_length=150, blank=True, default='')
