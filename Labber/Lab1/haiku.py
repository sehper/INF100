r1 = str(input("Første raden:\n"))
r2 = str(input("Andre raden:\n"))
r3 = str(input("Tredje raden:\n"))
print()

l1 = len(r1)
l2 = len(r2)
l3 = len(r3)

mlength = max(l1, l2, l3)

bar = (mlength + 4) * "@"
b1 = "@" + " " + (mlength - l1) * " " + r1 + " " + "@\n"
b2 = "@" + " " + (mlength - l2) * " " + r2 + " " + "@\n"
b3 = "@" + " " + (mlength - l3) * " " + r3 + " " + "@\n"

print(bar, "\n", b1, b2, b3, bar, sep = "")


