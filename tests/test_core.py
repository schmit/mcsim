from mcsim.core import *
from mcsim.utility import log_state


def config_to_state(state, config, log):
    state = {}
    state.update(config)
    return state

def test_empty_chain():
    """
    Test that empty chain returns empty dictionary
    """
    log = simulate_one([])
    assert log == {}

def test_config():
    """
    Test that initial state works
    """
    config = {"x": 1}
    log = simulate_one([config_to_state, log_state], config=config)
    assert log == config

def test_simple_chain():
    log = simulate_one(
            [ lambda state, config, log: 1
            , lambda state, config, log: state
            ]
            , {}
        )

    assert log == {}

def test_simulate():
    outcome = simulate([], 10)
    assert len(outcome) == 10

def test_simulate_lazy():
    assert False, "Write test"
