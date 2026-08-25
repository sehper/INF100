import math

x = float(input("Hvor mange er dere på laget?\n"))
y = float(input("Hvor mange twist er det i posen dere vant?\n"))

print("Det blir", math.floor(y / x), "twist til hver, og det blir", round(y % x), "twist til overs.")


