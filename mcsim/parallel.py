import copy
from joblib import Parallel, delayed

import mcsim.core

def identity(x):
    """ Identity function: returns its input """
    return x

def _simulate(chain, nsim, config={}, initial_state={}, transformer=identity):
    """
    Helper function to streamline replicate.
    Creates deep copies of config and initial state,
    and applies transformer to output.
    """
    out = mcsim.core.simulate(chain,
            nsim,
            copy.deepcopy(config),
            copy.deepcopy(initial_state)
            )
    return transformer(out)

def replicate(chain, nsim,
        nrepeat, njob=1,
        config={}, initial_state={},
        transformer=identity):
    """
    Replicate simulation multiple times, while dividing up the work across jobs.

    Args:
        - chain, nsim, config, initial_state:
            see documentation for simulate
        - nrepeat:
            number of replicas to generate
        - njob (default: 1):
            number of jobs to use
        - transformer (default: identity):
            how to transform the output of a simulation,
            if you are only interested in a certain outcome,
            this can reduce memory size of the output.

    Returns:
        List with nrepeat outputs of the simulation defined by
        chain, nsim, config and initial_state
    """
    return Parallel(n_jobs=njob)(
            delayed(_simulate)(
                chain,
                nsim,
                config,
                initial_state,
                transformer
            )
            for _ in range(nrepeat))
