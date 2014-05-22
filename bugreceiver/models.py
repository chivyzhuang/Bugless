from django.db import models
from bsdiff.models import ApkPackage
from bugfix.models import FixPackage


class JavaBug(models.Model):
    count = models.IntegerField(default=1)
    apk = models.ForeignKey(ApkPackage)
    report_content = models.TextField(blank=True, null=True)
    exception_type = models.CharField(max_length=50)
    source_class = models.CharField(max_length=50)
    source_method = models.CharField(max_length=50)
    source_line = models.IntegerField(default=0)
    tag = models.CharField(max_length=32)
    FIX_TYPE = (
            ('N', 'NoRepair'),
            ('P', 'Package'),
            ('U', 'Update'),
    )
    is_fix = models.CharField(max_length=1, choices=FIX_TYPE, default='N')  
    is_complete = models.CharField(max_length=1, default='N')
    date = models.DateTimeField('date reported')
    model = models.CharField(max_length=100)
    system_sdk = models.IntegerField(default=7)
    repair_package = models.OneToOneField(FixPackage, blank=True, null=True)
    is_repair_published = models.BooleanField(default=False)

#    def __unicode__(self):
#        return 'Type:' + self.bug_type + \
#                " ReportLocation:" + self.report_file_path

class NativeBug(models.Model):
    count = models.IntegerField(default=1)
    apk = models.ForeignKey(ApkPackage)
    report_content = models.TextField()
    tag = models.CharField(max_length=32)
    FIX_TYPE = (
            ('N', 'NoRepair'),
            ('P', 'Package'),
            ('U', 'Update'),
    )
    is_fix = models.CharField(max_length=1, choices=FIX_TYPE, default='N')  
    is_complete = models.CharField(max_length=1, default='N')
    date = models.DateTimeField('date reported')
    model = models.CharField(max_length=100)
    system_sdk = models.IntegerField(default=7)
    repair_package = models.OneToOneField(FixPackage, blank=True, null=True)
    is_repair_published = models.BooleanField(default=False)