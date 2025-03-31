import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Given data
X = np.array([1.5, 3, 5, 8, 12])
Y = np.array([0.3195, 0.1874, 0.0566, 0.01608, 0.00347])

# Convert to log10 scale
logX = np.log10(X)
logY = np.log10(Y)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(logX, logY)

# Generate fitted line
logY_fit = slope * logX + intercept

# Plot data and fit
plt.figure(figsize=(8, 6))
plt.scatter(logX, logY, label='Data', color='blue')
plt.plot(logX, logY_fit, label=f'Fit: y = {slope:.4f}x + {intercept:.4f}', color='red')
plt.xlabel('log10(X)')
plt.ylabel('log10(Y)')
plt.title('Log-Log Scale Linear Fit')
plt.legend()
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.show()

# Print regression results
print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"R-squared: {r_value**2:.4f}")
