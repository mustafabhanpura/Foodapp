from django.db import models
from django.contrib.auth.admin import User
# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=20,default=None)
    address=models.CharField(max_length=50,default=None)
    contact_number=models.CharField(max_length=100,default=None)
    date_of_birth=models.DateField(null=True)
    grand_total=models.CharField(max_length=200,default=None)


    def __str__(self):
        return self.name