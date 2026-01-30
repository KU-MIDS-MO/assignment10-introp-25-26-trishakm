import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x, y = sp.symbols('x y', real=True)

r_val = 10

ellipse = 2*x**2 + 3*y**2 - r_val
line = y - (2*x + 1)

ellipse_func = sp.lambdify((x, y), ellipse, 'numpy')
line_func = sp.lambdify(x, 2*x + 1, 'numpy')

x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x_vals, y_vals)

sol_num = sp.solve(
    (2*x**2 + 3*(2*x + 1)**2 - r_val),
    x
)

intersection_points = [(float(s), float(2*s + 1)) for s in sol_num]

plt.figure(figsize=(6, 6))

plt.contour(X, Y, ellipse_func(X, Y), levels=[0])

plt.plot(x_vals, line_func(x_vals))

for px, py in intersection_points:
    plt.plot(px, py, 'o')

plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.xlim(-3, 3)
plt.ylim(-3, 3)

plt.savefig("/Users/Trisha/Desktop/Problem2.pdf")
plt.show()


pass
