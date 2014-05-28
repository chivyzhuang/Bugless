from django.conf.urls import patterns, url
from bsdiff import views


urlpatterns = patterns('',
    url(r'^upload/$', views.upload_file, name='upload_file'),
    # detail of apks
    url(r'^detail/apk/$', views.ApkDetail.as_view(), name='detail_apk'),
    # detail of patchs
    url(r'^detail/patch/$', views.PatchDetail.as_view(), name='detail_patch'),
    #
    url(r'^publish/(?P<pk>\d+)/$', views.publish_apk, name='publish_apk'),
)
