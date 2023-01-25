import random
import time

def randomizer(x):
    random.shuffle(x)
    return random.choice(x)

def importing(x):
    with open(x, 'r') as f:
        return f.read().splitlines()

def sleeper(x):
    time.sleep(x)
    return
