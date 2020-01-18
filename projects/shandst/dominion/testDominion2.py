# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:16:00 2020

@author: Travis Shands
"""

import Dominion
from dominion import testUtility

# Get player names
player_names = testUtility.GetPlayers()

# number of curses and victory cards
nV, nC = testUtility.SetNumVC(player_names)

# Define box
box = testUtility.GetBoxes(nV)
supply_order = testUtility.SetSupplyOrder()

# Pick 10 cards from box to be in the supply.
boxlist, supply = testUtility.GetSupplyCards(box)

# The supply always has these cards
testUtility.DefaultSupply(supply, player_names, nV, nC)

# initialize the trash
trash = []

# Costruct the Player objectsSmithy
players = []
testUtility.MakePlayers(players, player_names)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)
