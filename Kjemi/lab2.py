def syrebase(t1, t2, C):
    m = 100
    c = 4.18
    print(-(C*t1 + m*c*t1 + m*c*t2))
    return -(C*t1 + m*c*t1 + m*c*t2)


P1 = syrebase(5.5, 5.7, 7.5)
P1max = syrebase(5.5, 5.7, 7.5 + 3.5)
P1min = syrebase(5.5, 5.7, 7.5 - 3.5)

P2 = syrebase(6.7, 6.4, 7.5)
P2max = syrebase(6.7, 6.4, 7.5 + 3.5)
P2min = syrebase(6.7, 6.4, 7.5 - 3.5)

print((((P1 + P1max + P1min)/3) + (P2 + P2max + P2min)/3)/2)
