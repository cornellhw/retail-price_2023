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
        else:
            prob = self.player.prob*100
        return {'prob': prob,
                }


class Res1(Page):
    def vars_for_template(self):
        return {'is_reject': self.player.is_reject,
                'reward': self.player.reward
                }

    def is_displayed(self):
        return self.player.consent.lower() == 'consent'


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
page_sequence += [SetPrice2] * 100
page_sequence += [Res2, Survey]
