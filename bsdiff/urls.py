from django.conf.urls import patterns, url
from bsdiff import views


urlpatterns = patterns('',
    url(r'^download/$', views.get_patch, name='get_patch'),
    url(r'^upload/$', views.upload_file, name='upload_file'),
    url(r'^upload/success/$', views.upload_success, name='upload_success'),
)
