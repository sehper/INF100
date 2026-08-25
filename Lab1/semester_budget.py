import math

bud = int(input("Hva er budsjettet ditt?\n")) #Jeg har valgt å bruke int istedenfor float

bo = int(input("Hvor mye bruker du på bolig?\n"))

mat = int(input("Hvor mye bruker du på mat?\n"))

rest = bud - bo - mat

kpris = 45      #prisen for en kopp kaffe
kaffe = math.floor(rest / kpris)

print(f"Det er {rest} NOK igjen, det er nok til {kaffe} kopper kaffe!")

