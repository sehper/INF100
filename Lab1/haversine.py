import math

print("Coordinate 1")
l1 = float(input("longitude = ")) * math.pi / 180
b1 = float(input("latitude = ")) * math.pi / 180
print("\n")

print("Coordinate 2")
l2 = float(input("longitude = ")) * math.pi / 180
b2 = float(input("latitude = ")) * math.pi / 180
print("\n")

r = 6371000 #jordens radius

d = 2*r* math.asin(math.sqrt(math.sin((b2 - b1) / 2)**2  + math.cos(b1) * math.cos(b2) * math.sin((l2 - l1) / 2)**2))

print("The distance (m) is", d)

