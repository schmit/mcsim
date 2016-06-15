def simulate_one(chain, initial_state={}):
    """
    Simulate a chain once

    Args:
        - chain: an iterable with functions of type
            f(state, log) -> new_state
        - initial_state: initial state to start every simulation with,
            useful to pass configuration parameters

    Returns:
        Dictionary with the log
    """
    state = initial_state
    log = {}
    for link in chain:
        state = link(state, log)

    return log

def simulate(chain, nsim, initial_state={}):
    """
    Simulate a chain of functions a number of times and aggregate the logs.

    Each function in the chain can write to the log to record outcomes.
    Note that the state is not saved: everything needs to be looged explicitly.
    The helper function log_state can be used to log the state

    Args:
        - chain: an iterable with functions of type
            f(state, log) -> new_state
        - nsim: number of simulations to perform
        - initial_state: initial state to start every simulation with,
            useful to pass configuration parameters

    Returns:
        List with the log of each simulation
    """
    assert hasattr(chain, '__contains__'), "Chain needs to be iterable"
    assert nsim > 0, "nsim > 0"

    return [simulate_one(chain, initial_state) for _ in range(nsim)]

def log_state(state, log):
    """
    Log the current state
    """
    log.update(state)
    return state

