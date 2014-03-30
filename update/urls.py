from django.conf.urls import patterns, url
from update import views


urlpatterns = patterns('',
    # ask update
    url(r'^ask/$', views.ask_update, name='ask_update'),
)
