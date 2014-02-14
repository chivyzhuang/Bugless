from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponse
from django.views import generic
from bsdiff.models import *
from bsdiff.forms import UploadFileForm
from bsdiff.upload import handle_uploaded_apk_file
from bsdiff.download import download_file


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_apk_file(
                    request.FILES['file'],
                    request.POST['pkgname'],
                    request.POST['version']
            )
            return HttpResponseRedirect(reverse('bsdiff:upload_success'))
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


def get_apk(request):
    l = request.path.split('/')
    if len(l) == 6:
        return download_file(
                request,
                'Storage/apk/%s' % l[4]
        )
    return HttpResponse('Error.')


def get_patch(request):
    l = request.path.split('/')
    if len(l) == 6:
        return download_file(
                request,
                'Storage/patch/%s' % l[4]
        )
    return HttpResponse('Error.')
