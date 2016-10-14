from mcsim.utility import *

def test_log_state():
    assert False, "Write test"

def test_unzip_dict():
    test_in = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    test_out = unzip_dict(test_in)
    assert test_out == {"a": [1, 3], "b": [2, 4]}


def test_withLogging():
    def cumbersome(state, config, log):
        new_x = state["x"] + 1
        log["new_x"] = new_x
        return state

    @withLogging("new_x")
    def simple(state, config, log):
        return state["x"] + 1

    log_cumbersome = {}
    log_simple = {}

    cumbersome({"x": 1}, {}, log_cumbersome)
    simple({"x": 1}, {}, log_simple)
    assert log_cumbersome == log_simple, "Logs don't match"

def test_withState():
    def cumbersome(state, config, log):
        new_x = state["x"] + 1
        state["new_x"] = new_x
        return state

    @withState("new_x")
    def simple(state, config, log):
        return state["x"] + 1

    new_cumbersome = cumbersome({"x": 1}, {}, {})
    new_simple = simple({"x": 1}, {}, {})
    assert new_cumbersome == new_simple, "States don't match"

def test_withStateAndLogging():
    def cumbersome(state, config, log):
        new_x = state["x"] + 1
        state["new_x"] = new_x
        log["new_x"] = new_x
        return state

    @withStateAndLogging("new_x")
    def simple(state, config, log):
        return state["x"] + 1

    log_cumbersome = {}
    log_simple = {}

    new_cumbersome = cumbersome({"x": 1}, {}, log_cumbersome)
    new_simple = simple({"x": 1}, {}, log_simple)
    assert log_cumbersome == log_simple, "Logs don't match"
    assert new_cumbersome == new_simple, "States don't match"

