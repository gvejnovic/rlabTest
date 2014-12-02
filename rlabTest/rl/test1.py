__author__ = 'Goran Vejnovic'
import re
from collections import OrderedDict


def readfile():
    """Reading file, put in dict, sort and print"""
    words = open('words.txt', 'r')
    wordict = {}
    for line in words:
        line = re.sub("[^a-zA-Z]+", "", line).lower()
        if line in wordict:
            wordict.update({line: (wordict.get(line) + 1)})
        else:
            wordict.update({line: 1})

    wordictsorted = OrderedDict(sorted(wordict.items(), key=lambda t: t[1], reverse=True)) #sortiraj desc po key
    for key, value in wordictsorted.items():
        if value > 1:
            print(key + " " + str(value))

readfile()