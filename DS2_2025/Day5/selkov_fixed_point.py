import sympy as sp

# 変数と定数
x = sp.Symbol('x')
y = sp.Symbol('y')

a = 0.06
b = 0.6

# ヌルクライン
f = x / ( a + x**2 )
g = b / ( a + x**2 )

# 交点の x 座標を求める。交点の x 座標は f = g となる x
x_solutions = sp.solve( sp.Eq( f , g ) , x )

print(x_solutions)

