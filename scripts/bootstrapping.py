#!/usr/bin/python3

import numpy as np
import random


# Generate Random Data
x = np.random.normal(loc= 300.0, size=1000)
print(np.mean(x))

means = []
for i in range(1000):
  y = random.sample(x.tolist(), 1)
  avg = np.mean(y)
  means.append(avg)

print(np.mean(means))
