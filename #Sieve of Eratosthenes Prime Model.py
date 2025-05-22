import numpy as np
import matplotlib.pyplot as plt
import time
start = time.time()
# sieve code
a = int(input('Choose an upperbound greater than 3: ')) 
is_prime = [True] * (a + 1)
is_prime[0:2] = [False, False]  # 0 and 1 are not prime
for n in range(2, int(a**0.5) + 1):
    if is_prime[n]:
        for multiple in range(n * n, a + 1, n):
            is_prime[multiple] = False
prime_list = [i for i, val in enumerate(is_prime) if val]
length = len(prime_list)
print(length)
o_v = np.ones(length) # one vector
x_list = list(range(1,length+1))
x_list = [i*np.log(i) + np.log(i) for i in x_list] # transformed into nlogn + logn
A = np.column_stack((o_v,x_list))
prime_list = np.array(prime_list)
A_T = np.transpose(A)
S_A = np.matmul(A_T,A)
S_B = np.matmul(A_T,prime_list)
sol = np.linalg.solve(S_A,S_B)
b = sol[0]
a = sol[1]
print(f'The best fit line for the data is y = {a}x*ln(x) + {a}*ln(x) + {b}')
plt.figure(figsize=(10, 6))
skip = 100
plt.scatter(x_list[::skip], prime_list[::skip], label='Prime data', color='blue')
x_fit = np.linspace(min(x_list), max(x_list), 300)
y_fit = a * x_fit + b
plt.plot(x_fit, y_fit, color='red', label='Best fit line: $y = a(n\\log n) + n\\log n + b$')
plt.xlabel('$n \\log n$')
plt.ylabel('$p(n)$ (n-th prime)')
plt.title('Prime Number Growth vs $n \\log n$')
plt.legend()
plt.grid(True)
plt.show()
print("Sieve time:", time.time() - start)