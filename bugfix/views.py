from django.shortcuts import render_to_response
from django.template import RequestContext
from bugreceiver.models import JavaBug
from django.views import generic

# Create your views here.
class JavaBugList(generic.ListView):
    template_name = 'bugfix/javabug_list.html'
    context_object_name = 'bug_list'

    def get_context_data(self, **kwargs):
        context = super(JavaBugList, self).get_context_data(**kwargs)
        context['index'] = 'bug'
        return context

    def get_queryset(self):
        return JavaBug.objects.all()


class JavaBugDetail(generic.DetailView):
	template_name = 'bugfix/javabug_detail.html'
	model = JavaBug
	context_object_name = 'java_bug'

	def get_context_data(self, **kwargs):
		context = super(JavaBugDetail, self).get_context_data(**kwargs)
		context['index'] = 'bug'
		return context
		