from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class passcode(Page):
    form_model = 'player'
    form_fields = ['passcode_2']

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if values[f] !=self.session.config['passcode_second']]
        if errors:
            return 'Your password is incorrect'


class Survey1(Page):
    form_model = 'player'
    form_fields = ['coffee_howoften', 'coffee_where', 'coffee_where_string',
                   'door_unlocked', 'lend_money', 'lend_personal', 'lie_parents', 'lie_roommates',
                   'lie_acquaintances', 'lie_friends', 'lie_partner']

    def is_displayed(self):
        # self.group.get_value2()
        return self.player.participant.vars['consent'].lower() == 'consent'
        # return True

    def error_message(self, values):
        errors = [1 for f in values if 'string' not in f and not values[f]]
        if errors:
            return 'you should select your answer'


class Survey2(Page):
    form_model = 'player'
    form_fields = ['take_advantage', 'try_to_be_helpful', 'trust',
                   'count_on_strangers', 'deal_with_strangers', 'recycle',
                   'more_pay_fair_trade', 'frequency_not_buy', 'car', 'frequency_shoes']

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent'
        # return True

    def error_message(self, values):
        errors = [1 for f in values if 'string' not in f and not values[f]]
        if errors:
            return 'you should select your answer'

class Survey3(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'gender_string','race','race_string',
                   'edu','major','major_string','parents','employment', 'employment_string',
                   'income','marital','children',
                   ]

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent'
        # return True

    def error_message(self, values):
        errors = [1 for f in values if 'string' not in f and not values[f]]
        if errors:
            return 'you should select your answer'



class Survey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'coffee']

    def is_displayed(self):

        return self.player.participant.vars['consent'].lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Final(Page):
    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent'

    def vars_for_template(self):


        return {
            'id': self.player.id_in_group,
            'payoff_trust': self.participant.vars['payoff_trust'],
            'payoff_cem': self.participant.vars['payoff_cem'],
            'payoff_all': self.participant.payoff_plus_participation_fee(),
            'total_bonus_coffee': self.participant.vars['total_bonus_coffee'],

        }



page_sequence = [Survey1, Survey2, Survey3, Final]


