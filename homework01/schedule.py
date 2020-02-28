
from csp import *

def schedule():
    # Return a CSP formulation of a scheduling problem
    variables = ['cs108', 'cs112', 'cs212', 'cs214', 'cs262', 'cs344']

    # Create the domains for every class variable, with the possible values being time and room
    domains = {}
    for var in variables:
        domains[var] = [['mwf800', 'nh253'],['mwf900', 'nh253'],['mwf1030', 'nh253'],['mwf1130', 'nh253'],['mwf800', 'sb382'],['mwf900', 'sb382'],['mwf1030', 'sb382'],['mwf1130', 'sb382']]

    # Explicitly assign faculty to specific classes to ensure each one only teaches one class, and to reduce the
    # total number of possible domains for each variable
    for i in range(8):
        domains['cs108'][i].append('schuurman')
        domains['cs112'][i].append('adams')
        domains['cs212'][i].append('adams')
        domains['cs214'][i].append('norman')
        domains['cs262'][i].append('norman')
        domains['cs344'][i].append('vanderlinden')

    # The neighbors for each variable are all the other variables (not itself)
    neighbors = {'cs108': ['cs112', 'cs212', 'cs214', 'cs262', 'cs344'], 'cs112': ['cs108', 'cs212', 'cs214', 'cs262', 'cs344'], 'cs212': ['cs108', 'cs112', 'cs214', 'cs262', 'cs344'], 'cs214': ['cs108', 'cs112', 'cs212', 'cs262', 'cs344'], 'cs262': ['cs108', 'cs112', 'cs212', 'cs214', 'cs344'], 'cs344': ['cs108', 'cs112', 'cs212', 'cs214', 'cs262']}

    # Define the constraints that the solution must meet
    def schedule_constraint(A, a, B, b):

        # each class cannot be offered more than once (more than one state)
        if A == B:
            return False
        if A != B:
            # if both the time and faculty are the same for 2 variables, it is not a solution because faculty cannot
            # teach 2 classes at the same time
            if a[0] == b[0] and a[1] == b[1]:
                return False
            # if both the time and room are the same for 2 variables, it is not a solution because the same room
            # cannot be used by 2 classes at the same time
            if a[0] == b[0] and a[2] == b[2]:
                return False
            # if the constraints are satisfied, a solution has been found
            return True

    return CSP(variables, domains, neighbors, schedule_constraint)

# use AIMA search algorithm to solve the problem
solution = min_conflicts(schedule(), max_steps=10000)

# display the solution if one was found
if solution != None:
    print("Solution:\n")
    print(solution)
else:
    print("Failed: solution returned None")
