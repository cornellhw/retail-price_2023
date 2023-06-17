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
            return 'You should select your answer'

class Passcode(Page):
    form_model = 'player'
    form_fields = ['passcode_1']

    def is_displayed(self):
        return self.player.participant.vars.get('consent', '').lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if values[f] != self.session.config['passcode_first']]
        if errors:
            return 'Your password is incorrect'

class ConsentWaitPage(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1 and player.participant.vars.get('consent', '').lower() == 'consent'

page_sequence = [Consent, Passcode, ConsentWaitPage]



