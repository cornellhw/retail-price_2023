from scipy import stats
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)

import random
import math

doc = """
Simple coffee experiment
"""
class Constants(BaseConstants):

    name_in_url = 'consent_group'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    def init_setting(self):
        consent = True
        for p in self.get_players():
            print(p.participant.vars)
            if p.participant.vars['consent'].lower() != 'consent':
                consent= False
        if consent:
            consent_group = 'Consent'
        else:
            consent_group = 'Do not consent'
        for p in self.get_players():
            p.participant.vars['consent'] = consent_group
            print(p.participant.vars['consent'] )
        return

class Player(BasePlayer):

    consent = models.StringField(initial='')