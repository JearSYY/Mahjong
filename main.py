'''
This project is to play. Wish I have a pleasant journey here.
By JearFSA
Aug 31 2022
'''

# Store constants to define the rule of the game


import Game
from Player import *

class Rules():
    def __init__(self, base_point, extra_point, n_rdora, has_mYkm, has_kykm, has_oneron,
                 has_mdraw):

        self.base_point = base_point
        self.extra_point = extra_point
        self.n_rdora = n_rdora
        self.has_mdraw = has_mdraw
        self.has_mykm = has_mYkm
        self.has_kykm = has_kykm
        self.has_oneron = has_oneron






def main():

    players = Players()
    game = Game()
    round = game.start()
    game.end()

    return


