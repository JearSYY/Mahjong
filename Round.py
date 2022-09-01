'''
To supervise all actions in a round
----------------------------------------------------------------------
Version 1.0
Author: JearFSA
Date:   2022.09.01
----------------------------------------------------------------------
'''

class RoundInfo():
    def __init__(self):
        self.n_lichi = 0
        self.n_draw = 0
        self.dora = None
        self.n_round = 0
        self.quarter_index = 0

    def update(self, n_lichi, n_draw, dora, n_round, quarter_index):
        self.n_lichi = n_lichi
        self.n_draw = n_draw
        self.dora = dora
        self.n_round = n_round
        self.quarter_index = quarter_index

    def getRoundInfo(self):
        return self.n_lichi, self.n_draw, self.dora, self.n_round, self.quarter_index



class Round():
    def __init__(self):