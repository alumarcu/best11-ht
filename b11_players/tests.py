import b11_players.models as mod
from django.test import TestCase

class PlayerClassTests(TestCase):
    def test_player_returned_main_skill_has_correct_format(self):
        _sk = mod.GameSkill(name='testing')
        _sk.save() # Create the new skill
        _gp = mod.GamePosition(name='Unit Tester',required_sk=_sk)
        _gp.save() # New game position
        _team = mod.Team(name='Test Team')
        _team.save() # New team
        # Create a new player
        _player = mod.Player(name='Random Tester', position=_gp, form=10, stamina=10, team=_team)
        # Is his default main skill what we expect it to be?
        mks = _player.get_main_skill()

        # -- test each condition one by one
        # self.assertEqual(isinstance(mks, tuple), True)
        # self.assertEqual(len(mks), 2)
        # self.assertEqual(mks[0], _player.position.required_sk.name)
        # self.assertEqual(mks[1], 0)
        
        # or compare directly with the expected tuple
        self.assertEqual(mks, (_player.position.required_sk.name, 0))


