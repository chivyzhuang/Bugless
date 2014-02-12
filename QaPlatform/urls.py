from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'QaPlatform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^bugreceiver/', include('bugreceiver.urls', namespace='bug_receiver')),
    url(r'^bsdiff/', include('bsdiff.urls', namespace='bsdiff')),
    url(r'^admin/', include(admin.site.urls)),
)
