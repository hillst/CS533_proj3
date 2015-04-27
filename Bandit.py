#!/usr/bin/env python

class Bandit:

    """
    Arms should just be a list of tuples (p_a, r_a). These tuples represent the probability (p_a) of getting a rewarad (r_a). Otherwise 0.

    Arms are implemented as a class with a reward function, a probability function, and a pull function.
    """
    def __init__(self, arms):
        self.arms = arms
        pass

    def get_arms(self):
        return self.arms

    def get_num_arms(self):
        return len(self.arms)

    def pull_arm(self, a):
        return self.arms[a].pull()

    def get_optimal(self):
        arm_evs = [ arm.get_expected_value() for arm in self.arms ]
        best = max( arm_evs )
        return arm_evs.index(best)
