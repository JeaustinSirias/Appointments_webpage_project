from django.db import models
from django.contrib.auth.models import User

'''
class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
'''

class appointment(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=30)
    