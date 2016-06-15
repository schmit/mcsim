# MCSim

Simple framework for Monte Carlo simulations in Python3.

The idea is by adding some structure to how to conduct simulations,
it is much easier to create more intricate simulations that can easily be adapted
to different scenarios by adding and removing bits and pieces as desired.

## Setup

Clone and install using

```
pip3 install ./
```

## Motivation

Often I have to write some simulations for research and I try to write some nice code
that can easily be re-used.
However, time and time again the one change to do a different simulation requires
an a complete rewrite:
suddenly an extra parameter has to be passed down to a new function
which requires restructuring all code.

The idea of this little framework is to impose a simple structure on simulations
where each simulation is a bunch of transformations combined with some logging.
Hopefully that makes it much easier to change certain parts of the simulation
without any hassle.

## Example

Here a simple example that shows how to approximate pi using monte carlo simulation
and this little framework

```python
from mcsim import simulate
import random

def generate_xy(state, config, log):
    state["x"] = random.random()
    state["y"] = random.random()
    return state

def check_in_circle(state, config, log):
    circle = False
    if state["x"]**2 + state["y"]**2 < 1:
        circle = True
    log["circle"] = circle
    return state

nsim = 50000
out = simulate([generate_xy, check_in_circle], nsim)

approx_pi = 4 * sum(o["circle"] for o in out) / nsim
print("pi is approximately {}".format(approx_pi))
```

