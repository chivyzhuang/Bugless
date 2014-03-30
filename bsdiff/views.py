# -*e coding: utf-8 -*-
import string
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponse
from django.views import generic
from bsdiff.models import ApkPackage, Patch
from bsdiff.forms import UploadFileForm
from bsdiff.operation import handle_uploaded_apk_file, check_if_apk_expired
from django.views.decorators.csrf import csrf_exempt


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # check if expired
            if check_if_apk_expired(
                    request.POST['pkgname'],
                    string.atoi(request.POST['version'])
                    ):
                return render_to_response(
                        'bsdiff/upload_fail.html',
                        {'reason': 'Apk的版本号必须大于或等于最新的Apk'},
                        context_instance=RequestContext(request)
                        )
            handle_uploaded_apk_file(
                    request.FILES['file'],
                    request.POST['pkgname'],
                    string.atoi(request.POST['version'])
            )
            return render_to_response(
                    'bsdiff/upload_success.html',
                    context_instance=RequestContext(request)
                    )
    else:
        form = UploadFileForm()
    return render_to_response(
            'bsdiff/upload.html',
            {'form': form},
            context_instance=RequestContext(request)
            )


class ApkDetail(generic.ListView):
    template_name = 'bsdiff/apkdetail.html'
    context_object_name = 'apk_list'

    def get_queryset(self):
        return ApkPackage.objects.all()


class PatchDetail(generic.ListView):
    template_name = 'bsdiff/patchdetail.html'
    context_object_name = 'patch_list'

    def get_queryset(self):
        return Patch.objects.all()


def upload_success(request):
    return HttpResponse("Upload success.")


def upload_fail(request, reason):
    return HttpResponse('Upload failed, because:\n' + reason)