"""
Ridge DeJong
CS 344
Homework 2.2

This problem uses the domain from Figure 14.12 of the AIMA text. The full joint probability distribution for
this domain has 2^4 - 1 = 15 independent values if no conditional independence. This is because there are 4
variables that each have 2 possible states, but they must all sum to 1 which removes an independent value.
The number of independent values for the Bayesian network of this domain is different because it implies that
Sprinkler and Rain depend on Cloudy, and in turn WetGrass depends on Sprinkler and Rain. Therefore, Cloudy has
1 independent value, Sprinkler and Rain both have 2 based on the value of Cloudy, and WetGrass has 4 based on the
value of Sprinkler and Rain, resulting in a total of 9 independent values, which is much better than the
original 15 independent values in the full joint probability distribution.
"""

from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

# From AIMA - Fig. 14.12
weather = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.1, F: 0.5}),
    ('Rain', 'Cloudy', {T: 0.80, F: 0.20}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.90, (F, T): 0.90, (F, F): 0.0})
    ])

# Compute P(Cloudy).
print(enumeration_ask('Cloudy', dict(), weather).show_approx())
# Compute P(Sprinkler | cloudy).
print(enumeration_ask('Sprinkler', dict(Cloudy=T), weather).show_approx())
# Compute P(Cloudy | the sprinkler is running and it's not raining).
print(enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), weather).show_approx())
# Compute P(WetGrass | it's cloudy, the sprinkler is running and it's raining).
print(enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), weather).show_approx())
# Compute P(Cloudy | grass is not wet).
print(enumeration_ask('Cloudy', dict(WetGrass=F), weather).show_approx())