from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)
import random

doc = """
Simple trust game
"""


class Constants(BaseConstants):
    F = 5
    X = 10

    name_in_url = 'exp_1c'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def init_setting(self):
        for p in self.get_players():
            p.C = round(random.random() * 2 + 5, 2)
            p.P = round(random.random() * 2 + 13, 2)
        return


class Player(BasePlayer):
    # EXP params
    # F = models.FloatField(initial=10)
    # X = models.FloatField(initial=10)
    W = models.FloatField(label='Enter W here')
    R = models.FloatField(
        label='How much would you like to set for the retailing price for one unit of this coffee sample (points)?')
    C = models.FloatField(initial=0)
    P = models.FloatField(initial=0)
    pi = models.FloatField(initial=0)
    payoff1 = models.FloatField(initial=0)
    payoff2 = models.FloatField(initial=0)

    consent = models.StringField(initial='')
    purchase_success = models.IntegerField(initial=0)
    purchase_success2 = models.IntegerField(initial=0)

    is_reject = models.StringField(initial='')
    test = models.StringField(initial='0')
    lockin = models.StringField(initial='-1', blank=True)
    reward = models.FloatField(initial=0)
    test_times = models.IntegerField(initial=0)

    lockin2 = models.StringField(initial='-1', blank=True)
    test_times2 = models.IntegerField(initial=0)

    sell = models.FloatField()
    bonus = models.FloatField()
    earn = models.FloatField()

    quality = models.StringField(
        choices=[['0', 'Poor'], ['1', 'Fair'], ['2', 'Good'], ['3', 'Very good']
            , ['4', 'Excellent!!']],
        # label='你的性别是？',
        widget=widgets.RadioSelect,
        # initial='0'
    )

    # survey
    age = models.IntegerField(label="What is your age?", min=5, max=125)
    gender = models.StringField(
        choices=[['0', 'male'], ['1', 'female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    coffee = models.StringField(
        choices=[['0', 'Never'], ['1', 'Once a week'], ['2', 'Two or three times a week'],
                 ['3', 'Everyday']],
        label='How often do you drink the coffee?',
        widget=widgets.RadioSelect,
        # initial='0'
    )

    coffee_like = models.StringField()
    coffee_quality = models.StringField()
    coffee_sweetness = models.StringField()
    coffee_flavor = models.StringField()
    coffee_impression = models.StringField()
    coffee_recom = models.StringField()
    coffee_drink = models.StringField()
    coffee_serve = models.StringField()
    coffee_buy = models.StringField()

    def price_check(self):
        self.pi = self.P - self.W
        self.purchase_success = int(self.W >= self.C)
        return

    def set_payoff1(self):
        if self.W >= 10:
            self.is_reject = 'accepted'
            self.reward = 0.5 * (10 - self.W)
        else:
            self.is_reject = 'rejected'
            self.reward = 5
        if self.lockin != 'lockin':
            self.test_times += 1
        return

    def price_check2(self):
        self.purchase_success2 = int(self.R <= self.P)
        return

    def set_payoff2(self):
        self.sell = self.R
        self.earn = 2 * self.R
        self.bonus = 3 * self.R
        if self.lockin2 != 'lockin':
            self.test_times2 += 1

        return