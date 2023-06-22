from otree.api import *
import numpy as np

doc = """
This is a trust game with a twist: only one player is playing, and the amount sent back is determined by a random process. The sent back amount is generated from a normal distribution with a mean equal to the amount sent and a standard deviation of 25. If the generated amount falls below 0 or above the tripled sent amount, it is set to 0 or the tripled sent amount, respectively.
"""

class C(BaseConstants):
    NAME_IN_URL = 'trust'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    INSTRUCTIONS_TEMPLATE = 'trust/Instructions.html'
    ENDOWMENT = cu(100)
    MULTIPLIER = 3

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        doc="Amount sent by Player",
        label="Please enter an amount from 0 to 100:",
    )
    sent_back_amount = models.CurrencyField(doc="Amount sent back by system", min=cu(0))

class Player(BasePlayer):
    pass

def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    # Generate a normally distributed random number for sent_back_amount, ensuring it's not less than 0 and does not exceed the tripled sent amount
    generated_amount = np.random.normal(loc=group.sent_amount, scale=25)
    bounded_amount = min(max(0, generated_amount), group.sent_amount * C.MULTIPLIER)
    group.sent_back_amount = cu(bounded_amount)
    p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount

class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars['consent'].lower() == 'consent'

class Send(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1 and player.participant.vars['consent'].lower() == 'consent'

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars['consent'].lower() == 'consent'

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)

    @staticmethod
    def is_displayed(player: Player):
        player.participant.vars['payoff_trust'] = player.payoff*0.02
        return player.participant.vars['consent'].lower() == 'consent'

page_sequence = [
    Introduction,
    Send,
    ResultsWaitPage,
    Results,
]
