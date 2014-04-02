from django.conf.urls import patterns, url
from bugfix import views


urlpatterns = patterns('',
    url(r'^java_list/$', views.JavaBugList.as_view(), name='list_java_bug'),
    url(r'^java_bug/(?P<pk>\d+)/$', views.JavaBugDetail.as_view(), name='java_bug_detail'),
    url(r'^native_list/$', views.NativeBugList.as_view(), name='list_native_bug'),
    url(r'^native_bug/(?P<pk>\d+)/$', views.NativeBugDetail.as_view(), name='native_bug_detail'),
)
