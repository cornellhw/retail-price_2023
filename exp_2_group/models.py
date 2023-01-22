from scipy import stats
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)

import random
import math

doc = """
Simple coffee experiment
"""
class Constants(BaseConstants):

    a1, u1, l1 = 0.2, 10, 2
    a2, u2, l2 = 0.2, 7, 1

    lower, upper = 2, 10
    miu, sigma = 6, 0.5
    F=5
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
    coffee_like_group = models.StringField(initial='')
    cost_bonus_group = models.FloatField(initial=0)
    earn_group = models.FloatField(initial=0)
    total_bonus_group = models.FloatField(initial=0)

    payoff_cem_group = models.FloatField(initial=0)
    payoff_trust_group = models.FloatField(initial=0)
    payoff_total_group = models.FloatField(initial=0)

    def init_setting(self):
        consent = True
        for p in self.get_players():
            # p.C = round(random.random()*8+2,2)  # uniform
            # print(self.dist.rvs(1))
            p.C = float(round(float(self.dist.rvs(1)), 2))  # normal
            print(p.participant.vars)
        #     if p.participant.vars['consent'].lower() != 'consent':
        #         consent= False
        # if consent:
        #     self.consent_group = 'Consent'
        # else:
        #     self.consent_group = 'Do not consent'
        # for p in self.get_players():
        #     p.participant.vars['consent'] = self.consent_group
        #     print(p.participant.vars['consent'] )
        return

    def get_value(self):


        for p in self.get_players():
            if p.role_own == 'A':
                self.W_group = p.W
                self.is_reject_group = p.is_reject
                self.coffee_like_group = p.coffee_like
                self.cost_bonus_group = p.cost_bonus
                self.earn_group = p.earn
                self.total_bonus_group = p.total_bonus

        for p in self.get_players():
            if p.role_own == 'B':
                p.W = self.W_group
                p.is_reject = self.is_reject_group
                p.coffee_like = self.coffee_like_group
                p.cost_bonus = self.cost_bonus_group
                p.earn = self.earn_group
                p.total_bonus = self.total_bonus_group

    def get_value2(self):
        for p in self.get_players():
            if p.role_own == 'B':

                self.payoff_cem_group = p.payoff_cem
                self.payoff_trust_group = p.payoff_trust
                self.payoff_total_group = p.payoff_total

        for p in self.get_players():
            if p.role_own == 'A':
                p.payoff_cem = self.payoff_cem_group
                p.payoff_trust =self.payoff_trust_group
                p.payoff_total = self.payoff_total_group


class Player(BasePlayer):
    W = models.FloatField(label='Enter W here', max=10, initial=0)
    R = models.FloatField(label='How much would you like to set for the retailing price for one unit of this coffee sample (points)?', min=2, max=10, initial=0)
    C = models.FloatField(initial=0)

    role_own = models.StringField(initial='')
    consent = models.StringField(initial='')
    purchase_success = models.IntegerField(initial=0)
    prob = models.FloatField(initial=0)
    is_reject = models.StringField(initial='')
    lockin = models.StringField(initial='-1', blank=True)
    cost_bonus = models.FloatField(initial=0)
    test_times = models.IntegerField(initial=0)

    test_round = models.IntegerField(initial=0)

    lockin2 = models.StringField(initial='-1', blank=True)
    test_times2 = models.IntegerField(initial=0)

    optimal_R = models.FloatField(initial=0)
    optimal_cost_bonus = models.FloatField(initial=0)
    optimal_profit_bonus = models.FloatField(initial=0)
    optimal_total_bonus = models.FloatField(initial=0)
    optimal_sell = models.IntegerField()
    optimal_market_coverage = models.FloatField(initial=0)
    optimal_earn = models.FloatField(initial=0)
    sell = models.IntegerField()
    profit_bonus = models.FloatField(initial=0)
    total_bonus = models.FloatField(initial=0)
    earn = models.FloatField(initial=0)
    market_demand = models.IntegerField()
    coffee_not_used = models.FloatField(initial=0)
    logger_W = models.LongStringField(initial='')
    logger_W_final = models.LongStringField(initial='')
    logger_T = models.LongStringField(initial='')

    quality = models.StringField(
        choices=[['0', 'Poor'], ['1', 'Fair'], ['2', 'Good'], ['3', 'Very good']
                 , ['4', 'Excellent!!']],
        # label='你的性别是？',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    payoff_trust = models.FloatField(initial=0)
    payoff_cem = models.FloatField(initial=0)
    payoff_total = models.FloatField(initial=0)


    # survey
    # age = models.IntegerField(label="What is your age?", min=5, max=125)
    # gender = models.StringField(
    #     choices=[['0', 'male'], ['1', 'female']],
    #     label='What is your gender?',
    #     widget=widgets.RadioSelect,
    # )
    # coffee = models.StringField(
    #     choices=[['0', 'Never'], ['1', 'Once a week'], ['2', 'Two or three times a week'],
    #              ['3', 'Everyday']],
    #     label='How often do you drink the coffee?',
    #     widget=widgets.RadioSelect,
    #     # initial='0'
    # )
    #

    coffee_like = models.StringField(blank=True,initial='')
    coffee_quality = models.StringField(blank=True,initial='')
    coffee_sweetness = models.StringField(blank=True,initial='')
    coffee_flavor = models.StringField(blank=True,initial='')
    coffee_impression = models.StringField(blank=True,initial='')
    coffee_recom = models.StringField(blank=True,initial='')
    coffee_drink = models.StringField(blank=True,initial='')
    coffee_serve = models.StringField(blank=True,initial='')
    coffee_buy = models.StringField(blank=True,initial='')

    coffee_howoften = models.StringField(
        choices=[['7', 'Multiple times daily'], ['6', 'Daily'], ['5', 'Weekly'], ['4', 'Monthly'], ['3', 'Bi-Monthly'],
                 ['2', 'Seasonally'], ['1', 'Never'],
                 ['0', 'Prefer not to answer']],
        label='1. How often do you drink the coffee?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    coffee_where = models.StringField(
        choices=[['5', 'Make at home'], ['4', 'Make at work'], ['3', 'Dine in at a coffee shop'],
                 ['2', 'Take out from a coffee shop'], ['1', 'Prefer not to answer'],
                 ['0', 'Other']],
        label='2. Where do you get your coffee most frequently?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    coffee_where_string = models.StringField(label='', blank=True)
    door_unlocked = models.StringField(
        choices=[['4', 'Very often'], ['3', 'Often'], ['2', 'Sometimes'], ['1', 'Rarely'],
                 ['0', 'Never']],
        label='3. How often do you leave your door unlocked?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lend_money = models.StringField(
        choices=[['3', 'More than once a week'], ['2', 'About once a week'], ['1', 'About once a month'],
                 ['0', 'Once a year or less']],
        label='4. How often do you lend money to your friends?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lend_personal = models.StringField(
        choices=[['3', 'More than once a week'], ['2', 'About once a week'], ['1', 'About once a month'],
                 ['0', 'Once a year or less']],
        label='5. How often do you lend personal possessions to friends (e.g., CDs, clothes, bicycle, etc.)?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lie_parents = models.StringField(
        choices=[['4', 'Very often'], ['3', 'Often'], ['2', 'Sometimes'], ['1', 'Rarely'],
                 ['0', 'Never']],
        label='6. How often do you lie to your parents?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lie_roommates = models.StringField(
        choices=[['4', 'Very often'], ['3', 'Often'], ['2', 'Sometimes'], ['1', 'Rarely'],
                 ['0', 'Never']],
        label='7. How often do you lie to your roommates?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lie_acquaintances = models.StringField(
        choices=[['4', 'Very often'], ['3', 'Often'], ['2', 'Sometimes'], ['1', 'Rarely'],
                 ['0', 'Never']],
        label='8. How often do you lie to your acquaintances?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lie_friends = models.StringField(
        choices=[['4', 'Very often'], ['3', 'Often'], ['2', 'Sometimes'], ['1', 'Rarely'],
                 ['0', 'Never']],
        label='9. How often do you lie to your close friends?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lie_partner = models.StringField(
        choices=[['4', 'Very often'], ['3', 'Often'], ['2', 'Sometimes'], ['1', 'Rarely'],
                 ['0', 'Never']],
        label='10. How often do you lie to your partner?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    take_advantage = models.StringField(
        choices=[['1', 'Would take advantage of you'], ['0', 'Would try to be fair']],
        label='11. Do you think most people would try to take advantage of you if they got a chance, or would they try to be fair?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    try_to_be_helpful = models.StringField(
        choices=[['1', 'Try to be helpful'], ['0', 'Just look out for themselves']],
        label='12. Would you say that most of the time people try to be helpful, or that they are mostly just looking out for themselves?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    trust = models.StringField(
        choices=[['1', 'Most people can be trusted'], ['0', 'Cannot be too careful']],
        label='13. Generally speaking, would you say that most people can be trusted or that you can not be too careful in dealing with people?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    count_on_strangers = models.StringField(
        choices=[['1', 'More or less agree'], ['0', 'More or less disagree']],
        label='14. Do you agree or disagree with the following statement: "You cannot count on strangers anymore',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    deal_with_strangers = models.StringField(
        choices=[['1', 'More or less agree'], ['0', 'More or less disagree']],
        label='15. Do you agree or disagree with the following statement: "When dealing with strangers, one is better off using caution before trusting them',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    recycle = models.StringField(
        choices=[['4', 'Very often'], ['3', 'Often'], ['2', 'Sometimes'], ['1', 'Rarely'],
                 ['0', 'Never']],
        label='16. How often do you recycle?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    more_pay_fair_trade = models.StringField(
        choices=[['0', 'Nothing'], ['1', '1 Dollar'], ['2', '2 Dollars'], ['3', '3 Dollars'],
                 ['4', '4 Dollars or more']],
        label='17. How much more would you pay for a cup of Fair Trade coffee?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    frequency_not_buy = models.StringField(
        choices=[['4', 'Very often'], ['3', 'Often'], ['2', 'Sometimes'], ['1', 'Rarely'],
                 ['0', 'Never']],
        label='18. How frequently do you not buy something that you want, due to where it was made?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    car = models.StringField(
        choices=[['4', 'Strongly agree'], ['3', 'Somewhat agree'], ['2', 'Indifferent'], ['1', 'Somewhat disagree'],
                 ['0', 'Strongly disagree']],
        label='19. Ignoring cost differences, how strongly do you agree with this statement: I would rather drive a well-maintained used car than a brand new one',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    frequency_shoes = models.StringField(
        choices=[['4', 'Very often'], ['3', 'Often'], ['2', 'Sometimes'], ['1', 'Rarely'],
                 ['0', 'Never']],
        label='20. How frequently do you think about the day-to-day lives of the people who made your shoes',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    age = models.IntegerField(label="21. What is your age? (years)", min=5, max=125)
    gender = models.StringField(
        choices=[['0', 'Male'], ['1', 'Female'], ['2', 'Non-binary/third gender'], ['3', 'Prefer not to answer'],
                 ['4', 'Prefer to self-describe']],
        label='22. How do you describe your gender?',
        widget=widgets.RadioSelect,
    )
    gender_string = models.StringField(label='', blank=True)
    describe_white = models.StringField(initial='0', blank=True)
    describe_Middle = models.StringField(initial='0', blank=True)
    describe_Black = models.StringField(initial='0', blank=True)
    describe_American = models.StringField(initial='0', blank=True)
    describe_Asian = models.StringField(initial='0', blank=True)
    describe_Native = models.StringField(initial='0', blank=True)
    describe_Hispanic = models.StringField(initial='0', blank=True)
    describe_other = models.StringField(initial='0', blank=True)
    describe_other_string = models.StringField(initial='', blank=True)
    describe_Prefer = models.StringField(initial='0', blank=True)
    edu = models.StringField(
        choices=[['0', 'Some or no high school'], ['1', 'High school degree or equivalent'], ['2', 'Some college'], ['3', 'Associate’s degree or equivalent'],
                 ['4', 'Bachelor’s degree or equivalent'],['5', 'Graduate degree or equivalent'],['6', 'Prefer not to answer']],
        label='24. What is the highest level of education you have completed?',
        widget=widgets.RadioSelect,
    )

    major = models.StringField(
        choices=[['0', 'Business Administration'], ['1', 'Social Sciences (Anthro., Pol. Science, History)'], ['2', 'Economics'],
                 ['3', 'Sciences (Bio., Physics, Math, Chem.)'],
                 ['4', 'Medicine'],['5', 'Engineering'],['6', 'Law'],['7', 'Arts and Humanities'],['8', 'Architecture and Design'],['9', 'Prefer not to answer'],
                 ['10', 'Other']],
        label='25.If you are currently or have previously attended college, what is or was your major?',
        widget=widgets.RadioSelect,
    )
    major_string = models.StringField(label='', blank=True)

    parents = models.StringField(
        choices=[['0', 'Some or no high school'], ['1', 'High school degree or equivalent'], ['2', 'Some college'], ['3', 'Associate’s degree or equivalent'],
                 ['4', 'Bachelor’s degree or equivalent'],['5', 'Graduate degree or equivalent'],['6', 'Prefer not to answer']],
        label='26.What is the highest level of education completed by either of your parents? ',
        widget=widgets.RadioSelect,
    )

    employment  = models.StringField(
        choices=[['0', 'Working full-time'], ['1', 'Working part-time'], ['2', 'Unemployed and looking for work'], ['3', 'A homemaker or stay-at-home parents'],
                 ['4', 'Student'],['5', 'Retired'],['6', 'Prefer not to answer'], ['7','Other']],
        label='27.What best describes your employment status over the last three months?',
        widget=widgets.RadioSelect,
    )
    employment_string = models.StringField(label='', blank=True)

    income = models.StringField(
        choices=[['0', 'Less than $10,000'], ['1', '$10,000 to $19,999'], ['2', '$20,000 to $29,999'], ['3', '$30,000 to $39,999'],
                 ['4', '$40,000 to $49,999'],['5', '$50,000 to $59,999'],['6', '$60,000 to $69,999'], ['7','$70,000 to $79,999'],
                 ['8', '$80,000 to $89,999'],['9', '$90,000 to $99,999'],['10', '$100,000 to $149,999'], ['11','$150,000 or more'],
                 ['12', 'Prefer not to answer']
                 ],
        label='28.What was your total household income before taxes during the past 12 months?',
        widget=widgets.RadioSelect,
    )
    marital = models.StringField(
        choices=[['0', 'Married'], ['1', 'Living with a partner'], ['2', 'Widowed'], ['3', 'Divorced'],
                 ['4', 'Separated '],['5', 'Never married'],['6', 'Prefer ']],
        label='29.What is your current marital status?',
        widget=widgets.RadioSelect,
    )
    children  = models.StringField(
        choices=[['0', 'Yes'], ['1', 'No'], ['2', 'Prefer not to answer']],
        label='30.Do you have children under 18 years old living in your household?',
        widget=widgets.RadioSelect,
    )

    def init_role(self):
        self.role_own = ['B', 'A'][self.id_in_group % 2] # A: procurement; B: markeing
        return

    def fz(self, w):
        return (w-Constants.miu)/Constants.sigma

    def set_payoff1(self):
        if self.W >= self.C:
            self.is_reject = 'accepted'
            self.cost_bonus = round(self.session.config['a1'] * (10 - self.W) * 20,1)
        else:
            self.is_reject = 'rejected'
            self.cost_bonus = 0
        if self.test_round == 0:
            self.prob = self.fz(self.W)
        elif self.test_round ==1:
            w1 = float(self.logger_W_final.split(',')[0])
            if self.W <= w1:
                self.prob = 0
            else:
                self.prob = (self.fz(self.W) - self.fz(w1))/(1-self.fz(w1))
        else:
            w1 = float(self.logger_W_final.split(',')[0])
            w2 = float(self.logger_W_final.split(',')[1])
            w_max = max(w1, w2)
            if self.W <= w_max:
                self.prob = 0
            else:
                self.prob = (self.fz(self.W) - self.fz(w_max)) / (1-self.fz(w_max))

        self.prob = max(0, self.prob)
        self.prob = round(self.prob, 2)

        self.optimal_R = self.session.config['u2'] / 2
        self.optimal_profit_bonus = round(self.session.config['a2'] * self.optimal_R * (28 * (1-(self.optimal_R-1)/6)),1)
        self.optimal_cost_bonus = round(self.session.config['a1'] * (10 - self.W) * 20, 1)
        self.optimal_total_bonus = round(self.session.config['F'] + self.optimal_cost_bonus + self.optimal_profit_bonus,1)
        self.optimal_earn = round(self.optimal_R * (28 * (1-(self.optimal_R-1)/6)) - self.W,1)

        if self.lockin != 'lockin':
            self.logger_W += str(self.W) + ','
            self.test_times += 1
        else:
            self.logger_W_final += str(self.W) + ','
        return


    def set_payoff2(self):
        sell_temp = 28 * (max(1-(self.R - self.session.config['l2']) / (self.session.config['u2'] - self.session.config['l2']), 0))
        self.sell = int(sell_temp)
        self.earn = int(self.R * sell_temp - self.W)
        self.market_demand = int(round(100*(1-(self.R-1)/6),0))
        self.coffee_not_used = round(
            (self.R - self.session.config['l2']) / (self.session.config['u2'] - self.session.config['l2']), 2)

        self.profit_bonus = round(self.session.config['a2'] * self.R * sell_temp,1)
        if self.lockin2 != 'lockin':
            self.test_times2 += 1
        self.total_bonus = round(5 + self.cost_bonus + self.profit_bonus, 1)

        self.payoff_cem = round(float(self.participant.vars['payoff_cem']*0.02),1)
        self.payoff_trust = round(float(self.participant.vars['payoff_trust']*0.02),1)
        self.payoff_total = round(float(self.total_bonus+(self.participant.vars['payoff_trust']+self.participant.vars['payoff_cem'])*0.02),1)

        return


















