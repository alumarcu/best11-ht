from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from b11_players.models import Player, GamePosition,PlayerSkill,Team


# Create your views here.
def player_overview(request):

    players_list = Player.objects.order_by('position', 'team')
    positions = GamePosition.objects.all()

    
    for player in players_list:
        player.skills = PlayerSkill.objects.filter(owner=player.id)
        


    context = {
        'message': 'you passed alpha!',  
        'positions' : positions,
        'players_list': players_list,
    }
    return render(request, 'b11_players/players.html', context)
    
def player_details(request, player_id):
    return HttpResponse("Details for player %s are shown here." % player_id )
    
def player_new(request):
    if request.POST:
        p = {}
        if request.POST['name']:
            p['name'] = request.POST['name']
        if request.POST['form']:
            p['form'] = int(request.POST['form'])
        if request.POST['stamina']:
            p['stamina'] = int(request.POST['stamina'])
        gp = GamePosition.objects.all().last()
        tt = Team.objects.all().last()
        plr = Player(name=p['name'],position=gp,form=p['form'],stamina=p['stamina'],team=tt)
        plr.save()
        return HttpResponseRedirect(reverse('b11_players:u_player_overview'))

    context = {}
    return render(request, 'b11_players/newplayer.html', context)

