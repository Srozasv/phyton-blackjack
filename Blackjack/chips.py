class Chips():
    def __init__(self,total = 100):
        self.total = total
        self.bet = 0

    def lose_bet(self):
        self.total = self.total - self.bet
        return self.total

    def win_bet(self):
        self.total = self.total + self.bet/2
        return self.total