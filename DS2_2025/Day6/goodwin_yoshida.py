import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def goodwin_model( t , init , *param ):
    v = init[ 0 ]
    u = init[ 1 ]
    
    [ alpha , beta , gamma , rho , sigma ] = param
    
    dvdt = ( ( 1.0 / sigma - ( alpha + beta )  ) - u / sigma ) * v
    dudt = ( - ( alpha + gamma ) + rho * v ) * u
    
    return [ dvdt , dudt ] 


init = [ 0.06 , 0.92 ]
t_span = [ 0 , 500 ]
t_eval = np.linspace( t_span[0] , t_span[1] , 10000 )

alpha = 0.02   # 技術進歩率
beta = 0.01    # 労働人口成長率
gamma = 0.01   # 賃金上昇の自然減衰項
rho = 0.5      # フィリップス曲線の感応度
sigma = 2.0    # 投資係数

param = [ alpha , beta , gamma , rho , sigma ]

solution = solve_ivp( goodwin_model, t_span, init, t_eval=t_eval, method='RK45', args=param )

v , u = solution.y

plt.figure()
plt.plot( solution.t , v )
plt.plot( solution.t , u ) 
plt.show()

plt.figure()
plt.plot( v , u )
plt.show()
