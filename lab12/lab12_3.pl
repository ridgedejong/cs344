% Exercise 12.3

% Monty Python Witch Logic.

weightofduck(woman).
floats(X):- weightofduck(X).
madeofwood(X):- floats(X).
witch(X):- madeofwood(X).

% This representation proves that the woman is a witch.

