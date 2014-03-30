from django.conf.urls import patterns, url
from bugreceiver import views

urlpatterns = patterns('',
    # receive bug report
    url(r'^test/$', views.test, name='test'),
    url(r'^report/tag/$', views.receive_bug_report),
    url(r'^report/detail/java/$', views.receive_java_bug_detail),
    url(r'^report/native/$', views.receive_native_bug),
)
