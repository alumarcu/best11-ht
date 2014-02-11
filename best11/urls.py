from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'best11.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^players/', include('b11_players.urls', namespace="b11_players")),
    url(r'^admin/', include(admin.site.urls)),
)
