% Exercise 3.2 LPN!

directlyIn(natasha, irina).
directlyIn(olga, natasha).
directlyIn(katarina, olga).
in(A,C):- directlyIn(A,C).
in(A,C):- directlyIn(B,C), in(A,B).

% Exercise 4.5 LPN!

tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).
listtran([],[]).
listtran([Hg|Tg],[He|Te]):- tran(Hg,He),
			 listtran(Tg,Te).

/**
b. Yes, Prolog implements a generalized modus ponens. If there is a rule involving a variable, and a fact about the
head of the rule, then Prolog will apply Modus Ponens by instatiating the variable and applying the fact to the body.
For example, if there is the rule person(X):-mortal(X), and also the fact person(socrates), then Prolog will
automatically know the fact mortal(socrates).
*/
