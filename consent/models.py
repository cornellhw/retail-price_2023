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

    name_in_url = 'consent'
    players_per_group = 2
    num_rounds = 1
    passcode_correct = ''

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    consent = models.StringField(initial='')
    passcode_new = models.StringField(label="Please enter the password to start the experiment:",blank=True)


