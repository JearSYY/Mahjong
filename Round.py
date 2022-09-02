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
        self.isEnd = False
        self.currentPlayer = 0

    def update(self, n_lichi, n_draw, dora, n_round, quarter_index, isEnd, currentPlayer):
        self.n_lichi = n_lichi
        self.n_draw = n_draw
        self.dora = dora
        self.n_round = n_round
        self.quarter_index = quarter_index
        self.isEnd = isEnd
        self.currentPlayer = currentPlayer

    def getRoundInfo(self):
        return self.n_lichi, self.n_draw, self.dora, self.n_round, self.quarter_index


class RoundMonitor():
    def __init__(self, rinfo):

        # 包含吃碰杠，振听，胡牌信息
        self.info = rinfo


    def start(self):
        return

    def launch(self, players):

        while(not self.isEnd):
            cplayer = players.getPlayer(self.info.currentPlayer)
            cplayer.draw()
            self.check("self")
            cplayer.discard()

        return

    def end(self):
        return

    def check(self, cktype):
        self.checkHuro()
        self.checkRon()
        self.checkDraw()
        return

    def checkDraw(self):
        return

    def checkHuro(self):
        return

    def checkRon(self):
        return

    def checkEnd(self):
        return

    def updateInfo(self):
        return


