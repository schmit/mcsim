import random

def generate_xy(state, config, log):
    return {"x": random.random(), "y": random.random()}

def check_in_circle(state, config, log):
    circle = False
    if state["x"]**2 + state["y"]**2 < 1:
        circle = True
    log["circle"] = circle
    return state

def pi_approximate(out):
    nsim = len(out)
    return 4 * sum(o["circle"] for o in out) / nsim

pi_chain = [generate_xy, check_in_circle]

