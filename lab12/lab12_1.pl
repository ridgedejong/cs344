% Exercise 12.1

% a.
% i.
killer(Butch).
% - Butch is an argument of the functor killer to define a property of Butch.
married(mia,marsellus).
% - married is a functor that takes 2 arguments to define that mia and marsellus are married in this case.
dead(zed).
% - zed is an argument of the functor dead to define a property of zed.
kill(X,marsellus):- footmassage(X,mia).
% - kill is a functor of 2 arguments so that we can involve 2 people the killer and the killed. Marsellus is given
% because it is known that he is doing the killing, and a variable is also given because we do not know who is killed.
% Footmassage is a functor with 2 arguments: a variable who gives a footmassage and mia who receieves it. There is an "if"
% statement here because marsellus will kill the same person X who gives mia a footmassage.
loves(Y,mia):- dancer(Y).
% - loves is a functor with 2 arguments to define 2 people in love. Mia is given because she is loving the unknown
% person Y. There is an "if" statement with the functor dancer (with the same variable) because mia loves anyone who is
% a good dancer.
eat(Z,jules):- tasty(Z); nutritious(Z).
% - eat is a functor that takes 2 arguments: jules eating and the variable being eaten. There is an "if" statement
% before the functors tasty and nutritious (with same variable) because jules will eat anything that has the property of
% being tasty or nutritious. A semicolon is between these functors because Z can be tasty OR nutritious.

/**
ii.
1. True because ron is defined as being a wizard in the representation.
2. False because there is nothing involves witches in the representation.
3. False because there is nothing about hermoine in the representation.
4. False because there is nothing about hermoine in the representation.
5. True because the if statement after wizard(X) is true for harry. Harry is defined has having a wand so that
statement is true, and him playing quidditch implies that he has a broom making the second statement true, therefore
he is a wizard.
6. ron (then harry if prompted) because it will find the first atom that satisfies the property of being a wizard.
7. False because there is no functor witch.

b. Yes it implements modus ponens. For example, if listens2Music(mia) is in the representation and so is the statement
playsAirGuitar(mia):-  listens2Music(mia), then if the query playsAirGuitar(mia) is asked, Prolog will respond true.
Prolog uses modus ponens to infer playsAirGuitar(mia) based on the other statements without specifically being told
that playsAirGuitar is a property of mia.

c. Horn clauses simplify the implementation of representation of logic statements, making them easier to use in Prolog.
However, horn clauses can only have at most 1 positive literal which limits the representational power it can
provide. Conversely, propositional logic can use any number of positive literals giving it more representational power,
however it does not have the power of horn clauses where 2 resolved horn clauses become another horn clause.

d. Yes if there is a ?- at the beginning of the line you are in query mode where you can only ask questions about
the KB. However, you can also enter into consult mode where this ?- disappears and you can now tell Prolog facts.

*/