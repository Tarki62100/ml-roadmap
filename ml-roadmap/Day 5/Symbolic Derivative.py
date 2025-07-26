import numpy as np
import matplotlib.pyplot as plt
import sympy 
from sympy.abc import x
x = sympy.symbols("x")
h = np.e**(-20)
f = x**2
f_ap= sympy.lambdify(x,f)
f_der = (f_ap(x+h) - f_ap(x-h))/(2*h)
f_derp = sympy.lambdify(x,f_der)
f_actual_der =sympy.lambdify(x,sympy.diff(f,x))
print(f_derp(3)-f_actual_der(3))
