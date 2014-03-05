# -*- coding: utf-8 -*-
import bugreport_pb2, time
from django.utils import timezone
from bugreceiver.models import JavaBug
from bsdiff.models import ApkPackage
from usermanager.operator import update_user


def process_java_bug_report(report, tag, user):
    try:
        apk = ApkPackage.objects.get(
                package_name=report.app_package_name,
                version_code=report.app_version_code
        )
    except ApkPackage.DoesNotExist:
        return True
    try:
        record = apk.javabug_set.get(
                tag=tag.tag
        )
        record.count += tag.count
        record.save()
        return record.is_complete == 'Y'
    except JavaBug.DoesNotExist:
        record = JavaBug.objects.create(
                apk=apk,
                tag=tag.tag,
                report_user=user,
                date=timezone.now()
        )
        return False


def process_native_bug_report(report, tag, user):
    return 'b'


def process_kernel_bug_report(report, tag, user):
    return 'c'


processor = {
        bugreport_pb2.JAVA: process_java_bug_report,
        bugreport_pb2.NATIVE: process_native_bug_report,
        bugreport_pb2.KERNEL: process_kernel_bug_report
}


def filter_bug_report(message):
    # get the bug report object
    bug_report = bugreport_pb2.BugReport()
    bug_report.ParseFromString(message)
    # process_user
    user = update_user(
            bug_report.user_id,
            bug_report.phone_product,
            bug_report.phone_model,
            bug_report.phone_system_sdk_version
    )
    # process_report
    report_feed = bugreport_pb2.ReportFeed()
    for tag in bug_report.tags:
        bug_feed = report_feed.feeds.add()
        bug_feed.type = tag.type
        bug_feed.tag = tag.tag
        bug_feed.answer = processor.get(tag.type)(bug_report, tag, user)
    return report_feed.SerializeToString()


def process_java_bug_detail(message):
    java_bug = bugreport_pb2.JavaBug()
    java_bug.ParseFromString(message)
    # save java bug detail
    try:
        # write file
        file_path = 'Storage/bug/java/%s' % time.time()
        file_object = open(file_path, 'w')
        file_object.write(java_bug.detail_info)
        file_object.close()
        # change record
        record = ApkPackage.objects.get(
                package_name=java_bug.app_package_name,
                version_code=java_bug.app_version_code
        ).javabug_set.get(
                tag=java_bug.tag
        )
        record.brief = java_bug.brief_info
        record.report_file_path = file_path
        record.is_complete = 'Y'
        record.save()
    except ApkPackage.DoesNotExist, JavaBug.DoesNotExist:
        return 'Error'
    return 'Success'


def testo():
    return processor.get(bugreport_pb2.JAVA)(bugreport_pb2.BugReport.BugTag())
