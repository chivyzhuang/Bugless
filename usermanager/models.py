from django.db import models


class PhoneUser(models.Model):
    unique_id = models.CharField(max_length=50, primary_key=True)
    product = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    system_sdk = models.IntegerField(default=7)
