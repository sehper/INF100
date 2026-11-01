
import math
import matplotlib.pyplot as plt

KA_EDDIKSYRE = 1.75e-5
KW = 1e-14

volum_hcl = 25.0
konsentrasjon_naoh = 0.100
fasit_hcl = 0.100

volum_eddiksyre = 10.0
volum_fortynnet = 100.0
volum_opprinnelig = 10.0
fasit_eddiksyre = 0.100

volum_hcl_malt = [0, 5, 10, 15, 20, 23, 24, 24.5, 25, 25.5, 26, 27, 30]
ph_hcl_malt = [1.0, 1.2, 1.4, 1.6, 1.9, 2.3, 2.6, 3.0, 7.0, 11.0, 11.4, 11.7, 12.0]

volum_eddiksyre_malt = [0, 2, 4, 6, 8, 9, 9.5, 10, 10.5, 11, 12, 14]
ph_eddiksyre_malt = [3.0, 3.6, 4.0, 4.3, 4.6, 4.9, 5.2, 8.7, 11.0, 11.3, 11.5, 11.7]


def feilprosent(malt, fasit):
    return abs(malt - fasit) / abs(fasit) * 100


def finn_ekvivalenspunkt(volum, ph):
    stigning = []

    for i in range(len(volum) - 1):
        endring = (ph[i + 1] - ph[i]) / (volum[i + 1] - volum[i])
        stigning.append(abs(endring))

    indeks = stigning.index(max(stigning))
    return (volum[indeks] + volum[indeks + 1]) / 2


def velg_punkter(volum, ekvivalens):
    for_volum = sorted(set(v for v in volum if v < ekvivalens))
    etter_volum = sorted(set(v for v in volum if v > ekvivalens))

    for_volum = for_volum[-3:]
    etter_volum = etter_volum[:2]

    return for_volum + [ekvivalens] + etter_volum


def ph_hcl(volum_naoh, fasit, volum_syra, kons_naoh):
    mol_syra = fasit * volum_syra / 1000
    mol_base = kons_naoh * volum_naoh / 1000
    totalvolum = (volum_syra + volum_naoh) / 1000

    if math.isclose(mol_syra, mol_base, rel_tol=1e-10, abs_tol=1e-12):
        return 7.0

    if mol_syra > mol_base:
        h = (mol_syra - mol_base) / totalvolum
        return -math.log10(h)

    oh = (mol_base - mol_syra) / totalvolum
    return 14 + math.log10(oh)


def ph_eddiksyre(volum_naoh, kons_syra, volum_syra, kons_naoh):
    mol_syra = kons_syra * volum_syra / 1000
    mol_base = kons_naoh * volum_naoh / 1000
    totalvolum = (volum_syra + volum_naoh) / 1000
    total_syrekons = mol_syra / totalvolum
    natriumkons = mol_base / totalvolum

    if mol_base > mol_syra:
        oh = (mol_base - mol_syra) / totalvolum
        return 14 + math.log10(oh)

    if math.isclose(mol_base, mol_syra, rel_tol=1e-10, abs_tol=1e-12):
        kb = KW / KA_EDDIKSYRE
        oh = math.sqrt(kb * total_syrekons)
        return 14 + math.log10(oh)

    def ladning(h):
        a = KA_EDDIKSYRE * total_syrekons / (KA_EDDIKSYRE + h)
        return h + natriumkons - KW / h - a

    lav = 1e-14
    hoy = 1.0

    for i in range(200):
        midt = (lav + hoy) / 2

        if ladning(midt) > 0:
            hoy = midt
        else:
            lav = midt

    return -math.log10((lav + hoy) / 2)


def vis_resultater(navn, volum, malt_ph, ekvivalens, teoretisk_ph, konsentrasjon, fasit):
    print("\n", navn)
    print("-" * 45)
    print(f"Ekvivalenspunkt: {ekvivalens:.3f} mL")
    print(f"Beregnet konsentrasjon: {konsentrasjon:.5f} M")
    print(f"Fasitkonsentrasjon: {fasit:.5f} M")
    print(f"Feilprosent: {feilprosent(konsentrasjon, fasit):.2f} %")
    print("\nTeoretiske pH-verdier:")

    for v, ph in zip(volum, teoretisk_ph):
        print(f"{v:8.3f} mL   pH = {ph:.3f}")

    plt.figure()
    plt.plot(volum, malt_ph, "o-", label="Målt pH")
    plt.scatter(volum, teoretisk_ph, marker="x", s=90,
                label="Teoretisk pH")
    plt.axvline(ekvivalens, linestyle="--", label="Ekvivalenspunkt")
    plt.xlabel("Tilsatt NaOH (mL)")
    plt.ylabel("pH")
    plt.title(navn)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()


ekvivalens_hcl = finn_ekvivalenspunkt(volum_hcl_malt, ph_hcl_malt)
kons_hcl = konsentrasjon_naoh * ekvivalens_hcl / volum_hcl

punkter_hcl = velg_punkter(volum_hcl_malt, ekvivalens_hcl)
ph_teori_hcl = [
    ph_hcl(v, fasit_hcl, volum_hcl, konsentrasjon_naoh)
    for v in punkter_hcl
]

vis_resultater(
    "HCl titrert med NaOH",
    volum_hcl_malt,
    ph_hcl_malt,
    ekvivalens_hcl,
    ph_teori_hcl,
    kons_hcl,
    fasit_hcl
)

fasit_eddiksyre_fortynnet = fasit_eddiksyre * volum_opprinnelig / volum_fortynnet

ekvivalens_eddiksyre = finn_ekvivalenspunkt(
    volum_eddiksyre_malt, ph_eddiksyre_malt
)

kons_eddiksyre_fortynnet = (
    konsentrasjon_naoh * ekvivalens_eddiksyre / volum_eddiksyre
)

kons_eddiksyre_opprinnelig = (
    kons_eddiksyre_fortynnet * volum_fortynnet / volum_opprinnelig
)

punkter_eddiksyre = velg_punkter(
    volum_eddiksyre_malt, ekvivalens_eddiksyre
)

ph_teori_eddiksyre = [
    ph_eddiksyre(
        v,
        fasit_eddiksyre_fortynnet,
        volum_eddiksyre,
        konsentrasjon_naoh
    )
    for v in punkter_eddiksyre
]

vis_resultater(
    "CH3COOH titrert med NaOH",
    volum_eddiksyre_malt,
    ph_eddiksyre_malt,
    ekvivalens_eddiksyre,
    ph_teori_eddiksyre,
    kons_eddiksyre_opprinnelig,
    fasit_eddiksyre
)

print("\nEddiksyre")
print("-" * 45)
print(f"Konsentrasjon etter fortynning: {kons_eddiksyre_fortynnet:.5f} M")
print(f"Opprinnelig konsentrasjon: {kons_eddiksyre_opprinnelig:.5f} M")
print(f"Fasit etter fortynning: {fasit_eddiksyre_fortynnet:.5f} M")
print(f"Feilprosent: {feilprosent(kons_eddiksyre_opprinnelig, fasit_eddiksyre):.2f} %")

plt.show()
