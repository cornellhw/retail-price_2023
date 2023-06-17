from otree.api import models, WaitPage, Page

class MyPage(WaitPage):
    group_by_arrival_time = False

    def after_all_players_arrive(self):
        self.subsession.group_randomly()

page_sequence = [MyPage]
