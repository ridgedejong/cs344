from search import Problem, hill_climbing, simulated_annealing, exp_schedule
import itertools
import math
import random


class TSP(Problem):
    """An implementation of Travelling Salesman Problem for local search. This uses the AIMA
    hill climbing and simulated annealing local search algorithms.

    State representation:
        [0, ..., n, ..., 0] gives the path visiting all of the cities
    Move representation:
        [random_index, random_index]: Gives 2 random indices in the state that will be swapped
    """

    def __init__(self, cities, distances, initial):
        self.cities = cities
        self.distances = distances
        self.initial = initial

    def actions(self, state):
        """Actions returns a list that contains a list of random indices to be swapped
        """
        actions = []
        swap1 = random.randint(1, len(self.cities)-1)
        swap2 = random.randint(1, len(self.cities)-1)
        t = [swap1, swap2]
        actions.append(t)
        return actions

    def result(self, state, move):
        """Makes the given move on a copy of the given state."""
        new_state = state[:]
        new_state[move[0]] = state[move[1]]
        new_state[move[1]] = state[move[0]]
        return new_state

    def value(self, state):
        """This method computes a value of given state based on the sum of
        all the distances between cities travelled.
        """
        value = 0
        j = 1
        for i in range (0, len(self.cities)):
            value += self.distances[(state[i], state[j])]
            i += 1
            j += 1
        return -1 * value



if __name__ == '__main__':

    # Set the city
    cities = (0,1,2,3,4,5,6,7,8,9,10)
    distances = {(0,1):1, (0,2):2, (0,3):4, (0,4):3, (0,5):6, (0,6):2, (0,7):5, (0,8):7, (0,9):4, (0,10):9, (1,0):1, (1,2):5, (1,3):3, (1,4):8, (1,5):1, (1,6):5, (1,7):4, (1,8):8, (1,9):5, (1,10):2, (2, 0): 2, (2,1):5, (2,3):2, (2,4):6, (2,5):2, (2,6):3, (2,7):6, (2,8):9, (2,9):1, (2,10):4,(3,0):4, (3,1):3, (3,2):2, (3,4):5, (3,5):2, (3,6):8, (3,7):2, (3,8):5, (3,9):1, (3,10):8, (4, 0):1, (4,1):2, (4, 2):2, (4, 3):4, (4, 4):3, (4, 5):6, (4, 6):2, (4, 7):5, (4, 8):7, (4, 9):4, (4, 10):9,(5, 0):3, (5, 1):3, (5, 1):5, (5, 2):7, (5, 3):9, (5, 4):2, (5, 5):5, (5, 6):8, (5, 7):1, (5, 8):4, (5, 9):7, (5, 10):8,(6, 0):4, (6,1):3, (6, 2):7, (6, 3):4, (6, 4):2, (6, 5):9, (6, 6):6, (6, 7):4, (6, 8):2, (6, 9):5, (6, 10):7,(7, 0):2, (7, 1):6, (7, 2):4, (7, 3):2, (7, 4):7, (7, 5):8, (7, 6):4, (7, 7):2, (7, 8):1, (7, 9):8, (7, 10):4,(8, 0):3, (8,1):5, (8, 2):8, (8, 3):4, (8, 4):2, (8, 5):3, (8, 6):7, (8, 7):8, (8, 8):4, (8, 9):2, (8, 10):1,(9, 0):7, (9, 1):5, (9, 2):2, (9, 3):8, (9, 4):3, (9, 5):4, (9, 6):5, (9, 7):3, (9, 8):9, (9, 9):6, (9, 10):7, (10, 0):3, (10, 1):3, (10,1):5, (10, 2):7, (10, 3):9, (10, 4):2, (10, 5):1, (10, 6):6, (10, 7):4, (10, 8):6, (10, 9):8, (10, 10):3}
    # print(cities)

    # Initialize a path using numerical order
    path = [0,1,2,3,4,5,6,7,8,9,10,0]

    # Initialize the TSP problem
    p = TSP(cities, distances, path)
    print("Initial Path:", path)

    # Solve the problem using hill climbing.
    hill_solution = hill_climbing(p)
    print('\nHill-climbing:')
    print('\tSolution:\t' + str(hill_solution))
    print('\tValue:\t\t' + str(p.value(hill_solution)))

    # Solve the problem using simulated annealing.
    annealing_solution = \
        simulated_annealing(p, exp_schedule(k=20, lam=0.005, limit=10000))
    print('\nSimulated annealing:')
    print('\tSolution:\t' + str(annealing_solution))
    print('\tValue:\t\t' + str(p.value(annealing_solution)))
