'''
Record players info
----------------------------------------------------------------------
Version 1.0
Author: JearFSA
Date:   2022.09.01
----------------------------------------------------------------------
'''

class Player():
    def __init__(self, name, place, point):
        self.name = name
        self.place = place
        self.point = point
        self.rank = 0

    def update(self, point, rank):
        self.point = point
        self.rank = rank


