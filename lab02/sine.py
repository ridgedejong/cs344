"""
This module implements local search on a sine function variant.
The function is not a linear function  with a single, discontinuous max value
(see the sine function variant in graphs.py).

@author: kvlinden, ridgedejong
@version 6feb2013
"""
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search, simulated_annealing_full
from random import randrange
import math
import numpy
import array


class SineVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return abs(x * math.sin(x))


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and many local maxima.
    maximum = 30.0
    initial = randrange(0, maximum)
    p = SineVariant(initial, maximum, delta=1.0)
    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    # Solve the problem using hill-climbing.
    temp1 = 0.0
    counter1 = 0
    hill_solution = hill_climbing(p)
    while hill_solution != maximum:
        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=1.0)
        print(hill_solution)
        hill_solution = hill_climbing(p)
        temp1 += p.value(hill_solution)
        counter1 += 1
    print('Hill-climbing solution       x: ' + str(hill_solution)
          + '\tvalue: ' + str(p.value(hill_solution))
          )
    if counter1 != 0:
        print("average: " + str(temp1/counter1))

    # Solve the problem using simulated annealing.
    temp2 = 0.0
    counter2 = 0
    annealing_solution = simulated_annealing(p, exp_schedule(k=20, lam=0.005, limit=1000))
    while annealing_solution != maximum:
        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=1.0)
        print(annealing_solution)
        annealing_solution = simulated_annealing(p, exp_schedule(k=20, lam=0.005, limit=1000))
        temp2 += p.value(annealing_solution)
        counter2 += 1
    print('Simulated annealing solution x: ' + str(annealing_solution)
          + '\tvalue: ' + str(p.value(annealing_solution))
          )
    if counter2 != 0:
        print("average: " + str(temp2/counter2))