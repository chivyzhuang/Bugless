from django.shortcuts import render
from download.operation import download_file


def get_apk(request, pkg_name, f_name):
    return download_file(
            request,
            'media/apk/%s/%s' % (pkg_name, f_name)
    )


def get_patch(request, pkg_name, f_name):
    return download_file(
            request,
            'media/patch/%s/%s' % (pkg_name, f_name)
    )