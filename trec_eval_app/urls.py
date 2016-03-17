from django.conf.urls import patterns, url, include
from trec_eval_app import views


#Takes the stripped URLs passed to it and tries to match what remains
#If a URL is matched, the given view is called and thus a HTML response is generated

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'scoreboard$', views.scoreboard, name='scoreboard'),
        url(r'login$', views.login, name='scoreboard'),
        url(r'register/$', views.register, name='register'),
        )