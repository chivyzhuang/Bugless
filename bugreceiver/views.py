# -*e coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bugreceiver.operation import process_bug_report, process_java_bug_detail, process_native_bug_detail, testo


@csrf_exempt
def receive_bug_report(request):
    message = str(request.body)
    if message:
        ret = process_bug_report(message)
    else:
        ret = 'Error'
    return HttpResponse(ret)


@csrf_exempt
def receive_java_bug_detail(request):
    message = str(request.body)
    if message:
        ret = process_java_bug_detail(message)
    else:
        ret = 'Error'
    return HttpResponse(ret)


@csrf_exempt
def receive_native_bug_detail(request):
    message = str(request.body)
    if message:
        ret = process_native_bug_detail(message)
    else:
        ret = 'Error'
    return HttpResponse(ret)


def test(request):
    ret = testo()
    return HttpResponse(ret)
