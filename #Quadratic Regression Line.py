import matplotlib.pyplot as plt
import numpy as np
import random as rand
data_b = []
data_x = []
data_x2 = []
dp = int(input('How many data points for each quadratic? ')) # data points
for i in range(dp):
    data_x.append(rand.randint(-5,5))
    data_b.append(rand.randint(-5,5))
data_x2 = [i**2 for i in data_x]
o_v = np.ones(dp)
data_x = np.array(data_x)
data_x2 = np.array(data_x2)
data_b = np.array(data_b)
A = np.column_stack((o_v, data_x, data_x2))
A_T = A.transpose()
S_A = np.matmul(A_T,A)
S_B = np.matmul(A_T, data_b)
sol = np.linalg.solve(S_A,S_B)
print(sol)
a = round(sol[0],3)
b = round(sol[1],3)
c = round(sol[2],3)
print('The best fit quadratic for the data is the equation y = ' + str(a) + 'x² +' + str(b) + 'x + ' + str(c))
x_range = np.linspace(min(data_x), max(data_x), 200)
y_fit = a * x_range**2 + b * x_range + c
plt.scatter(data_x, data_b, color='blue', label='Data Points')
plt.plot(x_range, y_fit, color='red', label='Best Fit Quadratic')
plt.title('Quadratic Regression Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()