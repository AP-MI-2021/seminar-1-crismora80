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

x = int(input("Dati nr.:"))
if isPrime(x):
    print("DA")
else:
    print("NU")

