from django.conf.urls import patterns, url


urlpatterns = patterns('b11_players.views',
    url(r'^$', 'player_overview', name='u_player_overview'),
    url(r'^(?P<player_id>\d+)/$', 'player_details', name='u_player_details'),
    url(r'^new/$', 'player_new', name='u_player_new'),
    
)

