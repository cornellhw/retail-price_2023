from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Welcome(Page):
    def vars_for_template(self):
        self.group.init_setting()

class Info(Page):
    pass

class Summary(Page):
    pass

class Survey_coffee(Page):
    form_model = 'player'
    form_fields = ['coffee_like', 'coffee_quality', 'coffee_sweetness',
                   'coffee_flavor', 'coffee_impression', 'coffee_recom',
                   'coffee_serve', 'coffee_buy', 'coffee_drink']
class Payment(Page):
    pass

class Payment2(Page):
    pass

class SetPrice(Page):
    form_model = 'player'
    form_fields = ['W', 'lockin']

    def is_displayed(self):
        if self.player.lockin == '1':
            return False
        else:
            return True


    def before_next_page(self):
        # self.player.price_check()
        self.player.set_payoff1()

    def vars_for_template(self):
        if self.player.test_times == 0:
            is_reject = '(rejected/accepted)'
            reward = '$5 or 5+0.5∗(10−W)'
        else:
            is_reject = self.player.is_reject
            reward = self.player.reward
        return {'is_reject': is_reject,
                'reward': reward
                }

class Res1(Page):
    def vars_for_template(self):
        return {'is_reject': self.player.is_reject,
                'reward': self.player.reward
                }


class SetPrice2(Page):
    form_model = 'player'
    form_fields = ['R', 'lockin2']

    def is_displayed(self):
        if self.player.is_reject == 'accepted':
            if self.player.lockin2 == '1':
                return False
            else:
                return True
        else:
            return False

    def before_next_page(self):
        # self.player.price_check()
        self.player.set_payoff2()

    def vars_for_template(self):
        if self.player.test_times2 == 0:
            sell = '28(1−R−2/10−2)'
            earn = '[R∗{28(1−R−2/10−2)}−W]'
            bonus = '0.5∗[R∗{28(1−R−2/10−2)}−W]'
        else:
            sell = self.player.sell
            earn = self.player.earn
            bonus = self.player.bonus
        return {'sell': sell,
                'earn': earn,
                'bonus': bonus
                }

class Res2(Page):
    def is_displayed(self):
        if self.player.is_reject == 'accepted':
            return True
        else:
            return False

class Survey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'coffee']

class End(Page):
    pass


page_sequence = [Welcome,
                 Info,
                 Summary,
                 Survey_coffee,
                 Payment,
                 Payment2,
                 ]

page_sequence += [SetPrice]*100
page_sequence += [Res1]
page_sequence += [SetPrice2]*100
page_sequence += [Res2, Survey]