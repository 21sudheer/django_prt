from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# from django.contrib.auth.models import Abstractuser


# Create your models here.
class User(models.Model):
    pass


class registration(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone_number = models.IntegerField()
