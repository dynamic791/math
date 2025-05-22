#emirp
n = int(input("Please choose an integer greater than 1: "))
while int(n) <= 1:
    n = int(input("Please choose a number larger than 1: "))
n_copy = n
n_r = str(n)[::-1]
n_reverse = int(n_r)
primes = []
palindromic = []
emirp = []
while n > 1:
    divisors = []
    divisors_reverse = []
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 0:
        primes.append(n)
        if str(n) == str(n)[::-1]:
            palindromic.append(n)
        elif str(n) != str(n)[::-1]: 
            for j in range(2,int(n_reverse**0.5)+1):
                if n_reverse % j == 0:
                    divisors_reverse.append(j)
            if len(divisors_reverse) == 0:
                emirp.append(n)
    n -= 1
    n_r = str(n)[::-1]
    n_reverse = int(n_r)
print("In the interval (2," + str(n_copy) + "), there are " + str(len(emirp)) + " emirps!!!")
print("The ratio between emirps and primes is " + str(len(emirp) / len(primes)))
print("The ratio between emirps and palindromics is " + str(len(emirp) / len(palindromic)))
print("Here are the emirps: " + str(emirp))