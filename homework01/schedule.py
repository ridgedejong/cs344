import time


from csp import *
from collections import defaultdict


def print_solution(result):
    """A CSP solution printer copied from csp.py."""
    for h in range(1, 7):
        print('Class', h)
        for (var, val) in result.items():
            if val == h: print('\t', var)


def schedule():
    """Return an instance of the Schedule Puzzle."""
    variables = ['cs108', 'cs112', 'cs212', 'cs214', 'cs262', 'cs344']
    faculty = 'schuurman adams norman vanderlinden'.split()
    time = 'mwf800 mwf900 mwf1030 mwf1130'.split()
    room = 'nh253 sb382'.split()
    domains = {}
    for var in variables:
        domains[var] = [faculty, time, room]



    # neighbors = parse_neighbors("""Englishman: Red;
    #             Spaniard: Dog; Kools: Yellow; Chesterfields: Fox;
    #             Norwegian: Blue; Winston: Snails; LuckyStrike: OJ;
    #             Ukranian: Tea; Japanese: Parliaments; Kools: Horse;
    #             Coffee: Green; Green: Ivory""", variables)

    neighbors = {'cs108': ['cs112', 'cs212', 'cs214', 'cs262', 'cs344'], 'cs112': ['cs108', 'cs212', 'cs214', 'cs262', 'cs344'], 'cs212': ['cs108', 'cs112', 'cs214', 'cs262', 'cs344'], 'cs214': ['cs108', 'cs112', 'cs212', 'cs262', 'cs344'], 'cs262': ['cs108', 'cs112', 'cs212', 'cs214', 'cs344'], 'cs344': ['cs108', 'cs112', 'cs212', 'cs214', 'cs262']}
    # for A in ['cs108', 'cs112', 'cs212', 'cs214', 'cs262', 'cs344']:
    #     for B in ['cs108', 'cs112', 'cs212', 'cs214', 'cs262', 'cs344']:
    #         if A != B:
    #              if B not in neighbors[A]:
    #                 neighbors[A].append(B)
    #              if A not in neighbors[B]:




    def schedule_constraint(A, a, B, b, recurse=0):
        same = (a == b)
        next_to = abs(a - b) == 1

        # each class cannot be offered more than once (more than one state)
        if A == B:
            return False
        if A != B:
            if a == b and A[0] == B[0]:
                return


        if a == 'sb382' and b == 'sb382':
            return False
       # if domains[A]

        if A == 'Englishman' and B == 'Red':
            return same
        if A == 'Spaniard' and B == 'Dog':
            return same
        if A == 'Chesterfields' and B == 'Fox':
            return next_to
        if A == 'Norwegian' and B == 'Blue':
            return next_to
        if A == 'Kools' and B == 'Yellow':
            return same
        if A == 'Winston' and B == 'Snails':
            return same
        if A == 'LuckyStrike' and B == 'OJ':
            return same
        if A == 'Ukranian' and B == 'Tea':
            return same
        if A == 'Japanese' and B == 'Parliaments':
            return same
        if A == 'Kools' and B == 'Horse':
            return next_to
        if A == 'Coffee' and B == 'Green':
            return same
        if A == 'Green' and B == 'Ivory':
            return a - 1 == b
        if recurse == 0:
            return schedule_constraint(B, b, A, a, 1)
        if ((A in Colors and B in Colors) or
                (A in Pets and B in Pets) or
                (A in Drinks and B in Drinks) or
                (A in Countries and B in Countries) or
                (A in Smokes and B in Smokes)):
            return not same
        raise Exception('error')
    return CSP(variables, domains, neighbors, schedule_constraint)

def parse_neighbors(neighbors, variables=None):
    """Convert a string of the form 'X: Y Z; Y: Z' into a dict mapping
    regions to neighbors. The syntax is a region name followed by a ':'
    followed by zero or more region names, followed by ';', repeated for
    each region name. If you say 'X: Y' you don't need 'Y: X'.
    >>> parse_neighbors('X: Y Z; Y: Z') == {'Y': ['X', 'Z'], 'X': ['Y', 'Z'], 'Z': ['X', 'Y']}
    True
    """
    dic = defaultdict(list)
    specs = [spec.split(':') for spec in neighbors.split(';')]
    for (A, Aneighbors) in specs:
        A = A.strip()
        for B in Aneighbors.split():
            dic[A].append(B)
            dic[B].append(A)
    return dic

puzzle = schedule()

# result = depth_first_graph_search(puzzle)
# result = AC3(puzzle)
result = backtracking_search(puzzle)
# result = min_conflicts(puzzle, max_steps=1000)

if puzzle.goal_test(puzzle.infer_assignment()):
    print("Solution:\n")
    print_solution(result)
else:
    print("failed...")
    print(puzzle.curr_domains)
    puzzle.display(puzzle.infer_assignment())