import sympy as sp

x, y, a, b = sp.symbols("x y a b", real=True, positive=True)

a_val = 0.06
b_val = 0.6

f = -x + a * y + x**2 * y
g =  

# ヌルクラインと固定点
solutions = sp.solve( [       ,       ]  , ( x , y ) )
fix_x , fix_y = solutions[0]

# ヤコビ行列
J_sym = sp.Matrix( [ [ f.diff( x ) ,         ] , [         , g.diff( y ) ] ] )
J_num = J_sym.subs( [ ( x ,     ) , ( y ,     ) , ( a , a_val ), ( b , b_val ) ] ) 

print( J_sym )
print( J_num )
print( J_num.       )


