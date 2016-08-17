from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import authenticate, login, logout

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'monitor.views.index', name='home'),
#    url(r'^editor/$', 'monitor.views.editor', name='editor'),
#    url(r'^monitor/$', 'monitor.views.monitor', name='monitor'),
    # url(r'^blog/', include('blog.urls')),
#    url('', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls))
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()