% Facts representing the planets and their characteristics
planet(mercury, rocky, 0.39, 88).
planet(venus, rocky, 0.72, 225).
planet(earth, rocky, 1, 365).
planet(mars, rocky, 1.52, 687).
planet(jupiter, gas_giant, 5.2, 4333).
planet(saturn, gas_giant, 9.58, 10759).
planet(uranus, ice_giant, 19.22, 30687).
planet(neptune, ice_giant, 30.05, 60190).

% Query to get information about a specific planet
planet_info(Name, Type, Distance, OrbitDays) :-
    planet(Name, Type, Distance, OrbitDays).

% Query to find rocky planets
rocky_planet(Name) :-
    planet(Name, rocky, _, _).

% Query to find gas giant planets
gas_giant_planet(Name) :-
    planet(Name, gas_giant, _, _).

% Query to find ice giant planets
ice_giant_planet(Name) :-
    planet(Name, ice_giant, _, _).
