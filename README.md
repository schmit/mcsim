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

## Examples

### Approximate pi

Here a simple example that shows how to approximate pi using monte carlo simulation
using this little framework

```python
from mcsim import simulate
import random

def generate_xy(state, config, log):
    return {"x": random.random(), "y": random.random()}

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

### Random walk

Now consider a slightly more complex example,
where we want to simulate a random walk with 10 steps starting at 0.
Hence, we really do need to keep track of the state.

```python
from mcsim import simulate, unzip_dict
from mcsim.examples.random_walk import random_step

# x indicates our location
simulate([random_step], 10, initial_state={"x": 0})
```

Suppose we are interested in the (empirical) distribution of the location after 10 steps.
Then we want to repeat the simulation many times.
This is easily run in parallel.
In the following example, we repeat the simulation 20 times,
and use 4 jobs to parallelize the computation.

```python
from mcsim.parallel import replicate

def last_location(simulation):
    """
    Return the last location of the random walk
    """
    return simulation[-1]["x"]

replicate([random_step], 10,
    nrepeat=20, njob=4,
    initial_state={"x": 0},
    transformer=last_location)
```

