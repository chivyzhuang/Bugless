from django.conf.urls import patterns, url
from bugreceiver import views

urlpatterns = patterns('',
    # receive bug report
    url(r'^$', views.receive_bug, name='bug_receiver'),
)
