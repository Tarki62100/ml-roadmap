from re import X
import sympy as sy
from sympy import sin,pi
x,y = sy.symbols("x y")
f = x**3 + 2*x*sin(x)
print(sy.diff(f,x))
g = 3*x**2*y + y**3
g_derx = sy.diff(g,x)
g_dery = sy.diff(g,y)

gradient = (g_derx,g_dery)
print("Gradient Vector:",gradient)

