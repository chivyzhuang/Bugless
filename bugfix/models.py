from django.db import models
from bugreceiver.models import JavaBug


class FixPackage(models.Model):
    file_path = models.CharField(max_length=200)
    file_md5 = models.CharField(max_length=32)


class JavaFixMap(models.Model):
    bug = models.ForeignKey(JavaBug)
    package = models.ForeignKey(FixPackage)
