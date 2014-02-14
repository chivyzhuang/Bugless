from django.conf.urls import patterns, url
from bugreceiver import views

urlpatterns = patterns('',
    # receive bug report
    url(r'^test/$', views.test, name='test'),
    url(r'^report/tag/$', views.receive_bug, name='bug_receiver'),
)
