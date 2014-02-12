# -*- coding: utf-8 -*-
import message_pb2
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from usermanager.operator import update_user


@csrf_exempt
def receive_bug(request):
    # get the bug report object
    bug_report = message_pb2.BugReport()
    message = str(request.body)
    bug_report.ParseFromString(message)

    # process
    update_user(
            bug_report.user_id,
            bug_report.phone_product,
            bug_report.phone_model,
            bug_report.phone_system_sdk_version)

    return HttpResponse("You're looking at poll %s." % bug_report.phone_model)
