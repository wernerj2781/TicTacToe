__author__ = 'Jeff Werner'

#Calling this an "AI" is a misnomer (It is an AI without the I). It is really just randomly selecting spaces that are available.
#But as far as Proof of Concept work goes, it does the job of having a non-human selecting spaces.
#So it serves its purpose by selecting a space on the non-human's turn.

import random
import time
import json

class AI_Level_One:
    def __init__(self, name):
        self.name = name

    #data should have existing spaces by each player accounted for, and inform the AI if it is X or O
    def select_space(self, data):
        location = self.analyze(data)
        return location

    def analyze(self, data):
        #figure out what is not taken
        spaces = self.getAvailableSpaces(data)
        length = len(spaces)
        if(length == 1):
            return spaces[0]
        #below is a placeholder
        location = random.randrange(0,length - 1)
        ##print("location: " + str(location) + " - space:  " + str(spaces[location]))
        return spaces[location]

    def getAvailableSpaces(self, data):
        available = {}
        counter = 0
        space = 0
        for dat in data:
            if dat ==  "-":
                available[space] = counter
                space += 1
            counter += 1
        return available
