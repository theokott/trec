from django.conf.urls import patterns, url, include
from trec_eval_app import views

# Takes the stripped URLs passed to it and tries to match what remains
# If a URL is matched, the given view is called and thus a HTML response is generated

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'scoreboard/$', views.scoreboard, name='scoreboard'),
                       url(r'login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'register/$', views.register, name='register'),
                       url(r'upload/$', views.upload, name='upload'),
                       url(r'user/$', views.user_profile, name='user'),
                       url(r'user/edit-profile/$', views.user_edit, name='edit_profile'),
                       url(r'user/edit-password', views.user_edit_password, name='edit_password'),
                       url(r'^scoreboard/(?P<track_slug>[\w\-]+)/$', views.scoreboard, name='scoreboard'),
                       )
