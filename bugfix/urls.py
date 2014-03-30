from django.conf.urls import patterns, url
from bugfix import views


urlpatterns = patterns('',
    url(r'^java_list/$', views.JavaBugList.as_view(), name='list_java_bug'),
    url(r'^java_bug/(?P<pk>\d+)/$', views.JavaBugDetail.as_view(), name='java_bug_detail'),
)
