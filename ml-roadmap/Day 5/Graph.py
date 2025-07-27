import matplotlib.pyplot as plt
import sympy
import numpy as np
from sympy import sin,pi
from sympy.abc import x
x = sympy.symbols("x")
f = x**3 + x*2*sin(x)
fr= sympy.lambdify(x,f)
plt.xlabel("x")
plt.ylabel("Function")
x_axis = np.arange(-5,5,1.)
y=fr(x_axis)
der_f= sympy.diff(f,x)
der_fr= sympy.lambdify(x,der_f)
der_at_2 = x*der_fr(2) - 12.67082530762286
der_at_2r = sympy.lambdify(x,der_at_2)
plt.plot(x_axis,der_at_2r(x_axis))
plt.plot(x_axis,y)
plt.legend(["Derivative at 2","Normal"])
plt.tight_layout()
plt.show()
