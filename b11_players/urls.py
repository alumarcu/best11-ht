from django.conf.urls import patterns, url
from b11_players import views

urlpatterns = patterns('b11_players.views',

    #url(r'^$', 'player_overview', name='u_player_overview'),
    
    url(r'^new/$', 'player_new', name='u_player_new'),
    
)
urlpatterns+= patterns('',
    url(r'^$', views.PlayerView.as_view(), name='u_player_overview'),
    url(r'^(?P<pk>\d+)/$', views.PlayerDetail.as_view(), name='u_player_details'),
)
