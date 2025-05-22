#Galton Board
from collections import Counter
import random as rand
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

direction = [-1,1]
bins = []
ball_s = 0
games = int(input('Choose a number of balls: '))
count = 0
while games > 2:
    if count != 5:
        ball_s += rand.choice(direction)
        count += 1
    elif count == 5:
        bins.append(ball_s)
        games -= 1
        ball_s = 0
        count = 0
bins.sort()
count_bins = Counter(bins)
print(count_bins)

bin_positions = sorted(count_bins.keys())
frequencies = [count_bins[pos] for pos in bin_positions]

plt.bar(bin_positions, frequencies, width=0.8, color='skyblue', edgecolor='black', label='Observed')

# Fit normal distribution
mu, std = norm.fit(bins)
x = np.array(bin_positions)
pdf_values = norm.pdf(x, mu, std)

# Scale the normal distribution to match the histogram counts
bin_width = 1  # Set to 1 if bins are adjacent integers
scaled_pdf = pdf_values * games * bin_width

# Plot fitted curve
plt.plot(x, scaled_pdf, 'r-', linewidth=2, label=f'Normal Fit\nμ={mu:.2f}, σ={std:.2f}')
plt.xlabel('Final Position (Bin)')
plt.ylabel('Number of Balls')
plt.title('Galton Board Distribution with Normal Fit')
plt.grid(axis='y')
plt.legend()
plt.show()