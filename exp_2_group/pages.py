from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'

class Waiting0(WaitPage):
    pass

class Welcome(Page):
    def is_displayed(self):
        self.player.init_role()
        self.group.init_setting()

        return self.player.participant.vars['consent'].lower() == 'consent'


class Info(Page):
    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent'
    def before_next_page(self):
        self.player.tast()

class Summary(Page):
    def vars_for_template(self):
        if self.player.tasting_new == 0:
            next_is = 'based on your choice'
        else:
            next_is = 'based on your tasting and choice'
        return {'tasting_new': self.player.tasting_new,
                'next_is': next_is
                }
    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent'

class passcode(Page):
    form_model = 'player'
    form_fields = ['passcode_2']

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if values[f] !=self.session.config['passcode_second']]
        if errors:
            return 'Your password is incorrect'


class Role_Info(Page):

    def vars_for_template(self):
        ID_number = self.player.id_in_subsession
        if self.player.role_own == 'A':
            role = 'Procurement Manager'
        else:
            role = 'Marketing Manager'
        if int(ID_number) % 2 == 1:
            ID_match = ID_number + 1
        else:
            ID_match = ID_number - 1
        return {'role':role,
                'ID_number':ID_number,
                'ID_match':ID_match}

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent'
        # return True


class Survey_coffee1(Page):
    form_model = 'player'
    form_fields = ['coffee_like']

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent' and self.player.role_own == 'A'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'

class Survey_coffee2(Page):
    form_model = 'player'
    form_fields = ['coffee_quality']

    def vars_for_template(self):
        if self.player.tasting_new == 0:
            next_is = 'you selected based on the information provided'
        else:
            next_is = 'you selected based on your tasting'
        return {'tasting_new': self.player.tasting_new,
                'next_is': next_is
                }
    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent' and self.player.role_own == 'A'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee3(Page):
    form_model = 'player'
    form_fields = ['coffee_sweetness']

    def vars_for_template(self):
        if self.player.tasting_new == 0:
            next_is = 'you selected based on the information provided'
        else:
            next_is = 'you selected based on your tasting'
        return {'tasting_new': self.player.tasting_new,
                'next_is': next_is
                }

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent' and self.player.role_own == 'A'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee4(Page):
    form_model = 'player'
    form_fields = ['coffee_flavor']

    def vars_for_template(self):
        if self.player.tasting_new == 0:
            next_is = 'you selected based on the information provided'
        else:
            next_is = 'you selected based on your tasting'
        return {'tasting_new': self.player.tasting_new,
                'next_is': next_is
                }
    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent' and self.player.role_own == 'A'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee5(Page):
    form_model = 'player'
    form_fields = ['coffee_impression']

    def vars_for_template(self):
        if self.player.tasting_new == 0:
            next_is = 'conveyed in the information provided'
        else:
            next_is = 'of its combined taste'
        return {'tasting_new': self.player.tasting_new,
                'next_is': next_is
                }

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent' and self.player.role_own == 'A'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee6(Page):
    form_model = 'player'
    form_fields = ['coffee_recom']

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent' and self.player.role_own == 'A'
        # return True

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee7(Page):
    form_model = 'player'
    form_fields = ['coffee_drink']

    def vars_for_template(self):
        if self.player.tasting_new == 0:
            next_is = 'Drink this coffee'
        else:
            next_is = 'Drink this coffee again'
        return {'tasting_new': self.player.tasting_new,
                'next_is': next_is
                }

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent' and self.player.role_own == 'A'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee8(Page):
    form_model = 'player'
    form_fields = ['coffee_serve']

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent' and self.player.role_own == 'A'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee9(Page):
    form_model = 'player'
    form_fields = ['coffee_buy']

    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent' and self.player.role_own == 'A'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Payment(Page):
    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent' and self.player.role_own == 'A'


class Payment2(Page):
    def is_displayed(self):
        return self.player.participant.vars['consent'].lower() == 'consent' and self.player.role_own == 'A'


class SetPrice(Page):
    form_model = 'player'
    form_fields = ['W', 'lockin']

    def is_displayed(self):
        if self.player.role_own == 'B':
            return False
        if self.player.participant.vars['consent'].lower() != 'consent':
            return False
        if self.player.lockin.lower() != 'lockin':
            return True
        else:
            return False

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'

    def before_next_page(self):
        self.player.set_payoff1()

    def vars_for_template(self):
        if self.player.test_times == 0:
            prob = 'XXX'
            optimal_cost_bonus= 'XXX'
            optimal_profit_bonus = 'XXX'
            optimal_total_bonus = 'XXX'
            optimal_earn = 'XXX'

        else:
            prob = self.player.prob*100
            optimal_cost_bonus = self.player.optimal_cost_bonus
            optimal_profit_bonus = self.player.optimal_profit_bonus
            optimal_total_bonus = self.player.optimal_total_bonus
            optimal_earn = self.player.optimal_earn
        return {'prob': prob if isinstance(prob, float) else prob[0],
                'optimal_cost_bonus' : optimal_cost_bonus,
                'optimal_profit_bonus': optimal_profit_bonus,
                'optimal_total_bonus': optimal_total_bonus,
                'optimal_earn': optimal_earn,
                'round': ['first', 'second', 'third'][self.player.test_round],
                'round_n': ['1st', '2nd', '3rd'][self.player.test_round],
                }

class Res1(Page):
    def vars_for_template(self):
        if self.player.is_reject == 'rejected' and self.player.test_round<3:
            next_info = 'Click the "Next" button to make the supplier another offer!'
        else:
            next_info = 'Click the "Next" button to continue with the experiment!'
        return {'is_reject': self.player.is_reject,
                'cost_bonus': self.player.cost_bonus,
                'next_info': next_info
                }

    def is_displayed(self):
        if self.player.role_own == 'B':
            return False
        # self.player.set_payoff1()
        return self.player.participant.vars['consent'].lower() == 'consent' or self.player.is_reject=='reject'

    def before_next_page(self):
        self.player.show_res1 = 0
        self.player.test_round += 1
        self.player.logger_W += '| '
        self.player.logger_T += str(self.player.test_times)+','
        self.player.test_times = 0

        if self.player.is_reject == 'rejected' and self.player.test_round<3:
            self.player.lockin = '-1'

class Res12(Page):
    def vars_for_template(self):
        if self.player.is_reject == 'rejected' and self.player.test_round<3:
            next_info = 'Click the "Next" button to make the supplier another offer!'
        else:
            next_info = 'Click the "Next" button to continue with the experiment! '
        return {'is_reject': self.player.is_reject,
                'cost_bonus': self.player.cost_bonus,
                'next_info': next_info
                }

    def is_displayed(self):
        if self.player.role_own == 'B':
            return False
        # self.player.set_payoff1()

        return (self.player.participant.vars['consent'].lower() == 'consent' or self.player.is_reject == 'reject') and self.player.show_res2

    def before_next_page(self):
        self.player.test_round += 1
        self.player.logger_W += '| '
        self.player.logger_T += str(self.player.test_times)+','
        self.player.test_times = 0

        if self.player.is_reject == 'rejected' and self.player.test_round<3:
            self.player.lockin = '-1'


class Res123(Page):
    def vars_for_template(self):
        if self.player.is_reject == 'rejected' and self.player.test_round<3:
            next_info = 'Click the "Next" button to finish the post-experimental survey!'
        else:
            next_info = 'Click the "Next" button to continue with the experiment! '
        return {'is_reject': self.player.is_reject,
                'cost_bonus': self.player.cost_bonus,
                'next_info': next_info
                }

    def is_displayed(self):
        if self.player.role_own == 'B':
            return False

        return (self.player.participant.vars['consent'].lower() == 'consent' or self.player.is_reject=='reject') and self.player.show_res3

    def before_next_page(self):
        self.player.test_round += 1
        self.player.logger_W += '| '
        self.player.logger_T += str(self.player.test_times)+','
        self.player.test_times = 0

        if self.player.is_reject == 'rejected' and self.player.test_round<3:
            self.player.lockin = '-1'

class Waiting1(WaitPage):
    body_text = "You are waiting for the results for procurement price setting from the Procurement Manager."
    after_all_players_arrive = 'get_value'


class Res_market(Page):
    def vars_for_template(self):
        return {'is_reject': self.player.is_reject,
                }
    def is_displayed(self):
        if self.player.role_own == 'A':
            return False
        return self.player.participant.vars['consent'].lower() == 'consent'

class SetPrice2(Page):
    form_model = 'player'
    form_fields = ['R', 'lockin2']

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'

    def is_displayed(self):
        if self.player.role_own == 'A':
            return False

        if self.player.participant.vars['consent'].lower() != 'consent':
            return False
        if self.player.is_reject == 'accepted':
            if self.player.lockin2.lower() != 'lockin':
                return True
            else:
                return False
        else:
            return False

    def before_next_page(self):
        # self.player.price_check()
        self.player.set_payoff2()
        self.player.set_payoff()

    def vars_for_template(self):
        if self.player.test_times2 == 0:
            earn = 'XXX'
            cost_bonus = 'XXX'
            profit_bonus = 'XXX'
            total_bonus_coffee = 'XXX'
            market_demand = 'XXX'
            coffee_not_used = 'XXX'

        else:
            earn = self.player.earn
            cost_bonus = self.player.group.cost_bonus
            profit_bonus = self.player.group.profit_bonus
            total_bonus_coffee = self.player.group.total_bonus_coffee
            market_demand = self.player.market_demand
            coffee_not_used = self.player.coffee_not_used

        return {
            'earn': earn,
            'cost_bonus': cost_bonus,
            'profit_bonus': profit_bonus,
            'total_bonus_coffee': total_bonus_coffee,
            'market_demand': market_demand,
            'coffee_not_used': coffee_not_used
        }

class Waiting2_0(Page):
    def is_displayed(self):
        self.player.set_payoff2()
        return False

class Waiting2(WaitPage):
    body_text = "You are waiting for the message confirmation and progress from the Marketing Manager."
    after_all_players_arrive = 'get_value2'
    
class Res2(Page):
    def is_displayed(self):
        # Set total_bonus_coffee for all participants
        self.group.total_bonus_coffee = self.group.cost_bonus + self.group.profit_bonus + self.session.config['participation_fee']
        self.participant.vars['total_bonus_coffee'] = self.group.total_bonus_coffee

        if self.player.participant.vars['consent'].lower() == 'consent':
            return True
        else:
            return False

    def vars_for_template(self):
        self.participant.payoff = self.group.cost_bonus + self.group.profit_bonus + self.participant.vars[
            'payoff_trust'] + self.participant.vars['payoff_cem']

        return {
            'id': self.player.id_in_group,
            'payoff_trust': self.participant.vars['payoff_trust'],
            'payoff_cem': self.participant.vars['payoff_cem'],
            'payoff_all': self.participant.payoff_plus_participation_fee(),
            'total_bonus_coffee': self.participant.vars['total_bonus_coffee'],
        }

page_sequence = []


page_sequence += [
                Waiting0,
                  Welcome,
                  Info,
                  Summary,
                  Role_Info,
                  passcode,
                  Survey_coffee1,
                  Survey_coffee2,
                  Survey_coffee3,
                  Survey_coffee4,
                  Survey_coffee5,
                  Survey_coffee6,
                  Survey_coffee7,
                  Survey_coffee8,
                  Survey_coffee9,
                  Payment,
                  Payment2,
                  ]

page_sequence += [SetPrice] * 100
page_sequence += [Res1]
page_sequence += [SetPrice] * 100
page_sequence += [Res12]
page_sequence += [SetPrice] * 100
page_sequence += [Res123]

page_sequence += [Waiting1,Res_market]

page_sequence += [SetPrice2] * 100
page_sequence += [Waiting2_0, Waiting2, Res2 ]