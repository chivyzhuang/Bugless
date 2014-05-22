from django.conf.urls import patterns, url
from bugfix import views


urlpatterns = patterns('',
    url(r'^java_list/$', views.JavaBugList.as_view(), name='list_java_bug'),
    url(r'^java_bug/(?P<pk>\d+)/$', views.JavaBugDetail.as_view(), name='java_bug_detail'),
    url(r'^repair/java/upload/(?P<pk>\d+)/$', views.java_repair_upload, name='java_bug_repair'),
    url(r'^repair/java/remove/(?P<pk>\d+)/$', views.java_repair_remove, name='java_bug_repair_remove'),
    url(r'^repair/java/publish/(?P<pk>\d+)/$', views.java_repair_publish, name='java_bug_repair_publish'),
    url(r'^native_list/$', views.NativeBugList.as_view(), name='list_native_bug'),
    url(r'^native_bug/(?P<pk>\d+)/$', views.NativeBugDetail.as_view(), name='native_bug_detail'),
    url(r'^repair/native/upload/(?P<pk>\d+)/$', views.java_native_upload, name='native_bug_repair'),
    url(r'^repair/native/remove/(?P<pk>\d+)/$', views.native_repair_remove, name='native_bug_repair_remove'),
    url(r'^repair/native/publish/(?P<pk>\d+)/$', views.native_repair_publish, name='native_bug_repair_publish'),
)
