from django.db import models
from usermanager.models import User
from bsdiff.models import ApkPackage


class JavaBug(models.Model):
    count = models.IntegerField(default=1)
    apk = models.ForeignKey(ApkPackage)
    report_content = models.TextField()
    exception_type = models.CharField(max_length=50)
    source_class = models.CharField(max_length=50)
    source_method = models.CharField(max_length=50)
    source_line = models.IntegerField(default=0)
    tag = models.CharField(max_length=32)
    # 'Y' or 'N'
    is_fix = models.CharField(max_length=1, default='N')  
    is_complete = models.CharField(max_length=1, default='N')
    date = models.DateTimeField('date reported')
    model = models.CharField(max_length=100)
    system_sdk = models.IntegerField(default=7)

#    def __unicode__(self):
#        return 'Type:' + self.bug_type + \
#                " ReportLocation:" + self.report_file_path

class NativeBug(models.Model):
    count = models.IntegerField(default=1)
    apk = models.ForeignKey(ApkPackage)
    report_content = models.TextField()
    tag = models.CharField(max_length=32)
    # 'Y' or 'N'
    is_fix = models.CharField(max_length=1, default='N')  
    is_complete = models.CharField(max_length=1, default='N')
    date = models.DateTimeField('date reported')
    model = models.CharField(max_length=100)
    system_sdk = models.IntegerField(default=7)