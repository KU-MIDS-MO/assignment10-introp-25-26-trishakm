import sympy as sp

x, y, r = sp.symbols('x y r', real=True)

eq1 = 2*x**2 + 3*y**2 - r
eq2 = y - (2*x + 1)

solutions = sp.solve((eq1, eq2), (x, y), dict=True)

sol = solutions

sol
pass
