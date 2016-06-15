def simulate_one(chain, config={}):
    """
    Simulate a chain once

    Args:
        - chain: an iterable with functions of type
            f(state, log) -> new_state
        - config: pass configuration parameters in a dictionary
    Returns:
        Dictionary with the log
    """
    state = {}
    log = {}
    for link in chain:
        state = link(state, config, log)

    return log

def simulate(chain, nsim, config={}):
    """
    Simulate a chain of functions a number of times and aggregate the logs.

    Each function in the chain can write to the log to record outcomes.
    Note that the state is not saved: everything needs to be looged explicitly.
    The helper function log_state can be used to log the state

    Args:
        - chain: an iterable with functions of type
            f(state, config, log) -> new_state
        - nsim: number of simulations to perform
        - config: pass configuration parameters in a dictionary

    Returns:
        List with the log of each simulation
    """
    assert hasattr(chain, '__contains__'), "Chain needs to be iterable"
    assert nsim > 0, "nsim > 0"

    return [simulate_one(chain, config) for _ in range(nsim)]

def log_state(state, config, log):
    """
    Log the current state
    """
    log.update(state)
    return state

