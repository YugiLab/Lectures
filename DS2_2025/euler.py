y = 1.0
t = 0.0
delta_t = 0.01
endtime = 1.0

k = - 0.8	

while t <= endtime :
    print(t,"\t",y)
    dydt = k * y
    delta_y = dydt * delta_t
    y = y + delta_y
    t = t + delta_t
