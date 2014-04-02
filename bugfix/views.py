from django.shortcuts import render_to_response
from django.template import RequestContext
from bugreceiver.models import JavaBug, NativeBug
from django.views import generic


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

	# def get_context_data(self, **kwargs):
	# 	context = super(JavaBugDetail, self).get_context_data(**kwargs)
	# 	context['index'] = 'bug'
	# 	return context


class NativeBugList(generic.ListView):
    template_name = 'bugfix/nativebug_list.html'
    context_object_name = 'bug_list'

    def get_context_data(self, **kwargs):
        context = super(NativeBugList, self).get_context_data(**kwargs)
        context['index'] = 'bug'
        return context

    def get_queryset(self):
        return NativeBug.objects.all()


class NativeBugDetail(generic.DetailView):
	template_name = 'bugfix/nativebug_detail.html'
	model = NativeBug
	context_object_name = 'native_bug'

	# def get_context_data(self, **kwargs):
	# 	context = super(NativeBugDetail, self).get_context_data(**kwargs)
	# 	context['index'] = 'bug'
	# 	return context