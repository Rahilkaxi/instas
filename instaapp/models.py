from django.db import models


# Create your models here.

class Getpassword(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    at = models.DateTimeField(auto_now_add=True)
