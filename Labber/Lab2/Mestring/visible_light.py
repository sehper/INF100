colors = {
    "Violet" : {
        "nm" : range(380,451),
        "THz" : range(670, 791)
        },
    "Blue" : {
        "nm" : range(450,486),
        "THz" : range(620, 670)
        },
    "Cyan" : {
        "nm" : range(485, 501),
        "THz" : range(600, 620)
        },
    "Green" : {
        "nm" : range(500, 566),
        "THz" : range(530, 600)
        },
    "Yellow" : {
        "nm" : range(565, 591),
        "THz" : range(510, 530)
        },
    "Orange" : {
        "nm" : range(590, 626),
        "THz" : range(481, 510)
        },
    "Red" : {
        "nm" : range(625, 751),
        "THz" : range(400, 480)
        }
}

def get_color(number, unit):
    for color, values in colors.items():
        if number in values[unit]:
            return print(color)
    return print(f"{number} {unit} er utenfor det synlige spekteret.")

unit = str(input("Angi enhet (nm eller THz):\n"))


if unit == "nm":
    number = int(input("Angi verdi i nm:\n"))
    print()
    get_color(number, unit)
elif unit == "THz":
    number = int(input("Angi verdi i THz:\n"))
    print()
    get_color(number, unit)
else:
    print(f"\nEnheten må være i nm eller THz, det kan ikke være {unit}.")





