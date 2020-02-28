'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden, Ridge DeJong
@version Jan 1, 2013
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())

#Compute P(Cavity|catch=T)
"""
This calculation was first done by hand so that the program solution could be confirmed.
The equations and steps taken can be found on the submitted sheet under 1b. 
"""
PCc = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PCc.show_approx())

# Probability distribution function for the flipping of 2 coins
P2 = JointProbDist(['coin1', 'coin2'])
# True = Heads, False = Tails
P2[T, T] = 0.25; P2[T, F] = 0.25
P2[F, T] = 0.25; P2[F, F] = 0.25

# Compute P(coin2|coin1=heads)
P2c = enumerate_joint_ask('coin1', {'coin2': T}, P2)
print(P2c.show_approx())
"""The result of this is 0.5, which makes sense because 2 coin flips are independent variables,
so the result of the first coin flip should not influence the result of the second coin flip, and this proves that.
This helps explain why the full joint probability distribution is not commonly used, because not all random variables
that it includes influence each other, diminishing its usefulness."""