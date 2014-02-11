from django.db import models

# Register players in teams
class Team(models.Model):
    name = models.CharField(max_length=40)
    def __unicode__(self):
        return self.name


# Player skills
class GameSkill(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name
    
# Positions of Players
class GamePosition(models.Model):
    name = models.CharField(max_length=20)
    required_sk = models.ForeignKey(GameSkill)
    secondary_sk = models.ManyToManyField(GameSkill,related_name='extra_feats')
    
    def __unicode__(self):
        return self.name

# Player data
class Player(models.Model):
    name     = models.CharField(max_length=40)
    position = models.ForeignKey(GamePosition)
    form     = models.PositiveSmallIntegerField()
    stamina  = models.PositiveSmallIntegerField()
    team     = models.ForeignKey(Team)
    def __unicode__(self):
        return self.name


# Defines the skills owned by players
class PlayerSkill(models.Model):
    sk_ref = models.ForeignKey(GameSkill)
    sk_value = models.PositiveSmallIntegerField()
    owner = models.ForeignKey(Player)
    def __unicode__(self):
        return self.owner.name + ': '  + self.sk_ref.name + ' @ ' + str(self.sk_value)

    


