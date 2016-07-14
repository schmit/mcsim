from functools import wraps

def log_state(state, config, log):
    """
    Log the current state
    """
    log.update(state)
    return state

def unzip_dict(list_of_dicts):
    """
    Converts a list of dictionaries to a dictionary of lists.

    Useful to transform the outcomes of a simulation
    """
    return {key: [d[key] for d in list_of_dicts] for key in list_of_dicts[0]}

"""
Decorators that make it less cumbersome to write a function that
generates one update to the state
"""

def withState(name):
    """
    Decorates such that return value gets stored in state[name]

    Instead of writing:
    def f(state, config, log):
        [...]
        state[name] = x
        return state

    we can write
    @withState(name)
    def f(state, config, log):
        [...]
        return x
    """
    def decorator(method):
        @wraps(method)
        def wrapped_method(state, config, log):
            out = method(state, config, log)
            state[name] = out
            return state

        return wrapped_method

    return decorator

def withLogging(name):
    """
    Decorates such that return value gets logged in log[name]

    Instead of writing:
    def f(state, config, log):
        [...]
        log[name] = x
        return state

    we can write
    @withLogging(name)
    def f(state, config, log):
        [...]
        return x
    """
    def decorator(method):
        @wraps(method)
        def wrapped_method(state, config, log):
            out = method(state, config, log)
            log[name] = out
            return state

        return wrapped_method

    return decorator

def withStateAndLogging(name):
    """
    Decorates such that return value gets stored in state[name] and logged in log[name]

    Instead of writing:
    def f(state, config, log):
        [...]
        state[name] = x
        log[name] = x
        return state

    we can write
    @withStateAndLogging(name)
    def f(state, config, log):
        [...]
        return x
    """
    def decorator(method):
        @wraps(method)
        def wrapped_method(state, config, log):
            out = method(state, config, log)
            state[name] = out
            log[name] = out
            return state

        return wrapped_method

    return decorator

