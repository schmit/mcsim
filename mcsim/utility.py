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
    return {key: [d[key] for d in list_of_dicts] for key in list_op_dicts[0]}

