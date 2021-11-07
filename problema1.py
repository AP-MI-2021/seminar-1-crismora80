a = int(input("Dati primul numar:"))
b = int(input("Dati al doilea numar:"))
c = int(input("Dati al treilea numar:"))

if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)
