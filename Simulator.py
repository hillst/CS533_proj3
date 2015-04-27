#!/usr/bin/env python
import sys
from Arm import Arm
from Bandit import Bandit
from BanditAlgorithm import *

def main():
    if len(sys.argv) < 3:
        print_usage()
        exit()
    num_pulls = int(sys.argv[1])
    goal = int(sys.argv[2])
    arms = [ Arm(arm.split(",")) for arm in sys.argv[3:] ]
    bandit = Bandit(arms)
    alg = IncrementalUniformBandit(num_pulls, bandit)
    print "NOTE: cumulative regret is incorrect right now"
    print "uniform simple regret", alg.get_simple_regret()
    print "uniform cumulative regret", alg.get_cum_regret()
    print "uniform best arm", alg.get_best_arm()
    alg = UCBBandit(num_pulls, bandit)
    print "ucb simple regret", alg.get_simple_regret()
    print "ucb cumulative regret", alg.get_cum_regret()
    print "ucb best arm", alg.get_best_arm()


def print_usage():
    print >> sys.stderr, "Specify some number of pulls, a goal, and the distributio of each arm"
    print >> sys.stderr, "Simulator.py\t<num_pulls>\t<goal?>\t<prob1,reward1>\t<prob2,reward2>..."

if __name__ == "__main__":
    main()
