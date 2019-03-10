import pycuber as pc
from pycuber.solver import CFOPSolver

array_default = '000000000111111111222222222333333333444444444555555555'

array = 'yyyrggowwbyogybgoyrygoorrwrggbbwgwwooowwbrwrybbryrbbog'

cube_default = pc.Cube()

cubie = pc.array_to_cubies(array)

cube_main = pc.Cube(cubie)

cube_main

solver = CFOPSolver(cube_main)

steps = solver.solve()
#print(len(steps))