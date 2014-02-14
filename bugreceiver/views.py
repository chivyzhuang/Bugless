# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bugreceiver.operation import filter_bug_report, testo


@csrf_exempt
def receive_bug(request):
    message = str(request.body)
    if message:
        ret = filter_bug_report(message)
    else:
        ret = 'Error'
    return HttpResponse(ret)


def test(request):
    ret = testo()
    return HttpResponse(ret)
