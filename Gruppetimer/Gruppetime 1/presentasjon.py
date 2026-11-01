for x in range(10):
    if x == 5:
        break
    print(x)


for x in range(5):
    if x == 2:
        continue
    print(x)


for i in range(5):
    print(i)

for i in range(3, 5):
    print(i)

for i in range(0, 5, 2):
    print(i)

for x in [1, 2, 3]:
    print(x)

for x in [10, 20, 30]:
    print(x)



i = 0

while i < 5:
    print(i)
    i += 2

password = ""

while password != "1234":
    password = input("Passord: ")

print("Riktig!")