"""
区間（ビン）の切り方で相互情報量の推定値が変わることを確かめる（講義5 発展）

真の値が分かる例：2 変数正規分布（相関 rho）の相互情報量は
    I = -1/2 * log2(1 - rho^2)
出力側だけ指数変換して、蛍光強度のように右に裾を引く分布にする。
（単調な変換なので、真の相互情報量は変わらない）
"""
import numpy as np


def entropy(p):
    p = p[p > 0]
    return -(p * np.log2(p)).sum()


def mi_binned(x, y, n_bins, equal_freq=False):
    """x, y を n_bins 個の区間に区切って相互情報量 [bit] を推定"""
    if equal_freq:   # 等頻度（分位点）で区切る
        ex = np.quantile(x, np.linspace(0, 1, n_bins + 1))
        ey = np.quantile(y, np.linspace(0, 1, n_bins + 1))
    else:            # 等幅で区切る
        ex = np.linspace(x.min(), x.max(), n_bins + 1)
        ey = np.linspace(y.min(), y.max(), n_bins + 1)
    P, _, _ = np.histogram2d(x, y, [ex, ey])
    P = P / P.sum()
    return entropy(P.sum(1)) + entropy(P.sum(0)) - entropy(P.ravel())


def simulate(rho=0.8, n_cells=1000, bins=(2, 3, 4, 5, 7, 10, 15, 20, 30, 40), reps=30, seed=0):
    rng = np.random.default_rng(seed)
    width = {b: [] for b in bins}
    freq = {b: [] for b in bins}
    for _ in range(reps):
        x = rng.normal(size=n_cells)
        y = np.exp(rho * x + np.sqrt(1 - rho ** 2) * rng.normal(size=n_cells))
        for b in bins:
            width[b].append(mi_binned(x, y, b))
            freq[b].append(mi_binned(x, y, b, equal_freq=True))
    return ({b: float(np.mean(v)) for b, v in width.items()},
            {b: float(np.mean(v)) for b, v in freq.items()})


if __name__ == "__main__":
    rho = 0.8
    print(f"真の相互情報量 = {-0.5 * np.log2(1 - rho ** 2):.3f} bit\n")
    for n in (100, 1000, 10000):
        w, f = simulate(rho=rho, n_cells=n)
        print(f"細胞数 {n}")
        print("  区間数 :", "  ".join(f"{b:5d}" for b in w))
        print("  等幅   :", "  ".join(f"{v:5.2f}" for v in w.values()))
        print("  等頻度 :", "  ".join(f"{v:5.2f}" for v in f.values()))
