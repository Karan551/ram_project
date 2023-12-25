from django.db import models


# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=500)
    password = models.CharField(max_length=200, default=" ")

    def __str__(self):
        return self.name
