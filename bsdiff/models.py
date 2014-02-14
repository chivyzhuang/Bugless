import os
from django.db import models


class ApkPackage(models.Model):
    package_name = models.CharField(max_length=50)
    version_code = models.IntegerField(default=0)
    file_path = models.CharField(max_length=200)
    file_md5 = models.CharField(max_length=32)

    def delete(self):
        try:
            os.remove(self.file_path)
        except OSError:
            pass
        super(ApkPackage, self).delete()

#    def __unicode__(self):
#        return 'Type:' + self.bug_type + \
#                " ReportLocation:" + self.report_file_path


class Patch(models.Model):
    file_path = models.CharField(max_length=200)
    file_md5 = models.CharField(max_length=32)
    pre_version_code = models.IntegerField(default=0)
    target_apk = models.ForeignKey(ApkPackage)

    def delete(self):
        try:
            os.remove(self.file_path)
        except OSError:
            pass
        super(Patch, self).delete()
