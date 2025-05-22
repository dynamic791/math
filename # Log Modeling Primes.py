# Find Primes up to N, then graph
import numpy as np
import matplotlib.pyplot as plt
x_list = []
prime_list = [] # y in A^TAx = A^Ty
old_prime = 1
n = int(input('Choose a positive integer greater than 1: '))
for i in range(3,n+1): # Generate x
    x_list.append(i)
o_v = np.ones(n-2) # one vector
f = 3
while f <= n: # Creates a list of the 'latest' prime number
    divisors_list = []
    for i in range(1,int(f**0.5)+1):
        if f % i == 0:
            divisors_list.append(i)
    if len(divisors_list) == 1:
        prime_list.append(f)
        old_prime = f
        f += 1
    elif len(divisors_list) > 1:
        prime_list.append(old_prime)
        f += 1
x_list = [np.log(np.log(i)) for i in x_list if i > 2]
A = np.column_stack((o_v,x_list)) # ln(y) = ln(a) + ln(ln(bx))
A_T = np.transpose(A)
S_A = np.matmul(A_T,A)
prime_list = [np.log(i) for i in prime_list] # ln(y)
S_B = np.matmul(A_T, prime_list)
sol = np.linalg.solve(S_A,S_B)
intercept = np.exp(sol[0])
exponent = sol[1]
print(f'The best fit natural logarithmic equation for the data is y = {round(intercept,4)} *ln(x)^{round(exponent,4)}')
predicted_ln_y = [sol[0] + sol[1] * x for x in x_list]
x_vals_original = [np.exp(np.exp(x)) for x in x_list]  # approximate original x
y_actual = [np.exp(y) for y in prime_list]              # y = actual primes
y_predicted = [np.exp(pred_ln_y) for pred_ln_y in predicted_ln_y]  # y = predicted values

plt.figure(figsize=(10, 6))
plt.scatter(x_vals_original, y_actual, color='green', label='Actual y', alpha=0.6)
plt.plot(x_vals_original, y_predicted, color='orange', label='Predicted y')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Model Fit: y = a * (ln(x))^b')
plt.legend()
plt.grid(True)
plt.show()