#!-*- coding=utf-8 -*-
from django.http import HttpResponseRedirect
from django.contrib.auth import logout 
from django.conf import settings
from django.template.response import TemplateResponse
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login)
from django.shortcuts import resolve_url
from django.utils.http import is_safe_url
from django.contrib.sites.models import get_current_site
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from forms import RegisterForm, AppAddForm, AppUserAddForm
from bsdiff.models import ApkMark, Management
from django.views import generic
from django.forms.util import ErrorList
from django.views.generic import TemplateView


class ManageAppVive(generic.ListView):
    template_name = 'accounts/profile_manage_app.html'
    context_object_name = 'management_list'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ManageAppVive, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        list = []
        for management in self.request.user.management_set.all():
            list.append(ManagementMarkItem(management.identity, management.mark))
        return list

    def get_context_data(self, **kwargs):
        context = super(ManageAppVive, self).get_context_data(**kwargs)
        context['sidebar_index'] = 'manage_app'
        return context


@login_required
def remove_app_user(request, pkg_name, user_name):
    try:
        apk_mark = ApkMark.objects.get(package_name=pkg_name)
        management = Management.objects.get(
            user=request.user,
            mark=apk_mark)
        if management.identity == 'O':
            user = User._default_manager.get(username=user_name)
            management = Management.objects.get(
                user=user,
                mark=apk_mark)
            management.delete()
    except Exception:
        pass
    return HttpResponseRedirect(reverse("accounts:edit_app", args = [pkg_name]))


class AppEditView(TemplateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppEditView, self).dispatch(*args, **kwargs)

    def get(self, request, pkg_name):
        apk_mark = ApkMark.objects.get(package_name=pkg_name)
        form = AppUserAddForm()
        user_list = Management.objects.filter(mark=apk_mark)
        return render_to_response(
            'accounts/profile_edit_app.html',
            {'sidebar_index': 'manage_app', 'form': form, 'apk_mark': apk_mark, 'user_list': user_list},
            context_instance = RequestContext(request)
        )

    def post(self, request, pkg_name):
        apk_mark = ApkMark.objects.get(package_name=pkg_name)
        if request.method == 'POST':
            form = AppUserAddForm(request.POST.copy())
            if form.is_valid():
                user = form.cleaned_data["username"]
                try:
                    management = Management.objects.get(
                        user=user,
                        mark=apk_mark)
                except Management.DoesNotExist:
                    management = Management(
                        mark=apk_mark, 
                        user=user,
                        identity='M')
                    management.save()
        else:
            form = AppUserAddForm()
        user_list = Management.objects.filter(mark=apk_mark)
        return render_to_response(
            'accounts/profile_edit_app.html',
            {'sidebar_index': 'manage_app', 'form': form, 'apk_mark': apk_mark, 'user_list': user_list},
            context_instance = RequestContext(request)
        )


@login_required
def add_app(request):
    if request.method == 'POST':
        form = AppAddForm(request.POST.copy())
        if form.is_valid():
            try:
                apkmark = ApkMark.objects.get(package_name=request.POST['pkgname'])
                error_msg = ["Add Repeatedly!"]
                form.errors['pkgname'] = ErrorList(error_msg)
            except ApkMark.DoesNotExist:
                appname = request.POST['appname']
                if appname == '':
                    appname = request.POST['pkgname']
                apkmark = ApkMark.objects.create(
                    package_name=request.POST['pkgname'],
                    app_name=appname,
                    brief=request.POST['brief'])
                management = Management(
                    mark=apkmark, 
                    user=request.user,
                    identity='O')
                management.save()
                return HttpResponseRedirect(reverse("accounts:profile_welcome"))
    else:
        form = AppAddForm()
    return render_to_response(
            'accounts/profile_add_app.html',
            {'form': form, 'sidebar_index': 'add_app'},
            context_instance=RequestContext(request)
            )


class ManagementMarkItem:
    mark = ''
    identity = ''

    def __init__(self, identity, mark):  
        self.identity = identity
        self.mark = mark


class ProfileWelcomeVive(generic.ListView):
    template_name = 'accounts/profile_welcome.html'
    context_object_name = 'management_list'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileWelcomeVive, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        list = []
        for management in self.request.user.management_set.all():
            list.append(ManagementMarkItem(management.identity, management.mark))
        return list

    def get_context_data(self, **kwargs):
        context = super(ProfileWelcomeVive, self).get_context_data(**kwargs)
        context['sidebar_index'] = 'overview'
        return context


@sensitive_post_parameters()
@csrf_protect
@never_cache
def process_login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


def process_logout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def register(request, template_name='registration/register.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=RegisterForm,
          current_app=None, extra_context=None):
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))
    if request.method=="POST":
        form = RegisterForm(request.POST.copy())
        if form.is_valid():
            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = reverse('accounts:login')

            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username, email, password)
            user.save()
            return HttpResponseRedirect(redirect_to);
    else:
        form = authentication_form()
    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)