#prime, perfect, fibonacci, square, even or odd, factorial (for small n), factors, binary representations
import random

def prime_check(n, k=5):
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
if n % 2 == 0:
    print(str(n) + ' is even')
else:
    print(str(n) + ' is odd')

if prime_check(n,k=5) == True:
    print(str(n) + " is most likely prime")
    print("The prime factorization of " + str(n) + " is [1," + str(n) + "]")

prime_factorization = []
plist = []

def divisors(n):
    divisor = set ()
    for _ in range(1,int(n**0.5) + 1):
        if n % _ == 0:
            divisor.add(_)
            divisor.add(n // _)
    return sorted(divisor)
if sum(divisors(n)) == n:
    print(str(n) + " is a perfect number!")
else:
    print(str(n) + ' is not a perfect number!')
if prime_check(n,k=5) == False:
    print(str(n) + " is composite")
    for i in divisors(n):
        if prime_check(i,k=5) == True:
            plist.append(i)
    for j in plist:
        n_copy = n 
        while n_copy % j == 0:
            n_copy = n_copy // j
            prime_factorization.append(j) 
for i in divisors(n):
    if i**2 == n:
        print(str(n) + ' is a square number')
        break    
print('The factors of ' + str(n) + ' are ' + str(divisors(n)))
print('The prime factorization of ' + str(n) + ' is ' + str(prime_factorization))
# factorial
if n < 250:
    if n == 0 or n == 1:
        print(str(n) + ' factorial equals 1')
    else:
        f = 1
        for i in range(2,n+1):
            x = i
            f = x*f 
    print(str(n) + '! is equal to ' + str(f))
