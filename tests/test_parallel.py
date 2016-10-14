import math

from mcsim.parallel import replicate
from mcsim.examples.pi import pi_chain, pi_approximate

def test_parallel_pi():
    nsim = 1000
    nreps = 8
    njobs = 4

    approximations = replicate(pi_chain, nsim, nreps, njobs, transformer=pi_approximate)
    assert abs(sum(approximations)/nreps - math.pi) < 0.1


