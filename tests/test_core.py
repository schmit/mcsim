from mcsim.core import *

def identity(state, log):
    return state

def test_empty_chain():
    """
    Test that empty chain returns empty dictionary
    """
    log = simulate_one([])
    assert log == {}

def test_initial_state():
    """
    Test that initial state works
    """
    initial_state = {"x": 1}
    log = simulate_one([log_state], initial_state=initial_state)
    assert log == initial_state

def test_simple_chain():
    log = simulate_one(
            [ lambda state, log: 1
            , lambda state, log: state
            ]
            , {}
        )

    assert log == {}

def test_simulate():
    outcome = simulate([], 10)
    assert len(outcome) == 10
