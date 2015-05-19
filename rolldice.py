import random

def rollDie(sides,numdie = 1):
    """
    Simulates rolling numdie dice with sides number of sides, and returns the 
    result
    """
    result = 0
    for i in range(numdie):
        try:
           result += random.randint(1,sides)
        except(ValueError):
           pass

    return result
