'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden, Ridge DeJong
@version Jan 2, 3/3/2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Burglary | John and Mary both call).
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.

# Compute P(Alarm | burglary and -earthquake)
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# Compute P(John calls | burglary and -earthquake)
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# Compute P(Burglary | Alarm)
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
# Compute P(Burglary | John and Mary both call)
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

"""
Alternate computations for P(Burglary | John and Mary both call) could use rejection sampling, likelihood estimate,
and Gibbs sampling. Rejection sampling works by generating samples from the prior distribution, then rejecting the 
ones that don't match the evidence, and counting how many desired states are found in the remaining cases. This leads
to a close estimate of the exact inference algorithms, and finally converges to the exact probability if given enough
samples. Likelihood estimate differs by only generating samples that are consistent with the evidence, and then weights
each event by the likelihood that the event accords to the evidence. The problem is that this estimate ignores the 
evidence of the child variable when sampling a variable, causing it to give a slight variation from the exact inference
algorithms. Gibbs sampling works by fixing evidence variables at their observed states, then systematically (or
randomly) generating new states by randomly sampling a value for one of the non-evidence variables. This method can
eventually match the true posterior distribution if it is allowed to generate enough samples. 
"""