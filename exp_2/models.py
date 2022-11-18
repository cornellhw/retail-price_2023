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
    a1, u1, l1 = 0.5, 10, 2
    a2, u2, l2 = 0.5, 10, 2

    F = 5
    name_in_url = 'exp_2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def init_setting(self):
        for p in self.get_players():
            p.C = round(random.uniform(2,10), 2)
        return


class Player(BasePlayer):
    W = models.FloatField(label='Enter W here', max=10)
    R = models.FloatField(
        label='How much would you like to set for the retailing price for one unit of this coffee sample (points)?',
        min=2, max=10)
    C = models.FloatField(initial=0)

    consent = models.StringField(initial='')
    purchase_success = models.IntegerField(initial=0)
    prob = models.FloatField()
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

    coffee_like = models.StringField(blank=True)
    coffee_quality = models.StringField(blank=True)
    coffee_sweetness = models.StringField(blank=True)
    coffee_flavor = models.StringField(blank=True)
    coffee_impression = models.StringField(blank=True)
    coffee_recom = models.StringField(blank=True)
    coffee_drink = models.StringField(blank=True)
    coffee_serve = models.StringField(blank=True)
    coffee_buy = models.StringField(blank=True)

    def set_payoff1(self):
        if self.W >= self.C:
            self.is_reject = 'accepted'
            self.reward = self.session.config['F'] + self.session.config['a1'] * (10 - self.W)
        else:
            self.is_reject = 'rejected'
            self.reward = self.session.config['F']
        self.prob = (self.W - self.session.config['l1']) / (self.session.config['u1'] - self.session.config['l1'])
        if self.lockin != 'lockin':
            self.test_times += 1
        return

    def set_payoff2(self):
        temp = int(
            28 * max(1-(self.R - self.session.config['l2']) / (self.session.config['u2'] - self.session.config['l2']), 0))
        self.sell = temp
        self.earn = self.R * (temp - self.W)
        self.bonus = self.session.config['a2'] * self.R * (temp - self.W)
        if self.lockin2 != 'lockin':
            self.test_times2 += 1
        return


