from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# Examples:
# url(r'^$', 'treceval.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^trec_eval_app/', include('trec_eval_app.urls')),
                       url(r'^$', include('trec_eval_app.urls'))
                       )
# Takes urls starting with /trec_eval_app/..., strips /trec_eval_app/
# and passes the rest to trec_eval_app.urls be matched

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT}))
