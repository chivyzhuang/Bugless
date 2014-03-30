from django.conf.urls import patterns, url
from usermanager import views

urlpatterns = patterns('',
    url(r'^update/$', views.update, name='user_update'),
)
