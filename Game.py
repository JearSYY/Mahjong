'''
To supervise all actions in a game
----------------------------------------------------------------------
Version 1.0
Author: JearFSA
Date:   2022.09.01
----------------------------------------------------------------------
'''

import Round


class Game():
    def __init__(self):
        return

    def start(self):
        return Round()

    def launch(self, round, players):

        round.start()
        round.launch(players)
        round.end()
        return

    def end(self):
        return







