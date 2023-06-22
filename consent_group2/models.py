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
    name_in_url = 'consent_group2'
    players_per_group = 2
    num_rounds = 1
    passcode_first = ''


class Subsession(BaseSubsession):
    def creating_session(self):
        pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    consent = models.StringField(initial='')
    passcode_1 = models.StringField(label="Please enter the password to start the experiment:", blank=True)

    def set_consent(self):
        if self.consent.lower() != 'consent':
            self.participant.vars['consent'] = 'Do not consent'

        else:
            self.participant.vars['consent'] = 'Consent'
