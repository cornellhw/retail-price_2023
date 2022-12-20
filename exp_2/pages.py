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


class Welcome(Page):
    def vars_for_template(self):
        self.group.init_setting()

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'


class Info(Page):
    def is_displayed(self):
        return self.player.consent.lower() == 'consent'


class Summary(Page):
    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

class Survey1(Page):
    form_model = 'player'
    form_fields = ['coffee_howoften', 'coffee_where', 'coffee_where_string',
                   'door_unlocked', 'lend_money', 'lend_personal', 'lie_parents', 'lie_roommates',
                   'lie_acquaintances', 'lie_friends', 'lie_partner']

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'
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
        return self.player.consent.lower() == 'consent'
        # return True

    def error_message(self, values):
        errors = [1 for f in values if 'string' not in f and not values[f]]
        if errors:
            return 'you should select your answer'

class Survey3(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'gender_string',
                   'describe_white','describe_Middle','describe_Black', 'describe_American',
                   'describe_Asian','describe_Native','describe_Hispanic','describe_Prefer','describe_other', 'describe_other_string',
                   'edu','major','major_string','parents','employment', 'employment_string',
                   'income','marital','children',
                   ]

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'
        # return True

    def error_message(self, values):
        errors = [1 for f in values if 'string' not in f and not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee1(Page):
    form_model = 'player'
    form_fields = ['coffee_like']

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee2(Page):
    form_model = 'player'
    form_fields = ['coffee_quality']

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee3(Page):
    form_model = 'player'
    form_fields = ['coffee_sweetness']

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee4(Page):
    form_model = 'player'
    form_fields = ['coffee_flavor']

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee5(Page):
    form_model = 'player'
    form_fields = ['coffee_impression']

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee6(Page):
    form_model = 'player'
    form_fields = ['coffee_recom']

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'
        # return True

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee7(Page):
    form_model = 'player'
    form_fields = ['coffee_drink']

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee8(Page):
    form_model = 'player'
    form_fields = ['coffee_serve']

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Survey_coffee9(Page):
    form_model = 'player'
    form_fields = ['coffee_buy']

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class Payment(Page):
    def is_displayed(self):
        return self.player.consent.lower() == 'consent'


class Payment2(Page):
    def is_displayed(self):
        return self.player.consent.lower() == 'consent'


class SetPrice(Page):
    form_model = 'player'
    form_fields = ['W', 'lockin']

    def is_displayed(self):
        if self.player.consent.lower() != 'consent':
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
            prob = '---'
            cost_bonus= '---'
            optimal_profit_bonus = '---'
            optimal_total_bonus = '---'
            optimal_sell='---'
            optimal_market_coverage = '---'
            optimal_earn = '---'

        else:
            prob = self.player.prob*100
            cost_bonus = self.player.cost_bonus
            optimal_profit_bonus = self.player.optimal_profit_bonus
            optimal_total_bonus = self.player.optimal_total_bonus
            optimal_sell = self.player.optimal_sell
            optimal_market_coverage = self.player.optimal_market_coverage
            optimal_earn = self.player.optimal_earn
        return {'prob': prob if isinstance(prob, float) else prob[0],
                'cost_bonus' : cost_bonus,
                'optimal_profit_bonus': optimal_profit_bonus if isinstance( optimal_profit_bonus, float) else  optimal_profit_bonus[0],
                'optimal_total_bonus': optimal_total_bonus,
                'optimal_sell': optimal_sell,
                'optimal_market_coverage': optimal_market_coverage,
                'optimal_earn': optimal_earn,
                'round': ['first', 'second', 'third'][self.player.test_round],
                'round_n': ['1st', '2nd', '3rd'][self.player.test_round],
                }


class Res1(Page):
    def vars_for_template(self):
        if self.player.is_reject == 'rejected' and self.player.test_round<3:
            next_info = 'Click the "next" button to continue the procurement price setting!'
        else:
            next_info = 'Click the "next" button to finish the post-experiment survey! '
        return {'is_reject': self.player.is_reject,
                'cost_bonus': self.player.cost_bonus,
                'next_info': next_info
                }

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

    def before_next_page(self):
        self.player.test_round += 1
        self.player.logger_W += '| '
        self.player.logger_T += str(self.player.test_times)+','
        if self.player.is_reject == 'rejected' and self.player.test_round<3:
            self.player.lockin = '-1'
            self.player.test_times = 0

class SetPrice2(Page):
    form_model = 'player'
    form_fields = ['R', 'lockin2']

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'

    def is_displayed(self):
        if self.player.consent.lower() != 'consent':
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

    def vars_for_template(self):
        if self.player.test_times2 == 0:
            sell = '28(1−(R−1)/7−1)'
            market_coverage = '(1−(R−1)/7−1)'
            earn = '[R∗{28(1−(R−1)/(7−1))}−W]'
            cost_bonus = 'F + 0.5∗(10-W)'
            profit_bonus = '0.5∗[R∗{28(1−(R−1)/(7−1))}−W]'
            total_bonus = 'F + 0.5∗(10-W) + 0.5∗[R∗{28(1−R−2/10−2)}−W]'
        else:
            sell = self.player.sell
            market_coverage = self.player.market_coverage
            earn = self.player.earn
            cost_bonus = self.player.cost_bonus
            profit_bonus = self.player.profit_bonus
            total_bonus = self.player.total_bonus
        return {'sell': sell,
                'market_coverage': [f'{market_coverage}:.2f' if isinstance(market_coverage, float) else market_coverage][0],
                'earn': earn,
                'cost_bonus': [f'{cost_bonus}:.2f' if isinstance(cost_bonus, float) else cost_bonus][0],
                'profit_bonus': [f'{profit_bonus}:.2f' if isinstance(profit_bonus, float) else profit_bonus][0],
                'total_bonus': [f'{total_bonus}:.2f' if isinstance(total_bonus, float) else total_bonus][0],
                }


class Res2(Page):
    def is_displayed(self):
        if self.player.consent.lower() != 'consent':
            return False
        if self.player.is_reject == 'accepted':
            return True
        else:
            return False


class Survey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'coffee']

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

    def error_message(self, values):
        errors = [1 for f in values if not values[f]]
        if errors:
            return 'you should select your answer'


class End(Page):
    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

class Final(Page):
    def is_displayed(self):
        return self.player.consent.lower() == 'consent'

    def vars_for_template(self):
        return {'id': self.player.id_in_group}
page_sequence = []


page_sequence += [Consent,
                  Welcome,
                  Info,
                  Summary,
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
page_sequence += [Res1]
page_sequence += [SetPrice] * 100
page_sequence += [Res1]

page_sequence += [SetPrice2] * 100
page_sequence += [Res2, Survey1, Survey2, Survey3, Final,]