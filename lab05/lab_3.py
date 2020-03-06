from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From a two-cause happiness example
happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1}),
    ])

# Compute P(Raise | Sunny).
print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())
# Compute P(Raise | Happy and Sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())
# Compute P(Raise | Happy)
print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
# Compute P(Raise | Happy and Sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())

"""
There is a 1% chance there was a raise if it's sunny. It makes sense that this is the same as the original raise
probability because Raise and Sunny are independent variables that cannot influence each other.
There is a 1.42% chance there was a raise if it's sunny and you're happy. It makes sense that this is slightly higher
than the original raise probability because there's a small chance that the reason you're happy is due to a raise.
There is a 1.85% chance there was a raise if you're happy. It makes sense that this is slightly higher than the last
calculation because instead of the sunny being 100% true it is now only 70% true, which means the probability that 
you're happy because of the sun is smaller and therefore the probability you're happy because of a raise is higher.
There is a 8.33% chance there was a raise when you're happy and it's not sunny. The reason this is so much higher
is similar to the previous explanation. Except now the sun is 0% true, meaning there is a much better chance that
you're happy because of a raise.
"""