def minim(a,b,c):
    '''
    determina minimul a 3 nr.
    :param a: nr. intreg
    :param b: nr. intreg
    :param c: nr. intreg
    :return: minimul dintre a, b si c
    '''
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

def isPrime(x):
    '''
    determina daca un nr. este prim
    :param x: nr. intreg
    :return: True, daca x este prim sau False, in caz contrar
    '''

    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True


assert isPrime(-1) is False
assert isPrime(0) is False
assert isPrime(1) is False
assert isPrime(2) is True
assert isPrime(3) is True
assert isPrime(4) is False
assert isPrime(5) is True

def oglindit(x):
    '''
    calculeaza oglinditul unui nr.
    :param x: nr natural
    :return: oglinditul lui x
    '''
    y = 0
    while x != 0:
        y = y * 10 + x % 10
        x = x // 10
    return y


assert oglindit(2) == 2
assert oglindit(212) == 212
assert oglindit(254) == 452

while True:
    print("1. Determinati minimul a 3 nr.")
    print("2. Determinati daca un nr. este prim")
    print("3. Determinati, pt. n numere, daca acestea sunt prime")
    print("4. Determinati oglinditul unui numar")
    print("x. Iesire")

    optiune = input("Dati optiunea: ")
    if optiune == "1":
        a = int(input("Dati primul numar:"))
        b = int(input("Dati al doilea numar:"))
        c = int(input("Dati al treilea numar:"))

        print(minim(a,b,c))
    elif optiune == "2":
        x = int(input("Dati nr.:"))
        if isPrime(x):
            print("DA")
        else:
            print("NU")
    elif optiune == "3":
        n = int(input("Dati nr. de nr.: "))
        for i in range(n):
            x = int(input("Dati nr.:"))
            if isPrime(x):
                print("DA")
            else:
                print("NU")
    elif optiune == "4":
        x = int(input("Dati nr.:"))
        print(oglindit(x))
    elif optiune == "x":
        break
    else:
        print("Optiune gresita! Reincercati!")