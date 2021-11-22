import os
import random
import time

import numpy as np
import yaml

with open(os.path.join('./results.yaml'), 'r') as f:
    results = yaml.safe_load(f)

options = {
    'Burger King': 1,
    'McDonald': 1,
    'Guofu Yang': 1,
    'QingFeng': 1,
    'King Yonghe': 1,
    'Try some new': 0.5,
    'Order takeout': 0.5,
}

probability = np.array(list(options.values()))
correction = 1 / np.array(list(results.values()))
weights = probability * correction

random.seed(time.time())
res = random.choices(population=list(options.keys()), weights=weights, k=1)[0]

results[res] += 1

print(f'Let\'s to go eat: {res}')

with open(os.path.join('./results.yaml'), 'w+') as f:
    yaml.dump(results, f)
