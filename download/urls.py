from django.conf.urls import patterns, url
from download import views


urlpatterns = patterns('',
    # download apk file
    url(r'^apk/(?P<pkg_name>.+)/(?P<f_name>.+)/$', views.get_apk, name='get_apk'),
    # download patch file
    url(r'^patch/(?P<pkg_name>.+)/(?P<f_name>.+)/$', views.get_patch, name='get_patch'),
    #
    url(r'^path/(?P<file_path>.+)/$', views.get_file, name='get_file'),
)
