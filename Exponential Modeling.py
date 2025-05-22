# exponential modeling
import numpy as np
import random as rand
import matplotlib.pyplot as plt
exponent = round(rand.uniform(0.5, 5), 3)  # b
scale = round(rand.uniform(1, 5), 3)       # a
print(f"True model: y = {scale} * e^({exponent}x)")
dp = int(input('Choose a number of data points: '))
x = []
y = []
for i in range(1,dp+1):
    x.append(i)
    noise = np.random.normal(0, 0.5)
    y.append(scale * np.exp(exponent * i) + noise)
y = [round(i,3) for i in y]
ln_y = np.array([np.log(i) for i in y])
o_v = np.ones(dp)
A = np.column_stack((o_v,x))
A_T = A.transpose()
S_A = np.matmul(A_T, A)
S_B = np.matmul(A_T, ln_y)
sol = np.linalg.solve(S_A,S_B)
b = round(sol[0],3)
a = round(np.exp(sol[1]),3)
points = np.column_stack((x,y))

# Print results
print(f'\nFitted model: y = {a} * e^({b}x)')
print('Generated data points:')
print(points)

# Prepare smooth curve for plotting
x_vals = np.linspace(min(x), max(x), 200)
y_fit = a * np.exp(b * x_vals)

# Plot
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_vals, y_fit, color='red', label='Best Fit: y = {:.3f}e^({:.3f}x)'.format(a, b))
plt.title('Exponential Regression Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()