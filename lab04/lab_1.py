'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden, Ridge DeJong
@version Jan 1, 2013
'''

from probability import JointProbDist, enumerate_joint_ask, ProbDist

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
PCc = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PCc.show_approx())

# Probability distribution function for the flipping of 2 coins
P2 = ProbDist(['coin1', 'coin2'])
# True = Heads, False = Tails
T, F = True, False
P[T, T] = 0.25; P[T, F] = 0.25
P[F, T] = 0.25; P[F, F] = 0.25

# Compute P(coin2|coin1=heads)
P2 = enumerate_joint_ask('coin1', {'coin2': T}, P2)
print(P2.show_approx())
