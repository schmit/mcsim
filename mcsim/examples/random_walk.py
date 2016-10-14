import random

from mcsim import *

def rademacher():
    if random.random() > 0.5:
        return -1
    return 1

@withStateAndLogging("x")
def random_step(state, config, log):
    return state["x"] + rademacher()


