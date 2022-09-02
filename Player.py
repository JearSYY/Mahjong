'''
Record players info
----------------------------------------------------------------------
Version 1.0
Author: JearFSA
Date:   2022.09.01
----------------------------------------------------------------------
'''

class Players():
    def __init__(self, player0, player1, player2, player3 ):
        self.player0 = Player(0)
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.player3 = Player(3)

    def getPlayer(self, cp):
        if ( cp==0 ):
            return self.player0
        if ( cp==1 ):
            return self.player1
        if ( cp==2 ):
            return self.player2
        if ( cp==3 ):
            return self.player3



class Player():
    def __init__(self, hand, index, name=None, point=25000):
        self.name = name
        self.index = index
        self.point = point
        self.rank = 0
        self.hand = None

    def update(self, point, rank):
        self.point = point
        self.rank = rank

    def draw(self):
        return

    def discard(self):
        return


