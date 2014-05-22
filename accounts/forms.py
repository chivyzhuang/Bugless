#!-*- coding=utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    '''注册表单'''
    username = forms.CharField(label=_(u"登录账号"))
    email=forms.EmailField(label=_(u"邮件地址"))

    password=forms.CharField(label=_(u"登录密码"))
    repassword=forms.CharField(label=_(u"重复登录密码"))

    def clean_username(self):
        '''验证昵称'''
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(_(u"该昵称已经被使用"));

    def clean_repassword(self):
        '''验证两次输入密码'''
        password = self.cleaned_data["password"]
        repassword = self.cleaned_data["repassword"]
        if password and repassword and password != repassword:
            raise forms.ValidationError(_(u"两次密码输入不一致"));
        return repassword;

    def clean_email(self):
        '''验证email'''
        email = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not email:
            return self.cleaned_data["email"];
        raise forms.ValidationError(_(u"该邮箱已经被使用"));


class AppAddForm(forms.Form):
	pkgname = forms.CharField(label=_(u"应用包名"))


class ResetPasswordForm(forms.Form):
    oldpassword = forms.CharField(label=_(u"旧密码"))
    newpassword1 = forms.CharField(label=_(u"新密码"))
    newpassword2 = forms.CharField(label=_(u"确认新密码"))

    def clean_newpassword2(self):
        '''验证两次输入新密码'''
        newpassword1 = self.cleaned_data["newpassword1"]
        newpassword2 = self.cleaned_data["newpassword2"]
        if newpassword1 and newpassword2 and newpassword1 != newpassword2:
            raise forms.ValidationError(_(u"两次新密码输入不一致"));
        return newpassword2;

class AppUserAddForm(forms.Form):
    username = forms.CharField(label=_(u"用户名"))

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            return User._default_manager.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(_(u"该用户不存在"));