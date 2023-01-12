from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def error_message(self, values):
        # errors = [1 for f in values if not values[f]]
        if self.player.consent != 'consent':
            return 'Please press consent to begin the experiment.'


page_sequence = []


page_sequence += [Consent]
