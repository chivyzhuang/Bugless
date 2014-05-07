from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import HomeView
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^usermanager/', include('usermanager.urls', namespace='usermanager')),
    url(r'^download/', include('download.urls', namespace='download')),
    url(r'^bugreceiver/', include('bugreceiver.urls', namespace='bug_receiver')),
    url(r'^bsdiff/', include('bsdiff.urls', namespace='bsdiff')),
    url(r'^bugfix/', include('bugfix.urls', namespace='bugfix')),
    url(r'^update/', include('update.urls', namespace='update')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^2048$', TemplateView.as_view(template_name="2048.html"), name='2048'),
    url(r'^admin/', include(admin.site.urls)),
)
