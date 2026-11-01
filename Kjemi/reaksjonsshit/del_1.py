import numpy as np

# Stamløsninger (mol/L)
c0 = {"KI": 0.01, "BrO3": 0.04, "HCl": 0.1, "S2O3": 0.001}
V_tot = 50  # mL

# Volum (mL) av hver løsning (resten er vann) og målt tid (s)
forsok = [
    {"navn": "Referanse", "V": {"KI": 10, "BrO3": 10, "HCl": 10, "S2O3": 10}, "t": 2*60 + 58},
    {"navn": "2x KI",     "V": {"KI": 20, "BrO3": 10, "HCl": 10, "S2O3": 10}, "t": 60 + 19},
    {"navn": "2x BrO3",   "V": {"KI": 10, "BrO3": 20, "HCl": 10, "S2O3": 10}, "t": 60 + 27},
    {"navn": "2x HCl",    "V": {"KI": 10, "BrO3": 10, "HCl": 20, "S2O3": 10}, "t": 43},
]

# Konsentrasjoner i blandingen og hastighet (forbruk av BrO3-) per forsøk
for f in forsok:
    f["c"] = {s: c0[s] * f["V"][s] / V_tot for s in c0}
    f["v"] = f["c"]["S2O3"] / (6 * f["t"])   # mol/(L·s)

ref = forsok[0]

# Reaksjonsordener (m = KI, n = BrO3, p = HCl)
orden = {}
for navn, f in zip(["KI", "BrO3", "HCl"], forsok[1:]):
    orden[navn] = np.log(f["v"] / ref["v"]) / np.log(f["c"][navn] / ref["c"][navn])

m, n, p = orden["KI"], orden["BrO3"], orden["HCl"]
mr, nr, pr = round(m), round(n), round(p)

# k for hvert forsøk med avrundede ordener
for f in forsok:
    f["k"] = f["v"] / (f["c"]["KI"]**mr * f["c"]["BrO3"]**nr * f["c"]["HCl"]**pr)

ks = np.array([f["k"] for f in forsok])
k = ks.mean()
s = ks.std(ddof=1)  # standardavvik

print(f"m = {m:.2f}  (avrundet: {mr})")
print(f"n = {n:.2f}  (avrundet: {nr})")
print(f"p = {p:.2f}  (avrundet: {pr})")

print("\nKonsentrasjoner i blandingen (mol/L)")
print(f"{'Forsøk':<12}{'[KI]':>12}{'[BrO3-]':>12}{'[H+]/HCl':>12}{'[S2O3 2-]':>12}")
for f in forsok:
    c = f["c"]
    print(f"{f['navn']:<12}{c['KI']:>12.4e}{c['BrO3']:>12.4e}{c['HCl']:>12.4e}{c['S2O3']:>12.4e}")

print("\nHastighet og k")
print(f"{'Forsøk':<12}{'t (s)':>8}{'v (M/s)':>14}{'k (M^-3 s^-1)':>18}")
for f in forsok:
    print(f"{f['navn']:<12}{f['t']:>8}{f['v']:>14.3e}{f['k']:>18.3g}")

print(f"\nk (gjennomsnitt) = {k:.3g} M^-3 s^-1")
print(f"s = {s:.2g}")