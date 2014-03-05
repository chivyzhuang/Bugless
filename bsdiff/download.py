import os
from django.http import StreamingHttpResponse
from django.core.servers.basehttp import FileWrapper


def download_file(request, filepath):
    wrapper = FileWrapper(file(filepath))
    response = StreamingHttpResponse(wrapper)
    response['Content-Length'] = os.path.getsize(filepath)
    return response
