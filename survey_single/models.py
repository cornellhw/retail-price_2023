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

    passcode_second = ''
    name_in_url = 'survey_single'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):



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















