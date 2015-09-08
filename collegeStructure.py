# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:16:54 2015

@author: aaronoswald
"""

import pandas as pd

class collegeStructure():
    def elo(self, winnerElo, loserElo, winnerPoints, loserPoints):
        
        ExpectedA = 1/ (1+pow(10,(loserElo - winnerElo)/400))
        if ExpectedA > 0:
            ExpectedB = 1 - ExpectedA
        else:
            ExpectedB = .5
            ExpectedA = .5
        k = 3
        print "{0} + {1} = {2}".format(ExpectedA,ExpectedB,ExpectedA+ExpectedB)
        updatedA = winnerElo + k*(winnerPoints-ExpectedA)
        updatedB = loserElo + k*(loserPoints-ExpectedB)
        
        return (updatedA,updatedB)
        
    def findTeams(self):
        league = []
        for year in range(1950,2014):
            df = pd.read_csv("{0}.csv".format(year))
            for x in range(df.shape[0]):
                winner = df.loc[x]['Winner']
                if winner not in league:
                    league.append(winner)
                loser = df.loc[x]['Loser']
                if loser not in league:
                    league.append(loser)
        print "Number of teams: {0}".format(len(league))
        return league