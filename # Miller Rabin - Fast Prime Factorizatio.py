import random
from collections import Counter
prime_factorization = []
plist = []
def miller_rabin(n, k=5):
    if n in (2, 3):
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # Composite
    return True  # Probably prime
n = int(input("Choose a value of n: "))

def divisors(n):
    divisor = set()
    for _ in range(1,int(n**0.5) + 1):
        if n % _ == 0:
            divisor.add(_)
            divisor.add(n // _)
    return sorted(divisor)
for i in divisors(n):
    if miller_rabin(i,k=5) == True:
        plist.append(i)
for j in plist:
    n_copy = n 
    while n_copy % j == 0:
        n_copy = n_copy // j
        prime_factorization.append(j) 
print(dict(Counter(prime_factorization)))
print(f'Multiply each of these values ( ex 2:3,5:1 =2*2*2*5 ) together and you should get {n}')
