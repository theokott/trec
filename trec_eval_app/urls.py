from django.conf.urls import patterns, url
from trec_eval_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))