import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def f( t , y ):
    k = 0.01
    dydt = - k * y 
    return dydt

y0 = [ 1.0 ]
t_span = [0, 350]
t_eval = np.linspace( t_span[0] , t_span[1] , 100 )

solution = solve_ivp( f, t_span, y0 , t_eval=t_eval , method='RK45')

plt.plot( solution.t , solution.y[0] )
plt.show()
