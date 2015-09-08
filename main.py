# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:25:39 2015

@author: aaronoswald
"""

import pandas as pd
import collegeStructure

cs = collegeStructure.collegeStructure()
eloHistory = pd.DataFrame(columns = [["year","week"]+cs.findTeams()])
eloHistory.loc[0] = 1500
totalWeek = 1
collegeHistory = range(1950,2012)

for year in collegeHistory:
    season = pd.read_csv("{0}.csv".format(year))
    weeks = season.loc[:,"Week"]
    for week in set(weeks.tolist()):
        #Copy previous week
        eloHistory.loc[totalWeek] = eloHistory.loc[totalWeek-1]
        #Update Parameters
        eloHistory.loc[totalWeek]["week"] = week
        eloHistory.loc[totalWeek]["year"] = year
        
        #Extract Week As Temporary Dataframe
        games = season.query('Week == {0}'.format(week))
        
        #Update According to Games Played
        for game in range(games.shape[0]):
            winner = games.iloc[game]["Winner"]
            winner_pts = games.iloc[game]["Winner_Pts"]
            loser = games.iloc[game]["Loser"]
            loser_pts = games.iloc[game]["Loser_Pts"]
            winner_previous_elo = eloHistory.loc[totalWeek-1][winner]
            loser_previous_elo = eloHistory.loc[totalWeek-1][loser]
            spread = winner_pts - loser_pts
            eloUpdateTuble = cs.elo(winner_previous_elo,loser_previous_elo,spread,-spread)
            print "{0} played {1} and won by {2} in {3}, week {4}".format(winner,loser,spread, year, week)
            
            eloHistory.loc[totalWeek][winner] = eloUpdateTuble[0]
            eloHistory.loc[totalWeek][loser] = eloUpdateTuble[1]
        totalWeek = totalWeek + 1

eloHistory.to_csv("Elo History.csv")
        
    