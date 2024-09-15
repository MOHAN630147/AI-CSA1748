match([],[]).
match([H1|T1],[H2|T2]):-
H1=H2,
match(T1,T2).
match([|T1],[|T2]):-
match(T1,T2).
match([a,b,c],Pattern):-
match([a,b,c],Pattern).
