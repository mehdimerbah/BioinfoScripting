#!/usr/bin/python3

import numpy as np
import random


# Generate Random Data
x = np.random.normal(loc= 300.0, size=1000)
print(np.mean(x))

means = []
for i in range(50):
  y = random.sample(x.tolist(), 4)
  avg = np.mean(y)
  means.append(avg)

print(np.mean(means))
