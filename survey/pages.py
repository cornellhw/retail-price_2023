from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Survey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'coffee']

class End2(Page):
    pass


page_sequence = [Survey,
                 End2,
                 ]