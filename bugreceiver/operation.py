# -*- coding: utf-8 -*-
import message_pb2
from bugreceiver.models import JavaBug
from usermanager.models import User
from usermanager.operator import update_user


def process_java_bug_report(report, tag, user):
    try:
        record = JavaBug.objects.get(
                package_name=report.app_package_name,
                version_code=report.app_version_code,
                tag=tag.tag
        )
        record.count += tag.count
        return record.is_complete
    except JavaBug.DoesNotExist:
        record = JavaBug.objects.create(
                package_name=report.app_package_name,
                version_code=report.app_version_code,
                tag=tag.tag,
                report_user=user
        )
        return True


def process_native_bug_report(report, tag, user):
    return 'b'


def process_kernel_bug_report(report, tag, user):
    return 'c'


processor = {
        message_pb2.JAVA: process_java_bug_report,
        message_pb2.NATIVE: process_native_bug_report,
        message_pb2.KERNEL: process_kernel_bug_report
}


def filter_bug_report(message):
    # get the bug report object
    bug_report = message_pb2.BugReport()
    bug_report.ParseFromString(message)
    # process_user
    user = update_user(
            bug_report.user_id,
            bug_report.phone_product,
            bug_report.phone_model,
            bug_report.phone_system_sdk_version
    )
    # process_report
    report_feed = message_pb2.ReportFeed()
    for tag in bug_report.tags:
        bug_feed = report_feed.feeds.add()
        bug_feed.type = tag.type
        bug_feed.tag = tag.tag
        bug_feed.answer = processor.get(tag.type)(bug_report, tag, user)
    return report_feed.SerializeToString()


def testo():
    return processor.get(message_pb2.JAVA)(message_pb2.BugReport.BugTag())
