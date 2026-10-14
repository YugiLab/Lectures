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

def hysteresis_timeseries():
    init = [ 0 , 0 ]
    t_span = [ 0 , 60 ]

    alpha = 0.1
    beta = 10
    rho = 25
    x_out = 10

    param = [ alpha , beta , rho , x_out ]

    solution = solve_ivp( ozbudak_model, t_span, init , method='RK45', args=param )
    
    t = solution.t
    TMG = solution.y[0]
    LacY = solution.y[1]

    plt.plot( t , TMG )
    plt.plot( t , LacY ) 

    ##
    ## Repeat after elimitating TMG_out (x_out)
    ##
    
    x_init = 
    y_init = 
    init = [ x_init , y_init ]
    
    x_out = 
    param = [ alpha , beta , rho , x_out ]
    
    t_span = [ 60 , 120 ]
    
    solution = solve_ivp( ozbudak_model, t_span, init , method='RK45', args=param )

    t = solution.t
    TMG = solution.y[0]
    LacY = solution.y[1]
    
    plt.plot( t , TMG , color='tab:blue')
    plt.plot( t , LacY , color='tab:orange') 
    plt.show()

hysteresis_timeseries()
