from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from bugreceiver.models import JavaBug, NativeBug
from django.views import generic


class JavaBugList(generic.ListView):
    template_name = 'bugfix/javabug_list.html'
    context_object_name = 'bug_list'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(JavaBugList, self).dispatch(*args, **kwargs)

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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(JavaBugDetail, self).dispatch(*args, **kwargs)
	# def get_context_data(self, **kwargs):
	# 	context = super(JavaBugDetail, self).get_context_data(**kwargs)
	# 	context['index'] = 'bug'
	# 	return context


class NativeBugList(generic.ListView):
    template_name = 'bugfix/nativebug_list.html'
    context_object_name = 'bug_list'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NativeBugList, self).dispatch(*args, **kwargs)

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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NativeBugDetail, self).dispatch(*args, **kwargs)