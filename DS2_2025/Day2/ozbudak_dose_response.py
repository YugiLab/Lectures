import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def ozbudak_model( t , init , *param ):
    x = init[ 0 ]
    y = init[ 1 ]

    [ alpha , beta , rho , x_out ] = param

    dxdt = -x + alpha * x_out + beta * y
    dydt =  x**2 / ( rho + x**2 ) - y
    
    return [ dxdt , dydt ] 

def ozbudak_dose_response( x_out , y_init , marker ):
    init = [ 0 , y_init ]
    t_span = [ 0 , 60 ]

    alpha = 0.1
    beta = 10
    rho = 25

    param = [ alpha , beta , rho , x_out ]

    solution = solve_ivp( ozbudak_model, t_span, init , method='RK45', args=param )
    
    LacY = solution.y[1]
    y_end =
    
    plt.plot( x_out , y_end , marker , fillstyle='none') 

    return 
    
##
## Main
##

y_init = 0
for x_out in range(11):
    y_init = ozbudak_dose_response( x_out , y_init , 'ko' )

for x_out in reversed( range(11) ):
    

plt.show()
