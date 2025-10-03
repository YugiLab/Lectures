import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def f( t , s0 , Vmax1 , Km1 , Vmax2 , Km2 ):
    S1 = s0[ 0 ]
    S2 = s0[ 1 ]
    
    v1 = Vmax1 * S1 / ( Km1 + S1 )
    v2 = 
    
    ds1dt = - v1
    ds2dt = 
    return [ ds1dt , ds2dt ] 

s0 = [ 2.0E-3 , 0 ]
t_span = [0, 30]
t_eval = np.linspace( t_span[0] , t_span[1] , 100 )

Vmax1 = 1.0E-3
Km1 = 1.0E-3

Vmax2 = 1.0E-4
Km2 = 2.0E-4

solution = solve_ivp( f, t_span, s0 , t_eval=t_eval , method='RK45', args=( Vmax1 , Km1 , Vmax2 , Km2 ) )

plt.plot( solution.t , solution.y[0] )
plt.plot( solution.t , solution.y[1] ) 
plt.show()
