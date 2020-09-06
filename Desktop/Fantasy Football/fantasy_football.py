#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:04:21 2020

@author: devinpowers
"""
import requests

scores = {}
for week in range(1, 17):
    r = requests.get('http://games.espn.com/ffl/api/v2/scoreboard', 
                     params={'leagueId': 123456, 'seasonId': 2017, 'matchupPeriodId': week})
    scores[week] = r.json()
    

df = []
for key in scores:
    temp = scores[key]['scoreboard']['matchups']
    for match in temp:
        df.append([key, 
                   match['teams'][0]['team']['teamAbbrev'],
                   match['teams'][1]['team']['teamAbbrev'],
                   match['teams'][0]['score'],
                   match['teams'][1]['score']])