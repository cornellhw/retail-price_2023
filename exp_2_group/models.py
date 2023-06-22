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
    num_rounds = 3


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

    coffee_like = models.StringField(blank=True)
    coffee_quality = models.StringField(blank=True)
    coffee_sweetness = models.StringField(blank=True)
    coffee_flavor = models.StringField(blank=True)
    coffee_impression = models.StringField(blank=True)
    coffee_recom = models.StringField(blank=True)
    coffee_drink = models.StringField(blank=True)
    coffee_serve = models.StringField(blank=True)
    coffee_buy = models.StringField(blank=True)

    coffee_howoften = models.StringField(
        choices=[['Multiple daily', 'Multiple times daily'], ['Daily', 'Daily'], ['Weekly', 'Weekly'], ['Monthly', 'Monthly'], ['Bi-Monthly', 'Bi-Monthly'],
                 ['Seasonally', 'Seasonally'], ['Never', 'Never'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='1. How often do you drink coffee?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    coffee_where = models.StringField(
        choices=[['Home', 'Make at home'], ['Work', 'Make at work'], ['Dine_coffee shop', 'Dine in at a coffee shop'],
                 ['Take out_coffee shop', 'Take out from a coffee shop'],['Not_to_answer', 'Prefer not to answer'],
                 ['Other', 'Other']],
        label='2. Where do you get your coffee most frequently?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    coffee_where_string = models.StringField(label='', blank=True)
    door_unlocked = models.StringField(
        choices=[['Very often', 'Very often'], ['Often', 'Often'], ['Sometimes', 'Sometimes'], ['Rarely', 'Rarely'],['Never', 'Never'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='3. How often do you leave your door unlocked?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lend_money = models.StringField(
        choices=[['More_once a week', 'More than once a week'], ['Once a week', 'About once a week'], ['Once a month', 'About once a month'],['Once a year', 'Once a year or less'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='4. How often do you lend money to your friends?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lend_personal = models.StringField(
        choices=[['More_once a week', 'More than once a week'], ['Once a week', 'About once a week'], ['Once a month', 'About once a month'],['Once a year', 'Once a year or less'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='5. How often do you lend personal possessions to friends (e.g., CDs, clothes, bicycle, etc.)?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lie_parents = models.StringField(
        choices=[['Very often', 'Very often'], ['Often', 'Often'], ['Sometimes', 'Sometimes'], ['Rarely', 'Rarely'],['Never', 'Never'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='6. How often do you lie to your parents?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lie_roommates = models.StringField(
        choices=[['Very often', 'Very often'], ['Often', 'Often'], ['Sometimes', 'Sometimes'], ['Rarely', 'Rarely'],['Never', 'Never'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='7. How often do you lie to your roommates?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lie_acquaintances = models.StringField(
        choices=[['Very often', 'Very often'], ['Often', 'Often'], ['Sometimes', 'Sometimes'], ['Rarely', 'Rarely'],['Never', 'Never'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='8. How often do you lie to your acquaintances?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lie_friends = models.StringField(
        choices=[['Very often', 'Very often'], ['Often', 'Often'], ['Sometimes', 'Sometimes'], ['Rarely', 'Rarely'],['Never', 'Never'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='9. How often do you lie to your close friends?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    lie_partner = models.StringField(
        choices=[['Very often', 'Very often'], ['Often', 'Often'], ['Sometimes', 'Sometimes'], ['Rarely', 'Rarely'],['Never', 'Never'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='10. How often do you lie to your partner?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    take_advantage = models.StringField(
        choices=[['1', 'Would take advantage of you'], ['0', 'Would try to be fair'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='11. Do you think most people would try to take advantage of you if they got a chance, or would they try to be fair?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    try_to_be_helpful = models.StringField(
        choices=[['1', 'Try to be helpful'], ['0', 'Just look out for themselves'],
            ['Not_to_answer', 'Prefer not to answer']],
        label='12. Would you say that most of the time people try to be helpful, or that they are mostly just looking out for themselves?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    trust = models.StringField(
        choices=[['1', 'Most people can be trusted'], ['0', 'Cannot be too careful'],
        ['Not_to_answer', 'Prefer not to answer']],
    label='13. Generally speaking, would you say that most people can be trusted or that you can not be too careful in dealing with people?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    count_on_strangers = models.StringField(
        choices=[['0', 'More or less agree'], ['1', 'More or less disagree'],
        ['Not_to_answer', 'Prefer not to answer']],
        label='14. Do you agree or disagree with the following statement: "You cannot count on strangers anymore".',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    deal_with_strangers = models.StringField(
        choices=[['0', 'More or less agree'], ['1', 'More or less disagree'],
        ['Not_to_answer', 'Prefer not to answer']],
    label='15. Do you agree or disagree with the following statement: "When dealing with strangers, one is better off using caution before trusting them".',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    recycle = models.StringField(
        choices=[['Very often', 'Very often'], ['Often', 'Often'], ['Sometimes', 'Sometimes'], ['Rarely', 'Rarely'],['Never', 'Never'],
        ['Not_to_answer', 'Prefer not to answer']],
    label='16. How often do you recycle?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    more_pay_fair_trade = models.StringField(
        choices=[['Nothing', 'Nothing'], ['1 Dollar', '1 Dollar'], ['2 Dollars', '2 Dollars'], ['3 Dollars', '3 Dollars'],['4 Dollars_more', '4 Dollars or more'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='17. How much more would you pay for a cup of Fair Trade coffee?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    frequency_not_buy = models.StringField(
        choices=[['Very often', 'Very often'], ['Often', 'Often'], ['Sometimes', 'Sometimes'], ['Rarely', 'Rarely'],['Never', 'Never'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='18. How frequently do you not buy something that you want, due to where it was made?',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    car = models.StringField(
        choices=[['Strongly agree', 'Strongly agree'], ['Somewhat agree', 'Somewhat agree'], ['Indifferent', 'Indifferent'], ['Somewhat disagree', 'Somewhat disagree'],['Strongly disagree', 'Strongly disagree'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='19. Ignoring cost differences, how strongly do you agree with this statement: I would rather drive a well-maintained used car than a brand new one.',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    frequency_shoes = models.StringField(
        choices=[['Very often', 'Very often'], ['Often', 'Often'], ['Sometimes', 'Sometimes'], ['Rarely', 'Rarely'],['Never', 'Never'],
                 ['Not_to_answer', 'Prefer not to answer']],
        label='20. How frequently do you think about the day-to-day lives of the people who made your shoes.',
        widget=widgets.RadioSelect,
        # initial='0'
    )
    age = models.IntegerField(label="21. What is your age? (years)", min=5, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'], ['third gender', 'Non-binary/third gender'], ['Not_to_answer', 'Prefer not to answer'],
                 ['self-describe', 'Prefer to self-describe']],
        label='22. How do you describe your gender?',
        widget=widgets.RadioSelect,
    )
    gender_string = models.StringField(label='', blank=True)
    race = models.StringField(
        choices=[['White', 'White'], ['Middle Eastern/North African', 'Middle Eastern or North African'],
                 ['Black/African American', 'Black or African American'], ['American Indian', 'American Indian or Alaska Native'],
                 ['Asian', 'Asian (including South Asian)'], ['Native Hawaiian', 'Native Hawaiian or Pacific Islander'],
                 ['Hispanic/Latino', 'Hispanic/Latino'],['Not_to_answer', 'Prefer not to answer'],
                 ['Other', 'Other']],
        label='23. Which of the following best describes you?',
        widget=widgets.RadioSelect,
    )
    race_string = models.StringField(label='', blank=True)
    edu = models.StringField(
        choices=[['No high school', 'Some or no high school'], ['High school', 'High school degree or equivalent'], ['College', 'Some college'], ['Associate', 'Associate’s degree or equivalent'],
                 ['Bachelor', 'Bachelor’s degree or equivalent'],['Graduate', 'Graduate degree or equivalent'],['Not_to_answer', 'Prefer not to answer']],
        label='24. What is the highest level of education you have completed?',
        widget=widgets.RadioSelect,
    )

    major = models.StringField(
        choices=[['Business', 'Business Administration'], ['Social Sciences', 'Social Sciences (Anthro., Pol. Science, History)'], ['Economics', 'Economics'],
                 ['Sciences', 'Sciences (Bio., Physics, Math, Chem.)'],
                 ['Medicine', 'Medicine'],['Engineering', 'Engineering'],['Law', 'Law'],['Arts', 'Arts and Humanities'],['Architecture', 'Architecture and Design'],['Not_to_answer', 'Prefer not to answer'],
                 ['Other', 'Other']],
        label='25. If you are currently or have previously attended college, what is or was your major?',
        widget=widgets.RadioSelect,
    )
    major_string = models.StringField(label='', blank=True)

    parents = models.StringField(
        choices=[['No high school', 'Some or no high school'], ['High school', 'High school degree or equivalent'], ['College', 'Some college'], ['Associate', 'Associate’s degree or equivalent'],
                 ['Bachelor', 'Bachelor’s degree or equivalent'],['Graduate', 'Graduate degree or equivalent'],['Not_to_answer', 'Prefer not to answer']],
        label='26. What is the highest level of education completed by either of your parents? ',
        widget=widgets.RadioSelect,
    )

    employment  = models.StringField(
        choices=[['Full-time', 'Working full-time'], ['Part-time', 'Working part-time'], ['Unemployed', 'Unemployed and looking for work'], ['Homemaker', 'A homemaker or stay-at-home parents'],
                 ['Student', 'Student'],['Retired', 'Retired'],['Not_to_answer', 'Prefer not to answer'], ['Other','Other']],
        label='27. What best describes your employment status over the last three months?',
        widget=widgets.RadioSelect,
    )
    employment_string = models.StringField(label='', blank=True)

    income = models.StringField(
        choices=[['less_$10,000', 'Less than $10,000'], ['$10,000-$19,999', '$10,000 to $19,999'], ['$20,000-$29,999', '$20,000 to $29,999'], ['$30,000-$39,999', '$30,000 to $39,999'],
                 ['$40,000-$49,999', '$40,000 to $49,999'],['$50,000-$59,999', '$50,000 to $59,999'],['$60,000-$69,999', '$60,000 to $69,999'], ['$70,000-$79,999','$70,000 to $79,999'],
                 ['$80,000-$89,999', '$80,000 to $89,999'],['$90,000-$99,999', '$90,000 to $99,999'],['$100,000-$149,999', '$100,000 to $149,999'], ['$150,000_more','$150,000 or more'],
                 ['Not_to_answer', 'Prefer not to answer']
                 ],
        label='28. What was your total household income before taxes during the past 12 months?',
        widget=widgets.RadioSelect,
    )
    marital = models.StringField(
        choices=[['Married', 'Married'], ['Living_with_partner', 'Living with a partner'], ['Widowed', 'Widowed'], ['Divorced', 'Divorced'],
                 ['Separated', 'Separated'],['Never married', 'Never married'],['Not_to_answer', 'Prefer not to answer']],
        label='29. What is your current marital status?',
        widget=widgets.RadioSelect,
    )
    children  = models.StringField(
        choices=[['1', 'Yes'], ['0', 'No'], ['Not_to_answer', 'Prefer not to answer']],
        label='30. Do you have children under 18 years old living in your household?',
        widget=widgets.RadioSelect,
    )

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



















