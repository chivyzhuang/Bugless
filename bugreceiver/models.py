from django.db import models
from usermanager.models import User
from bsdiff.models import ApkPackage


class JavaBug(models.Model):
    count = models.IntegerField(default=1)
    apk = models.ForeignKey(ApkPackage)
    report_file_path = models.CharField(max_length=200)
    brief = models.CharField(max_length=80)
    tag = models.CharField(max_length=32)
    # 'Y' or 'N'
    is_fix = models.CharField(max_length=1, default='N')  
    is_complete = models.CharField(max_length=1, default='N')
    date = models.DateTimeField('date reported')
    report_user = models.ForeignKey(User)

#    def __unicode__(self):
#        return 'Type:' + self.bug_type + \
#                " ReportLocation:" + self.report_file_path
