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
Simple game
"""

  
class Constants(BaseConstants):
    F = 10
    X = 10
    r1, r2 = 0.5, 0.7

    name_in_url = 'exp_1c'
    players_per_group = 60
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

# Set the random numbers for suppliers' actual cost between 5-7 dollars，could be decimal
# The random numbers for consumers' willingness to pay 13-15 dollars, could be decimal
class Group(BaseGroup):

    def init_setting(self):
        for p in self.get_players():
            p.C = round(random.uniform(5,7),1)
            p.P = round(random.uniform(13,15),1)
        return

# Initialize of the variables, could be decimal
class Player(BasePlayer):
    # EXP params
    # F = models.FloatField(initial=10)
    # X = models.FloatField(initial=10)
    W = models.FloatField(label='How much would like to bid for one unit according to the average production cost (points)?')
    R = models.FloatField(label='How much would you like to set for the retailing price for one unit of this coffee sample (points)?')
    C = models.FloatField(initial=0)
    P = models.FloatField(initial=0)
    pi = models.FloatField(initial=0)
    payoff1 = models.FloatField(initial=0)
    payoff2 = models.FloatField(initial=0)

    purchase_success= models.IntegerField(initial=0)
    purchase_success2= models.IntegerField(initial=0)

    choice = models.StringField(
        choices=[['1', 'type1'], ['2', 'type2'], ['3', 'type3'], ['4', 'type4']
                 , ['5', 'type5']],
        widget=widgets.RadioSelect,
        # initial='0'
    )

    quality = models.StringField(
        choices=[['0', 'Poor'], ['1', 'Fair'], ['2', 'Good'], ['3', 'Very good']
                 , ['4', 'Excellent!!']],
        # label='你的性别是？',
        widget=widgets.RadioSelect,
        # initial='0'
    )


# Calculate the final profit pi; To see if the offer is higher than the suppliers' actual cost or not
    def price_check(self):
        self.pi = self.P - self.W
        self.purchase_success = int(self.W >= self.C)
        return

# If the offer is accepted, procurement managers' formula of payoffs; Else.
    def set_payoff1(self):
        if self.purchase_success:
            self.payoff1 = Constants.F + Constants.r1 * (Constants.X - self.W)
        else:
            self.payoff1 = Constants.F
        return

# To see if the retail price is lower or equal to the consumers' willingness to pay or not
    def price_check2(self):
        self.purchase_success2 = int(self.R <= self.P)
        return

# If the retail price is accepted, marketing managers' formula of payoffs; Else.
    def set_payoff2(self):
        if self.purchase_success2:
            self.payoff2 = self.payoff1 + Constants.r2*(self.P-self.R)
        else: # cooperate slavage value in case it is not sold.
            self.payoff2 = self.payoff1
        return


