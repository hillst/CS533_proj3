#!/usr/bin/env python
from math import log
from math import sqrt
class BanditAlgorithm:
    def __init__(self, n_pulls, bandit):
        self.bandit = bandit
        self.n_pulls = n_pulls
        self.pulls = [0 for i in range(bandit.get_num_arms())]
        self.rewards = [0 for i in range(bandit.get_num_arms())]
        pass
    """
    Returns the current best arm available
    """
    def best_arm(self):
        pass

    """
    Suggests an arm to be pulled on the next iteration. Not necessarily the "best". This is where the algorithmic work is done.
    """
    def suggest_arm(self):
        pass

    #expected regret is the "best" arm (We can cheat) * n - our current reward
    def get_cum_regret(self):
        #still does not work
        #what we need to do is track the expected reward of an arm when we choose it, that way we can track cumulative regret, which involves expected value
        return self.bandit.get_optimal() * self.n_pulls - sum(self.rewards)

    def get_simple_regret(self):
        return self.simple_regret

    def get_best_arm(self):
        return self.best_arm

class IncrementalUniformBandit(BanditAlgorithm):

    def __init__(self, n_pulls, bandit):
        BanditAlgorithm.__init__(self, n_pulls, bandit)
        self.run()

    def run(self):
        for i in range(self.n_pulls):
            current_arm = i % self.bandit.get_num_arms()
            self.pulls[current_arm] += 1
            self.rewards[current_arm] += self.bandit.pull_arm(current_arm)
        means = [ self.rewards[i]/float(self.pulls[i] ) for i in range(len(self.rewards))]
        m = max( means )
        self.best_arm = means.index(m)
        self.simple_regret = m
        #self.cum_regret = sum(self.rewards)/self.bandit.get_num_arms()
    
class UCBBandit(BanditAlgorithm):
    
    def __init__(self, n_pulls, bandit):
        BanditAlgorithm.__init__(self, n_pulls, bandit)
        self.run() 

    def run(self):
        for i in range(1, self.n_pulls + 1):
            to_pull = self.suggest_arm(i)
            self.rewards[to_pull] += self.bandit.pull_arm(to_pull)
            self.pulls[to_pull] += 1
        means = [ self.rewards[i]/float(self.pulls[i]) for i in range(len(self.rewards))]
        m = max( means )
        self.best_arm = means.index(m)
        self.simple_regret = m
        #self.cum_regret = sum(self.rewards)/self.bandit.get_num_arms()

    def suggest_arm(self, t):
        ucb_choice = []
        for arm in range(self.bandit.get_num_arms()):
            n_a = self.pulls[arm]
            try:
                q_a = self.rewards[arm] / n_a 
                ucb = q_a +  sqrt(2 * log(t) / n_a)
            except ZeroDivisionError:
                ucb = 1000000000 #force this oe
            ucb_choice.append(ucb)
        best = ucb_choice.index(max(ucb_choice))
        return best
