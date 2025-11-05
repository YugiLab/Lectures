import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def selkov_model( t , init , *param ):
    x = init[ 0 ]
    y = init[ 1 ]
    
    [ a , b ] = param


    v1 = 
    v2 = 
    v3 = 
    
    dxdt = v2 - v3
    dydt = v1 - v2
    
    return [ dxdt , dydt ] 


init = [ 1.0 , 1.0 ]
t_span = [ 0 , 100 ]
t_eval = np.linspace( t_span[0] , t_span[1] , 10000 )

a = 0.06
b = 0.6

param = [ a , b ]

solution = solve_ivp( selkov_model, t_span, init, t_eval=t_eval, method='RK45', args=param )

ADP = solution.y[0]
F6P = solution.y[1]

plt.plot( , , 'k-')

x = np.linspace( 0, 3, 100 )
x_null = x / ( a + x**2 ) # The nullcline for dydt 
y_null = # The nullcline for dydt 

plt.plot( x , x_null , 'r-')
plt.plot( , , 'b-')
plt.show()
