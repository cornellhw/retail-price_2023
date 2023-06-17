from otree.api import models, BaseConstants, BasePlayer, BaseGroup, BaseSubsession

class Constants(BaseConstants):
    name_in_url = 'RandomGrouping'
    players_per_group = 2
    num_rounds = 1

class Player(BasePlayer):
    pass

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)
        for player in self.get_players():
            player.participant.vars['group_id'] = player.group.id_in_subsession
            player.participant.vars['id_in_group'] = player.id_in_group
