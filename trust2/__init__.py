import numpy as np
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'trust2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    INSTRUCTIONS_TEMPLATE = 'trust2/Instructions.html'
    ENDOWMENT = cu(100)
    MULTIPLIER = 3

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sent_amount = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        doc="""Amount sent by P1""",
        label="Please enter an amount from 0 to 100:",
    )
    sent_back_amount = models.CurrencyField(doc="""Amount sent back by P2""", min=cu(0))

    def currency_to_points(self, value):
        value_float = float(value)

        if value_float == 1:
            return f'{int(value_float)} point'
        elif value_float.is_integer():
            return f'{int(value_float)} points'
        else:
            return f'{value_float:.2f} points'


def set_payoffs(player: Player):
    generated_amount = np.random.normal(loc=player.sent_amount, scale=25)
    bounded_amount = min(max(0, generated_amount), player.sent_amount * C.MULTIPLIER)
    player.sent_back_amount = bounded_amount
    player.payoff = C.ENDOWMENT - player.sent_amount + player.sent_back_amount
    player.participant.vars['payoff_trust'] = player.payoff * 0.02


class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars['consent'].lower() == 'consent'


class Send(Page):
    form_model = 'player'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars['consent'].lower() == 'consent'


class Results(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars['consent'].lower() == 'consent'

    @staticmethod
    def vars_for_template(player: Player):
        set_payoffs(player)

        sent_amount_points = player.currency_to_points(player.sent_amount)
        sent_back_amount_points = player.currency_to_points(player.sent_back_amount)
        endowment_points = player.currency_to_points(C.ENDOWMENT)
        payoff_points = player.currency_to_points(player.payoff)

        return dict(
            sent_amount_points=sent_amount_points,
            sent_back_amount_points=sent_back_amount_points,
            endowment_points=endowment_points,
            payoff_points=payoff_points,
        )




page_sequence = [
    Introduction,
    Send,
    Results,
]
