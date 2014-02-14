from django.conf.urls import patterns, url
from bsdiff import views


urlpatterns = patterns('',
    url(r'^upload/$', views.upload_file, name='upload_file'),
    url(r'^upload/success/$', views.upload_success, name='upload_success'),
    # detail of apks
    url(r'^detail/apk/$', views.ApkDetail.as_view(), name='detail_apk'),
    # detail of patchs
    url(r'^detail/patch/$', views.PatchDetail.as_view(), name='detail_patch'),
    # download apk file
    url(r'^download/apk/.+/$', views.get_apk, name='get_apk'),
    # download patch file
    url(r'^download/patch/.+/$', views.get_patch, name='get_patch'),
)
