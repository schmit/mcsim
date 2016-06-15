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

## Example

Here a simple example that shows how to approximate pi using monte carlo simulation
and this little framework

```
from mcsim import simulate
import random

def generate_xy(s, log):
    """ generate a random point in [0, 1]^2 """
    s["x"] = random.random()
    s["y"] = random.random()
    return s

def check_in_circle(s, log):
    """ Check whether the generated point is in circle with radius 1 """
    circle = False
    if s["x"]**2 + s["y"]**2 < 1:
        circle = True
    log["circle"] = circle
    return s

nsim = 5000
out = simulate([generate_xy, check_in_circle], nsim)

# We note that the area of a unit circle is pi / 4
approx_pi = 4 * sum(o["circle"] for o in out) / nsim
print("pi is approximately {}".format(approx_pi))
```
