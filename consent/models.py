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


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    consent = models.StringField(initial='')