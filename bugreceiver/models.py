from django.db import models
from usermanager.models import User


class Bug(models.Model):
    BUG_TYPE = (
        ('J', 'JAVA'),
        ('N', 'NATIVE'),
        ('K', 'KERNEL'),
    )

    count = models.IntegerField(default=0)
    package_name = models.CharField(max_length=50)
    version_code = models.IntegerField(default=0)
    bug_type = models.CharField(max_length=1, choices=BUG_TYPE)
    report_file_path = models.CharField(max_length=200)
    tag = models.CharField(max_length=20)
    is_ifx = models.CharField(max_length=1)  # 'Y' or 'N'
    report_user_id = models.ForeignKey(User)


    def __unicode__(self):
        return 'Type:' + self.bug_type + \
                " ReportLocation:" + self.report_file_path
