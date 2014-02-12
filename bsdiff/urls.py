from django.conf.urls import patterns, url
from bsdiff import views


urlpatterns = patterns('',
    url(r'^upload/$', views.upload_file, name='upload_file'),
    url(r'^upload/success/$', views.upload_success, name='upload_success'),
    # download apk file
    url(r'^download/apk/.+/$', views.get_apk, name='get_apk'),
    # download patch file
    url(r'^download/patch/.+/$', views.get_patch, name='get_patch'),
)
