from scipy import stats
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    cu,
    WaitPage
)

import random
import math
from scipy.stats import norm
doc = """
Simple coffee experiment
"""
class Constants(BaseConstants):

    a1 = 0.2
    a2, u2, l2 = 0.2, 7, 1

    lower, upper = 0, 10
    miu, sigma = 6, 0.5
    participation_fee=5
    tasting = 0
    passcode_second = ''
    name_in_url = 'exp_2_group'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    dist = stats.truncnorm((Constants.lower - Constants.miu) / Constants.sigma,
                    (Constants.upper - Constants.miu) / Constants.sigma,
                    loc=Constants.miu, scale=Constants.sigma)
    W_group = models.FloatField(initial=0)
    R_group = models.FloatField(initial=0)
    is_reject_group = models.StringField(initial='')
    consent_group = models.StringField(initial='')
    coffee_quality_group = models.StringField(initial='')
    cost_bonus_group = models.CurrencyField(initial=0)
    earn_group = models.CurrencyField(initial=0)
    total_bonus_group = models.CurrencyField(initial=0)

    payoff_cem_group = models.CurrencyField(initial=0)
    payoff_trust_group = models.CurrencyField(initial=0)

    payoff_total_group = models.CurrencyField(initial=0)

    total_bonus_coffee = models.CurrencyField(initial=0)
    profit_bonus = models.CurrencyField(initial=0)
    cost_bonus = models.CurrencyField(initial=0)


    def get_players_with_consent(self):
        # get players who gave their consent
        return [p for p in self.get_players() if p.participant.vars['consent'].lower() == 'consent']


    def init_setting(self):
        for p in self.get_players_with_consent():
            p.C = float(round(float(self.dist.rvs(1)), 2))  # normal
            print(p.participant.vars)
        return

    def get_value(self):
        for p in self.get_players_with_consent():
            if p.role_own == 'A':
                self.W_group = p.W
                self.is_reject_group = p.is_reject
                self.coffee_quality_group = p.coffee_quality
                self.cost_bonus_group = p.cost_bonus
                self.earn_group = p.earn

        for p in self.get_players_with_consent():
            if p.role_own == 'B':
                p.W = self.W_group
                p.is_reject = self.is_reject_group
                p.coffee_quality = self.coffee_quality_group
                p.cost_bonus = self.cost_bonus_group
                p.earn = self.earn_group
                p.total_bonus = self.total_bonus_group

    def get_value2(self):
        for p in self.get_players_with_consent():
            if p.role_own == 'B':
                profit_bonus = p.profit_bonus
                total_bonus_group = p.total_bonus
                earn = p.earn

        for p in self.get_players_with_consent():
            if p.role_own == 'A':
                p.profit_bonus = profit_bonus
                p.total_bonus = total_bonus_group
                p.earn = earn


class Player(BasePlayer):
    W = models.FloatField(
        label='Enter W here',
        max=10,
        initial=0
    )
    R = models.FloatField(
        label='How much would you like to set for the retailing price for one unit of this coffee sample (points)?',
        min = 1,
        max = 7,
        initial=0


    )
    C = models.FloatField(
        initial=0
    )

    # survey
    coffee_like = models.StringField(blank=True)
    coffee_quality = models.StringField(blank=True)
    coffee_sweetness = models.StringField(blank=True)
    coffee_flavor = models.StringField(blank=True)
    coffee_impression = models.StringField(blank=True)
    coffee_recom = models.StringField(blank=True)
    coffee_drink = models.StringField(blank=True)
    coffee_serve = models.StringField(blank=True)
    coffee_buy = models.StringField(blank=True)

    role_own = models.StringField(initial='')
    consent = models.StringField(initial='')
    purchase_success = models.IntegerField(initial=0)
    prob = models.FloatField(initial=0)
    is_reject = models.StringField(initial='')
    lockin = models.StringField(initial='-1', blank=True)
    cost_bonus = models.CurrencyField(initial=0)
    test_times = models.IntegerField(initial=0)

    test_round = models.IntegerField(initial=0)

    lockin2 = models.StringField(initial='-1', blank=True)
    test_times2 = models.IntegerField(initial=0)

    tasting_new = models.IntegerField(initial=0)
    passcode_2 = models.StringField(label="Please enter the password to continue with the experiment:",blank=True)
    optimal_R = models.CurrencyField(initial=0)
    optimal_cost_bonus = models.CurrencyField(initial=0)
    optimal_profit_bonus = models.CurrencyField(initial=0)
    optimal_total_bonus = models.CurrencyField(initial=0)
    optimal_earn = models.CurrencyField(initial=0)
    profit_bonus = models.CurrencyField(initial=0)
    total_bonus = models.CurrencyField(initial=0)
    total_bonus_coffee = models.CurrencyField(initial=0)
    earn = models.CurrencyField(initial=0)
    market_demand = models.IntegerField()
    coffee_not_used = models.FloatField(initial=0)
    logger_W = models.LongStringField(initial='')
    logger_W_final = models.LongStringField(initial='')
    logger_T = models.LongStringField(initial='')

    show_res1 = models.IntegerField(initial=0)
    show_res2 = models.IntegerField(initial=0)
    show_res3 = models.IntegerField(initial=0)

    payoff_trust = models.CurrencyField(initial=0)
    payoff_cem = models.CurrencyField(initial=0)
    payoff_total = models.CurrencyField(initial=0)


    def init_role(self):
        self.role_own = ['B', 'A'][self.id_in_group % 2] # A: procurement; B: markeing
        return

    def tast(self):
        self.tasting_new = self.session.config['tasting']

    def fz(self, w):
        return norm.cdf((w-Constants.miu)/Constants.sigma)

    def set_payoff1(self):
        self.is_reject = 'accepted' if self.W >= self.C else 'rejected'
        self.group.cost_bonus = cu(round(self.session.config['a1'] * (10 - self.W) * 20, 1)) if self.W >= self.C else cu(0)

        if self.test_round == 0:
            self.prob = self.fz(self.W)
            self.show_res1 = 1
        elif self.test_round == 1:
            w1 = float(self.logger_W_final.split(',')[0])
            self.show_res2 = 1
            self.prob = (self.fz(self.W) - self.fz(w1)) / (1 - self.fz(w1)) if self.W > w1 else 0

        else:
            self.show_res3 = 1
            w1, w2 = map(float, self.logger_W_final.split(',')[:2])
            w_max = max(w1, w2)
            self.prob = (self.fz(self.W) - self.fz(w_max)) / (1 - self.fz(w_max)) if self.W > w_max else 0

        self.prob = max(0, self.prob)
        self.prob = round(self.prob, 3)

        self.optimal_R = cu(round(self.session.config['u2'] / 2, 2))
        self.optimal_profit_bonus = cu(round(
            self.session.config['a2'] * self.optimal_R * (28 * (1 - (self.optimal_R - 1) / 6)), 2))
        self.optimal_cost_bonus = cu(round(self.session.config['a1'] * (10 - self.W) * 20, 2)).to_real_world_currency(
            self.session)
        self.optimal_total_bonus = cu(
            round(self.session.config['participation_fee'] + self.optimal_cost_bonus + self.optimal_profit_bonus, 2))
        self.optimal_earn = cu(round(self.optimal_R * (28 * (1 - (self.optimal_R - 1) / 6)) - self.W, 2))

        if self.lockin != 'lockin':
            self.logger_W += str(self.W) + ','
            self.test_times += 1
        else:
            self.logger_W_final += str(self.W) + ','
        return


    def set_payoff2(self):
        sell_temp = 28 * (max(1-(self.R - self.session.config['l2']) / (self.session.config['u2'] - self.session.config['l2']), 0))
        self.earn = cu(round((self.R * sell_temp - self.W), 2))
        self.market_demand = int(round(100*(1-(self.R-1)/6),0))
        self.coffee_not_used = round(
            (self.R - self.session.config['l2']) / (self.session.config['u2'] - self.session.config['l2']), 2)

        self.group.profit_bonus = cu(round(self.session.config['a2'] * self.R * sell_temp, 2))
        if self.lockin2 != 'lockin':
            self.test_times2 += 1


        return

    def set_payoff(self):

        self.group.total_bonus_coffee = self.group.cost_bonus + self.group.profit_bonus + self.session.config['participation_fee']
        self.participant.payoff = self.group.cost_bonus + self.group.profit_bonus + self.participant.vars[
            'payoff_trust'] + self.participant.vars['payoff_cem']



















