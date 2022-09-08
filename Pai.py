'''
Define class Pai, Pai and their operations
--------------------------------------------------
Version:1.0
Author: JearFSA
Date: Sep 8 2022
'''

import random

class Pai():
    def __init__(self, str, is_dora=False):
        self.rank = int(str[0])
        self.type = str[1]
        self.is_dora = is_dora
        self.value = self.getValue()

    def toStr(self):
        return(str(self.rank) + self.type)

    def compare(self, pai):
        return (self.type==pai.type and self.rank==pai.rank)

    def getValue(self):
        if self.type == "m":
            return self.rank
        elif self.type == "p":
            return self.rank+ 9
        elif self.type == "s":
            return self.rank + 18
        elif self.type == "w":
            return self.rank + 27
        elif self.type == "d":
            return self.rank + 36


class PaiSet():
    def __init__(self, str = None, paiList = None):
        if str == None:
            self.paiList = paiList
        else:
            self.paiList = str2PaiList(str)

    def append(self, pai):
        self.paiList.append(pai)

    def sort(self):
        self.paiList.sort(key=lambda x: x.value)

    def getValues(self):
        values = []
        for pai in self.paiList:
            values.append(pai.getValue())
        return values

    def getStr(self):
        return paiList2Str(self.paiList)

    def shuffle(self):
        random.shuffle(self.paiList)


# seems complicated, see whether it can improve
def paiList2Str(paiList):
    str = ""
    cache = []
    tmp_type = ""
    for i in range(len(paiList)):
        pai = paiList[i]
        if i != len(paiList) - 1:
            if pai.type == paiList[i + 1].type:
                cache.append(pai.rank)
            else:
                cache.append(pai.rank)
                for c in cache:
                    str += c.__str__() + pai.type
                cache.clear()
        else:
            cache.append(pai.rank)
            for c in cache:
                str += c.__str__() + pai.type

    return str


def str2PaiList(str):
    paiList = []
    cache = []
    for c in str:
        if c == 'm' or c == "s" or c == "p" or c == "d" or c == "w":
            for i in cache:
                paiList.append(Pai(i.__str__() + c))
            cache.clear()
        else:
            cache.append(c)
    return paiList


def test():

    example = []
    hand = PaiSet(str = "12s2d56p89m1w")
    hand.shuffle()
    print(hand.getStr())
    hand.sort()
    print(hand.getStr())


test()