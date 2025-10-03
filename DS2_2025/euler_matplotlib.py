import matplotlib.pyplot as plt

y = 1.0
t = 0.0
delta_t = 0.01
endtime = 1.0

k = - 0.8	

y_list = [ y ]
t_list = [ t ]

while t <= endtime :
    dydt = k * y
    delta_y = dydt * delta_t
    y = y + delta_y 
    t = t + delta_t

    y_list.append( y )
    t_list.append( t )

plt.plot( t_list , y_list )
plt.show()
