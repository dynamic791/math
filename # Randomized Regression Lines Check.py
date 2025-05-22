# Randomized Regression Lines Check
import numpy as np
import random as rand
import matplotlib.pyplot as plt
times = int(input('How many regression lines would you like to calculate? '))
length = int(input('How many data points should be included in each? '))
for _ in range(times):
    data_x = []
    data_y = []
    o_v = np.ones(length) # One vector
    for i in range(1,length + 1):
        data_x.append(rand.randint(-20, 20))
        data_y.append(rand.randint(-20, 20))
    A = np.column_stack((o_v, data_x))
    A_T = np.transpose(A)
    S_A = np.matmul(A_T, A) 
    S_b = np.matmul(A_T, data_y) 
    sol = np.linalg.solve(S_A,S_b)
    data_x = np.array(data_x)
    data_y = np.array(data_y)
    print('The best fit line for the given data is, y = ' + str(round(sol[1],3)) + 'x + ' + str(round(sol[0],3)))
    data = np.column_stack((data_x,data_y))
    if length < 8:
        print('The given data is \n', data)

       # Plotting the data and regression line
    x_vals = np.linspace(min(data_x), max(data_x), 100)
    y_vals = sol[0] + sol[1] * x_vals

    plt.scatter(data_x, data_y, color='blue', label='Data Points')
    plt.plot(x_vals, y_vals, color='red', label='Best Fit Line')
    plt.title('Random Linear Regression')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()