#!/usr/bin/env python2.7

from __future__ import division

import pprint

import constraint
import termcolor

GOOD = 0
EVIL = 1

players = list(range(1, 11))
players_evil = 4
players_good = len(players) - players_evil

problem = constraint.Problem()

# Every player is good or evil
problem.addVariables(players, [GOOD, EVIL])

# There are always an exact number of evil players
problem.addConstraint(constraint.ExactSumConstraint(players_evil))

# Assume no evil players if a mission passes
mission_passed = known_good_player = constraint.ExactSumConstraint(GOOD)

# Assume at most 1 evil player if the 4th mission passes
mission_4_passed = constraint.MaxSumConstraint(EVIL)

# Know at least 1 evil player is on every failed mission
mission_failed = known_evil_player = constraint.MinSumConstraint(EVIL)

# problem.addConstraint(known_good_player, [1])

# The following is a simulated game
# Players 1, 2, 3, 4 are evil, but we don't "know" this
problem.addConstraint(mission_failed, [1, 2, 3])
problem.addConstraint(mission_failed, [1, 5, 6, 7])
problem.addConstraint(mission_passed, [5, 6, 7, 8])
# problem.addConstraint(mission_4_passed, [4, 5, 7, 8, 6])


solutions = problem.getSolutions()

print len(solutions), "possible solutions"

if not solutions:
    exit(1)

if len(solutions) < 10:
    pprint.pprint(solutions)

player_total = {i: 0 for i in players}

for solution in solutions:
    for player, alignment in solution.iteritems():
        player_total[player] += alignment

player_probability = {player: (t / len(solutions)) for player, t in player_total.items()}

print "Probabilities:"

for player, p in player_probability.items():
    if p == 0:
        color = "grey"
    elif p > 0.75:
        color = "red"
    else:
        color = "white"
        
    print "  {:02}: {}".format(player, termcolor.colored("{:.2f}".format(p), color))
