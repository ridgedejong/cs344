from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From a two-test cancer example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.20}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.20}),
    ])

# Compute P(Cancer | positive results on both tests).
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
# Compute P(Cancer | a positive result on test 1, but a negative result on test 2)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

"""
The first calculation (17% true when both tests positive) makes sense because both of the tests have a relatively
high chance of giving a false positive. Combining this with the overall very small chance of having cancer leads to 
a situation where even both positive tests still has a decently low chance of having cancer.
When one of the tests is negative, the chance of having cancer plummets from 17% to 0.6%. This also makes sense because
while the tests have a relatively high chance of a false positive, they have a much better chance of giving the correct
answer. So, when one of these tests is negative, the nature of its good accuracy causes the chance of cancer to drop
significantly. 
"""