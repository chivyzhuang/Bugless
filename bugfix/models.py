from django.db import models


class FixPackage(models.Model):
    file_path = models.CharField(max_length=200)
    file_md5 = models.CharField(max_length=32)
    brief = models.TextField(blank=True, null=True)