# -*e coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from update.operation import check_update


@csrf_exempt
def ask_update(request):
    message = str(request.body)
    if message:
        ret = check_update(message)
    else:
        ret = 'Error'
    return HttpResponse(ret)