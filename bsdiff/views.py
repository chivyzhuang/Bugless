from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from bsdiff.forms import UploadFileForm
from bsdiff.upload import handle_uploaded_apk_file
from bsdiff.download import download_file
from django.http import HttpResponse


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


def upload_success(request):
    return HttpResponse("Upload success.")


def get_patch(request):
    return download_file(request, 'Storage/apk/1.apk')
