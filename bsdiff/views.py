# -*e coding: utf-8 -*-
import string
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views import generic
from bsdiff.models import ApkPackage, Patch
from bsdiff.forms import UploadFileForm
from bsdiff.operation import handle_uploaded_apk_file, check_if_apk_valid
from django.utils.decorators import method_decorator


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # check if valid
            is_valid, reason = check_if_apk_valid(
                request.POST['pkgname'],
                string.atoi(request.POST['version'])
                )
            if not is_valid:
                return render_to_response(
                        'bsdiff/upload_fail.html',
                        {'reason': reason},
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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ApkDetail, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        list = []
        for apkmark in self.request.user.apkmark_set.all():
            list += apkmark.apkpackage_set.all()
        return list


class PatchDetail(generic.ListView):
    template_name = 'bsdiff/patchdetail.html'
    context_object_name = 'patch_list'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PatchDetail, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        list = []
        for apkmark in self.request.user.apkmark_set.all():
            for apk in apkmark.apkpackage_set.all():
                list += apk.patch_set.all()
        return list


def upload_success(request):
    return HttpResponse("Upload success.")


def upload_fail(request, reason):
    return HttpResponse('Upload failed, because:\n' + reason)