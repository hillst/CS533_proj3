#!/usr/bin/env python
from random import random

class Arm:
    def __init__(self, (p_a, r_a)):
        self.p_a = float(p_a)
        self.r_a = float(r_a)

    def get_probability(self):
        return self.p_a

    def get_reward(self):
        return self.r_a

    def get_expected_value(self):
        return self.r_a * self.p_a

    def pull(self):
        pull = random()
        if pull < self.p_a: return self.r_a
        else: return 0
        
