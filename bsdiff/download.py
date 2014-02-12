import os
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper


def download_file(request, filepath):
    wrapper = FileWrapper(file(filepath))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filepath)
    return response
