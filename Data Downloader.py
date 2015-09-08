# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:03:59 2015

@author: aaronoswald
"""

import mechanize
import cookielib
import BeautifulSoup
import html2text
from bs4 import BeautifulSoup
import pandas as pd
from time import time

br = mechanize.Browser()

collegefootball = range(1950,2014)
y = 0
for year in collegefootball:
    start = time()
    colllege = 'http://www.sports-reference.com/cfb/years/{0}-schedule.html'.format(year)
    html_doc =  br.open(colllege).read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.table
    x=0
    df = pd.DataFrame(columns=('Rank','Week','Date','Day','Winner','Winner_Pts',"At","Loser","Loser_Pts","Notes"))
    for row in table.findAll('tr')[1:]:
        if row.attrs["class"] == ['no_ranker', 'thead']:
            #print ""
            y = 2+y
        else:
            #Rk	Wk	Date	Day	Winner/Tie	Pts		Loser/Tie	Pts	Notes
            col = row.findAll('td')
            rank = col[0].string
            week = col[1].string
            date =col[2].string
            day = col[3].string
            if len(col[4]) == 2:
                winner =col[4].a.string
            else:
                 winner =col[4].string
            winner_pts =col[5].string
            if len(col[7]) == 2:
                loser =col[7].a.string
            else:
                 loser =col[7].string
            at = col[6].string
            loser_pts = col[8].string
            notes = col[9].string
            
            df.loc[x] = [rank, week, date, day, winner, winner_pts,at,loser,loser_pts,notes]
            x = x +1        
            
    df.to_csv("{0}.csv".format(year))
    print "{0} took {1} seconds.".format(year, time()-start)
   