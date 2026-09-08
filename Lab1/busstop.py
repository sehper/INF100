husnummer = int(input("Husnummer:"))      
stopp = round(husnummer / 7) * 7    #her deler vi husnummeret på 7, og avrunder, dette fører til at vi kommer til nærmeste heltall.
#hvert 7ende stopp

print("Nærmeste busstopp er ved nummer", stopp)