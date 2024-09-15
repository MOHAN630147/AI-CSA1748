bird(canary,can_fly).
bird(sparrow,can_fly).
bird(ostrich,cant_fly).
bird_fly(name,nature):-
    bird(name,nature).