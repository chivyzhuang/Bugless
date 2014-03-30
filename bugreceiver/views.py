# -*e coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bugreceiver.operation import filter_bug_report, process_java_bug_detail, testo


@csrf_exempt
def receive_bug_report(request):
    message = str(request.body)
    if message:
        ret = filter_bug_report(message)
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
def receive_native_bug(request):
    f = request.FILES['upload_file_minidump']
    destination = open('media/dump.txt', 'w+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.write('\nprod:' + request.POST['prod'])
    destination.write('\nver :' + request.POST['ver'])
    destination.close()
    return HttpResponse('EEE')


def test(request):
    ret = testo()
    return HttpResponse(ret)
