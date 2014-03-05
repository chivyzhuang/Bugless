from django.db import models


class User(models.Model):
    unique_id = models.CharField(max_length=50, primary_key=True)
    product = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    system_sdk = models.IntegerField(default=7)
    

class Group(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User)
