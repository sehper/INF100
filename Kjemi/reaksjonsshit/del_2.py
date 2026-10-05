import numpy as np
from scipy import stats

R = 8.314  # J/(mol·K)

# Målinger
t = np.array([8*60 + 12, 5*60 + 53, 40], dtype=float)  # s
temp = np.array([0, 10, 40], dtype=float)              # °C

# Anslått måleusikkerhet (juster til det som passer for deg)
sigma_t = 2.0     # s, f.eks. reaksjonstid ved stoppeklokke
sigma_T = 0.5     # K, termometer

def arrhenius(t, temp):
    T = temp + 273.15
    x = 1 / T
    y = np.log(1 / t)          # ln k, med k = 1/t
    res = stats.linregress(x, y)
    return res, x, y

res, x, y = arrhenius(t, temp)
n = len(x)

Ea = -res.slope * R
se_Ea = res.stderr * R
t_krit = stats.t.ppf(0.975, n - 2)   # 95 % konfidensintervall

print(f"Stigningstall = {res.slope:.1f} ± {res.stderr:.1f} K")
print(f"Ea = {Ea/1000:.1f} ± {se_Ea/1000:.1f} kJ/mol  (standardfeil fra regresjon)")
print(f"95 % KI: ± {t_krit*se_Ea/1000:.0f} kJ/mol  (t = {t_krit:.2f}, df = {n-2})")
print(f"R² = {res.rvalue**2:.4f}")

# Ln A fra skjæringspunktet
print(f"ln A = {res.intercept:.2f} ± {res.intercept_stderr:.2f}")

# Monte Carlo: propager målefeil i tid og temperatur
rng = np.random.default_rng(1)
N = 20000
Eas = np.empty(N)
for i in range(N):
    t_s = t + rng.normal(0, sigma_t, n)
    T_s = temp + rng.normal(0, sigma_T, n)
    r, _, _ = arrhenius(t_s, T_s)
    Eas[i] = -r.slope * R

print(f"Ea (Monte Carlo, kun målefeil) = {Eas.mean()/1000:.1f} ± {Eas.std(ddof=1)/1000:.1f} kJ/mol")