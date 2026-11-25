"""
Blahut–Arimoto アルゴリズムで通信路容量を計算する（講義5 演習9 の続き）

    C = max_{P(x)} I(X ; Y)

X: NGF の用量（入力）、Y: CREB の区間（出力）
W[x, y] = P(Y = y | X = x) : 通信路行列（各行の和は 1）
"""
import numpy as np


def mutual_information(p, W):
    """入力分布 p と通信路行列 W から I(X;Y) [bit] を計算"""
    r = p @ W                                   # 出力の分布 r(y)
    I = 0.0
    for x in range(W.shape[0]):
        for y in range(W.shape[1]):
            if p[x] > 0 and W[x, y] > 0:        # 0·log(…) = 0 として扱う
                I += p[x] * W[x, y] * np.log2(W[x, y] / r[y])
    return I


def blahut_arimoto(W, tol=1e-6, max_iter=1000, verbose=True):
    n_in = W.shape[0]
    p = np.ones(n_in) / n_in                    # 0. はじめは等確率
    for t in range(max_iter):
        r = p @ W                               # 1. 出力の分布
        D = np.zeros(n_in)                      # 2. 各用量の D(x)
        for x in range(n_in):
            m = W[x] > 0
            D[x] = np.sum(W[x, m] * np.log2(W[x, m] / r[m]))
        lower = np.log2(np.sum(p * 2 ** D))     # C の下限
        upper = D.max()                         # C の上限
        if verbose:
            print(f"{t:3d}  P(x) = {np.round(p, 3)}  {lower:.4f} <= C <= {upper:.4f}")
        if upper - lower < tol:
            break
        p = p * 2 ** D                          # 3. 更新して
        p = p / p.sum()                         #    合計 1 に割り直す
    return lower, p


if __name__ == "__main__":
    # 行: NGF 低・中・高、列: CREB 低・中・高
    W = np.array([[0.75, 0.25, 0.00],
                  [0.25, 0.50, 0.25],
                  [0.00, 0.25, 0.75]])

    print("演習7  等確率のとき I =", round(mutual_information(np.ones(3) / 3, W), 3), "bit")
    print("演習8  (1/2, 0, 1/2) のとき I =", round(mutual_information(np.array([.5, 0, .5]), W), 3), "bit\n")

    C, p_opt = blahut_arimoto(W)
    print(f"\n通信路容量 C = {C:.3f} bit,  最適な入力分布 P(x) = {np.round(p_opt, 3)}")
