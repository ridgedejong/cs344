'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden, Ridge DeJong
@version Jan 1, 2013
'''

from probability import JointProbDist, enumerate_joint_ask

"""Edited: now includes a new random variable Rain which can take on values rain or not rain"""
# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch', 'Rain'])

"""The full joint probability distribution now contains 16 entries instead of 8 because a new variable was introduced,
so the initial entries exist for the possibility of rain and the possibility of not rain.
These entries still add up to 1.0 because it still holds true that every possibility in this world must be a fraction
of all the possibilities. In order to maintain the total at 1.0 from the initial joint probability distribution, every
entry value was divided by 2.
I think technically other values besides True and False could be used for the values of random variables, however it
would make everything more difficult since the comparisons in the solution couldn't simply be tested as True or False,
but would have to be compared to specific values.
The values that I chose for the other variables as a result of rain indicates that Rain is independent of the other
variables. By dividing every entry exactly by 2, I was implying that the addition of the rain condition would not
change the probabilities of the other variables relative to each other. The values of the other variables when it rains
are exactly the same for when it does not rain, thus being independent of rain.
"""
T, F = True, False
P[T, T, T, T] = 0.054; P[T, T, F, T] = 0.006
P[F, T, T, T] = 0.036; P[F, T, F, T] = 0.004
P[T, F, T, T] = 0.008; P[T, F, F, T] = 0.032
P[F, F, T, T] = 0.072; P[F, F, F, T] = 0.288
P[T, T, T, F] = 0.054; P[T, T, F, F] = 0.006
P[F, T, T, F] = 0.036; P[F, T, F, F] = 0.004
P[T, F, T, F] = 0.008; P[T, F, F, F] = 0.032
P[F, F, T, F] = 0.072; P[F, F, F, F] = 0.288

# Compute <P(Toothache|rain), P(-Toothache|rain), P(Toothache|-rain), P(-Toothache|-rain)>
"""
Hand calculations were also done to test the accuracy of the program.
These calculations can be found on the sheet turned in.
"""
print('With Rain:')
print('False = -Toothache; True = Toothache')
PC1 = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print(PC1.show_approx())
print('\nWithout Rain:')
print('False = -Toothache; True = Toothache')
PC2 = enumerate_joint_ask('Toothache', {'Rain': F}, P)
print(PC2.show_approx())


