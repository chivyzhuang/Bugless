from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView


class HomeView(TemplateView):
    def get(self, request):
        return render_to_response(
            'home.html',
            {'index': 'summary'},
            context_instance = RequestContext(request)
        )