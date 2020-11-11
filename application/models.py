from django.db import models
from django.contrib.auth.models import User

'''
class usuario(models.Model):
    user = models.OneToOneField(User, related_name='usuarios')
    first_name = models.CharField(max_length=30)
    #username = models.CharField(max_length=15)
    #password = models.CharField(max_length=10)
'''

DEPENDANT = [('Asesor 1', 'Ana Maria')]
class appointment(models.Model):
    '''The appointment model with its respective
    entries and __str__ definition'''
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=30)
    dependant = models.CharField(max_length=25, choices=DEPENDANT)

    def __str__(self):
        '''A method to display an appointment object
        as a readable string'''
        return "hay una cita a nombre de %s, el %s" %(self.name, self.date) 
    