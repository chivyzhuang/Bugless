from django.conf.urls import patterns, url
from django.contrib.auth.views import login
from views import process_logout, process_login, register, add_app, remove_app_user
from views import ProfileWelcomeVive, AppEditView, ManageAppVive


urlpatterns = patterns('',
	# login
    url(r'^login/$', login, name='login'), 
    url(r'^nlogin/$', process_login, name='nlogin'), 
    # logout 
    url(r'^logout/$', process_logout, name='logout'),
    # regist
    url(r'^register/$', register, name='register'),
    # prifile
    url(r'^profile/$', ProfileWelcomeVive.as_view(), name='profile_welcome'),
    url(r'^profile/add_app/$', add_app, name='add_app'),
    url(r'^profile/edit_app/list/$', ManageAppVive.as_view(), name='app_list'),
    url(r'^profile/edit_app/panel/(?P<pkg_name>.+)/$', AppEditView.as_view(), name='edit_app'),
    url(r'^profile/edit_app/remove/(?P<pkg_name>.+)/(?P<user_name>.+)/$', remove_app_user, name='remove_app_user'),
)
