w1 = str(input("Skriv et ord:"))
w2 = str(input("\nSkriv et annet ord:"))
w3 = str(input("\nSkriv et siste ord:"))
print()
print()

l1 = len(w1)
l2 = len(w2)
l3 = len(w3)

if l1 == l2 == l3:
    print(w1)
elif l1 == l2 and l1 > l3:
    print(w1)
elif l1 == l3 and l1 > l2:
    print(w1)
elif l2 == l3 and l2 > l1:
    print(w2)
elif l1 > l2 and l1 > l3:
    print(w1)
elif l2 > l1 and l2 > l3:
    print(w2)
elif l3 > l1 and l3 > l2:
    print(w3)

