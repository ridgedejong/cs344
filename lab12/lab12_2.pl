/** Exercise 12.2

a.
i.
1. True
2. False
8. True, X=bread.
9. True, X=sausage, Y=bread.
14. False.

ii.
1. False
2. False
3. False
4. True, X='McGonagall'
5. True, Hermoine=dobby

Prolog does its unification through this reasoning. It reads the knowledge base and tries to find to unify a functor
and argument to either a fact or the head of a rule. It works top to bottom to find the first solution it can to make
the query true. When Prolog unifies the variable in a query to a variable in a fact or rule, it generates a brand new
variable to represent the shared variables. It then makes goals based on the body of the rule because if the body is
true then the head is true. It then works systematically like a top-down graph where it tries a solution that fulfils
one goal and sees if it fulfils the other goals. It tries this with the possible values of the goals and eventually
return false if it cannot find a solution and true if it can.

b. Yes inference uses unification because the whole reason that a statement can be inferred is only if 2 statements
unify. The advantage of this unification is that it combines 2 overlapping general rules.

c. Prolog inferences using resolution because it makes a new clause by resolving 2 clauses that contain a
complimentary literal. This is advantageous as it simplifies the logic by cutting out an extra step in the analysis.

*/