import os
from django.db import models
from django.contrib.auth.models import User


class ApkMark(models.Model):
    package_name = models.CharField(max_length=50, unique=True)
    app_name = models.CharField(max_length=50)
    brief = models.CharField(max_length=200, blank=True)
    version_code = models.IntegerField(default=0)
    users = models.ManyToManyField(User, through='Management')


class Management(models.Model):
    IDENTITY_TYPE = (
            ('O', 'Owner'),
            ('M', 'Member'),
    )
    mark = models.ForeignKey(ApkMark)
    user = models.ForeignKey(User)
    identity = models.CharField(max_length=1, choices=IDENTITY_TYPE, blank=False)


class ApkPackage(models.Model):
    package_name = models.CharField(max_length=50, blank=False)
    version_code = models.IntegerField(default=1, blank=False)
    file_path = models.CharField(max_length=100)
    file_md5 = models.CharField(max_length=32)
    target_mark = models.ForeignKey(ApkMark, blank=False)
    is_published = models.BooleanField(default=False)

    def delete(self):
        try:
            os.remove(self.file_path)
        except OSError:
            pass
        super(ApkPackage, self).delete()


class Patch(models.Model):
    file_path = models.CharField(max_length=200)
    file_md5 = models.CharField(max_length=32)
    pre_version_code = models.IntegerField(default=0)
    target_apk = models.ForeignKey(ApkPackage, blank=False)

    def delete(self):
        try:
            os.remove(self.file_path)
        except OSError:
            pass
        super(Patch, self).delete()
