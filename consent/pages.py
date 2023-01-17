from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def error_message(self, values):
        self.player.participant.vars['consent'] = values['consent']
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'
    # def error_message(self, values):
    #     # errors = [1 for f in values if not values[f]]
    #     print(values)
    #     self.player.participant.vars['consent'] = values['consent']
    #     # self.player.participant['consent'] = values['consent']
    #     if values['consent'].lower() != 'consent':
    #         return 'Please press consent to begin the experiment.'
    #


page_sequence = []


page_sequence += [Consent, ]
