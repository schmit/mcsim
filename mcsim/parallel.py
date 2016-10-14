import copy
from joblib import Parallel, delayed

import mcsim.core

def identity(x):
    return x

def simulate(chain, nsim, config={}, initial_state={}, transformer=identity):
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
    return Parallel(n_jobs=njob)(
            delayed(simulate)(
                chain,
                nsim,
                config,
                initial_state,
                transformer
            )
            for _ in range(nrepeat))
