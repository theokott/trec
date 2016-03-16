from django.conf.urls import patterns, url, include
from trec_eval_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'scoreboard$', views.scoreboard, name='scoreboard'),
        url(r'login$', views.login, name='scoreboard')
        )