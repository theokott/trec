from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'treceval.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^trec_eval_app/', include('trec_eval_app.urls')),     #Takes urls starting with /trec_eval_app/..., strips /trec_eval_app/ and passes the rest to trec_eval_app.urls be matched
    url(r'^$', include('trec_eval_app.urls'))
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static', (r'^media/(?P<path>.*)', 'serve',
                            {'document_root': settings.MEDIA_ROOT}), )
