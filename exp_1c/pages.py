from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Welcome(Page):
    def vars_for_template(self):
        self.group.init_setting()

class Quality(Page):
    form_model = 'player'
    form_fields = ['choice', 'quality']

class Introduction(Page):
    pass

class SetPrice(Page):
    form_model = 'player'
    form_fields = ['W']

    def before_next_page(self):
        self.player.price_check()
        self.player.set_payoff1()


class PriceResults(Page):
    def vars_for_template(self):
        return {'payoff1': round(self.player.payoff1,2)}


class Introduction2(Page):
    def is_displayed(self):
        return self.player.purchase_success

class SetPrice2(Page):
    form_model = 'player'
    form_fields = ['R']

    def before_next_page(self):
        self.player.price_check2()
        self.player.set_payoff2()

    def is_displayed(self):
        return self.player.purchase_success


class PriceResults2(Page):
    def vars_for_template(self):
        return {'payoff2': round(self.player.payoff2,2)}

    def is_displayed(self):
        return self.player.purchase_success

class End(Page):
    pass


page_sequence = [Welcome,
                 Quality,
                 Introduction,
                 SetPrice,
                 PriceResults,
                 Introduction2,
                 SetPrice2,
                 PriceResults2,
                 End,
                 ]