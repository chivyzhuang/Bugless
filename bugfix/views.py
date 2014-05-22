# -*e coding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from bugreceiver.models import JavaBug, NativeBug
from bugfix.forms import RepairUploadForam
from bugfix.operation import handle_uploaded_java_repair_file, handle_uploaded_native_repair_file
from bugfix.operation import handle_remove_java_repair, handle_remove_native_repair
from bugfix.operation import handle_remove_java_publish, handle_remove_native_publish
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


@login_required
def java_repair_remove(request, pk):
    handle_remove_java_repair(pk)
    return HttpResponseRedirect(reverse('bugfix:java_bug_detail', args=(pk,)))


@login_required
def native_repair_remove(request, pk):
    handle_remove_native_repair(pk)
    return HttpResponseRedirect(reverse('bugfix:native_bug_detail', args=(pk,)))


@login_required
def java_repair_publish(request, pk):
    handle_remove_java_publish(pk)
    return HttpResponseRedirect(reverse('bugfix:java_bug_detail', args=(pk,)))


@login_required
def native_repair_publish(request, pk):
    handle_remove_native_publish(pk)
    return HttpResponseRedirect(reverse('bugfix:native_bug_detail', args=(pk,)))


@login_required
def java_repair_upload(request, pk):
    if request.method == 'POST':
        form = RepairUploadForam(request.POST, request.FILES)
        if form.is_valid():
            if request.POST['options'] == 'update':
                method = 'U'
            elif request.POST['options'] == 'repair':
                method = 'P'
            else:
                return render_to_response(
                    'bugfix/repair_upload.html',
                    {'form': form},
                    context_instance=RequestContext(request)
                    )
            error = handle_uploaded_java_repair_file(
                request.FILES['file'],
                pk,
                method,
                request.POST['brief']
                )
            if error != None:
                return render_to_response(
                    'bugfix/repair_upload.html',
                    {'form': form, 'error': error},
                    context_instance=RequestContext(request)
                    )
            else:
                return render_to_response(
                    'upload_success.html',
                    {'title': '上传修复方案成功', 'url': reverse("bugfix:java_bug_detail", args=[pk])},
                    context_instance=RequestContext(request)
                    )
    else:
        form = RepairUploadForam()
    return render_to_response(
            'bugfix/repair_upload.html',
            {'form': form},
            context_instance=RequestContext(request)
            )


class JavaBugList(generic.ListView):
    template_name = 'bugfix/javabug_list.html'
    context_object_name = 'bug_list'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(JavaBugList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return JavaBug.objects.all()


@login_required
def java_native_upload(request, pk):
    if request.method == 'POST':
        form = RepairUploadForam(request.POST, request.FILES)
        if form.is_valid():
            if request.POST['options'] == 'update':
                method = 'U'
            elif request.POST['options'] == 'repair':
                method = 'P'
            else:
                return render_to_response(
                    'bugfix/repair_upload.html',
                    {'form': form},
                    context_instance=RequestContext(request)
                    )
            error = handle_uploaded_native_repair_file(
                request.FILES['file'],
                pk,
                method,
                request.POST['brief']
                )
            if error != None:
                return render_to_response(
                    'bugfix/repair_upload.html',
                    {'form': form, 'error': error},
                    context_instance=RequestContext(request)
                    )
            else:
                return render_to_response(
                    'upload_success.html',
                    {'title': '上传修复方案成功', 'url': reverse("bugfix:native_bug_detail", args=[pk])},
                    context_instance=RequestContext(request)
                    )
    else:
        form = RepairUploadForam()
    return render_to_response(
            'bugfix/repair_upload.html',
            {'form': form},
            context_instance=RequestContext(request)
            )


class JavaBugDetail(generic.DetailView):
    template_name = 'bugfix/javabug_detail.html'
    model = JavaBug
    context_object_name = 'java_bug'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(JavaBugDetail, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(JavaBugDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', -1)
        if pk != -1:
            context['pk'] = pk
        return context


class NativeBugList(generic.ListView):
    template_name = 'bugfix/nativebug_list.html'
    context_object_name = 'bug_list'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NativeBugList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return NativeBug.objects.all()


class NativeBugDetail(generic.DetailView):
    template_name = 'bugfix/nativebug_detail.html'
    model = NativeBug
    context_object_name = 'native_bug'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NativeBugDetail, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(NativeBugDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', -1)
        if pk != -1:
            context['pk'] = pk
        return context