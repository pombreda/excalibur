#!/usr/bin/env python3.2

good = 1
evil = 0

players = {i: None for i in range(10)}
players[0] = good

good_players = 6
evil_players = 4

print(players)

for player, alignment in players.items():
    if alignment == good:
        good_players = good_players - 1
    elif alignment == evil:
        evil_players = evil_players - 1
    else:
        players[player] = evil_players / (good_players + evil_players)
        
for player, alignment in players.items():
    print("Player {}: {:.2f}".format(player, alignment))
