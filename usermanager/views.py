# -*e coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from usermanager.operation import update_user


@csrf_exempt
def update(request):
    message = str(request.body)
    if message:
        ret = update_user(message)
    else:
        ret = 'Error'
    return HttpResponse(ret)