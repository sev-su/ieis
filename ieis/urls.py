from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

handler404 = 'utils.views.return_404'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ieis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('frontpage.urls')),
)
