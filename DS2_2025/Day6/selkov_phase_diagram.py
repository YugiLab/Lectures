import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy import re

# 変数と定数
x, y, a, b = sp.symbols("x y a b", real=True, positive=True)

f = -x + a * y + x**2 * y
g =  b - a * y - x**2 * y

# ヌルクラインと固定点
solutions = sp.solve( [ -x + a * y + x**2 * y , b - a * y - x**2 * y ]  , ( x , y ) )
fix_x , fix_y = solutions[0]

# ヤコビ行列
J_sym = sp.Matrix( [ [ f.diff( x ) , f.diff( y ) ] , [ g.diff( x ) , g.diff( y ) ] ] )

# 相図を描く
a_grid = np.linspace( 0, 0.15, 15 )
b_grid = np.linspace( 0, 1.0, 10 )
[A, B] = np.meshgrid( a_grid , b_grid )

for a_val , b_val in zip( A.flatten() , B.flatten() ):
    J_num = J_sym.subs( [ ( x , fix_x ) , ( y , fix_y ) , ( a , a_val ), ( b , b_val ) ] )
    eig1, eig2 = J_num.eigenvals().keys()

    if          : # eig1 が実数ならば if 節に入る
        if eig1 < 0 and eig2 < 0 : # 実数・安定
            plt.plot( a_val , b_val , 'ko' ) 
        else : # 実数・不安定
            plt.plot( a_val , b_val , 'ko' , fillstyle='none') 
    else :
        if         : # eig1 の実部が負であれば if 節に入る。すなわち複素数・安定の場合。
            plt.plot( a_val , b_val , 'ro' ) 
        else : # 複素数・不安定
            plt.plot( a_val , b_val , 'ro' , fillstyle='none') 

# 振動するパラメータと振動しないパラメータの位置関係を表示
oscillation_a = 0.06
oscillation_b = 0.6
stable_a = 0.14
plt.plot( oscillation_a , oscillation_b , 'b+', ms=20)
plt.plot( stable_a , oscillation_b , 'g+', ms=20)
            
plt.show()

