from django.conf.urls import patterns, url
from bsdiff import views


urlpatterns = patterns('',
    url(r'^upload/$', views.upload_file, name='upload_file'),
    url(r'^upload/success/$', views.upload_success, name='upload_success'),
    url(r'^upload/fail/$', views.upload_fail, name='upload_fail'),
    # detail of apks
    url(r'^detail/apk/$', views.ApkDetail.as_view(), name='detail_apk'),
    # detail of patchs
    url(r'^detail/patch/$', views.PatchDetail.as_view(), name='detail_patch'),
)
