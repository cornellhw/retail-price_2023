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

class Waiting0(WaitPage):
    def is_displayed(self):
        return self.player.participant.vars.get('consent', '').lower() == 'consent'


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def before_next_page(self):
        self.player.set_consent()

class Waiting0(WaitPage):
    pass

class Passcode(Page):
    form_model = 'player'
    form_fields = ['passcode_1']

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent'


class Final_not(Page):
    def is_displayed(self):
        return self.player.participant.vars.get('consent', '') == 'Do not consent'

page_sequence = [Consent, Waiting0, Passcode, Final_not]