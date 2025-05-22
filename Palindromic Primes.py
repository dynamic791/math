#Palindromic Primes
#list[::-1] to reverse a list.
#[int(i) for i in str(n)] - slices # into a list

n = int(input("Please choose an integer greater than 1: "))
palindromic_primes = []
primes = []
palindromic = []
while int(n) <= 1:
    n = int(input("Please choose a number larger than 1: "))
n_copy = n
while n > 1:
    count_p = 0 
    divisors = []
    n_list = [int(i) for i in str(n)]
    n_reverse = n_list[::-1]
    if n_list == n_reverse:
        palindromic.append(n)
        count_p += 1
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 0 and count_p == 0:
        primes.append(n)
    if len(divisors) == 0 and count_p == 1:
        palindromic_primes.append(n)
    n -= 1
print("In the interval (2," + str(n_copy) + ") the palindromic primes are " + str(palindromic_primes))
print("The rate of palindromic primes to primes in this interval is " + str(len(palindromic_primes) / len(primes)))
print("The rate of palindromic primes to palindromic numbers in this interval is " + str(len(palindromic_primes) / len(palindromic)))