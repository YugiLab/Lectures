import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def ozbudak_model( t , init , *param ):
    x = init[ 0 ]
    y = init[ 1 ]

    [ alpha , beta , rho , x_out ] = param
    
    dxdt = 
    dydt = 
    
    return [ dxdt , dydt ] 


init = [ 0 , 0 ]
t_span = [ 0 , 30 ]
t_eval = np.linspace( t_span[0] , t_span[1] , 300 )

alpha = 0.1
beta = 10
rho = 25
x_out = 5

param = [ alpha , beta , rho , x_out ]

solution = solve_ivp( ozbudak_model, t_span, init , t_eval=t_eval , method='RK45', args=param )

TMG = solution.y[0]
LacY = solution.y[1]

plt.plot( solution.t , TMG )
plt.plot( solution.t , LacY ) 
plt.show()
