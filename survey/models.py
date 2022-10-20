from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)
import random

doc = """
Simple survey
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = 32
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # survey
    age = models.IntegerField(label="What is your age?", min=5, max=125)

    gender = models.StringField(
        choices=[['0', 'male'], ['1', 'female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    coffee = models.StringField(
        choices=[['0', 'Never'], ['1', 'Once a week'], ['2', 'Two or three times a week'],
                 ['3', 'Everyday']],
        label='How often do you drink the coffee?',
        widget=widgets.RadioSelect,
        # initial='0'
    )


