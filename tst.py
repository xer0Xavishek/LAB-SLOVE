# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 4, 1000)
# S1 = (32/np.pi) * np.sin(np.pi*x/2)
# S3 = S1 + (32/(3*np.pi)) * np.sin(3*np.pi*x/2)
# S5 = S3 + (32/(5*np.pi)) * np.sin(5*np.pi*x/2)

# plt.plot(x, S1, label='S1')
# plt.plot(x, S3, label='S3')
# plt.plot(x, S5, label='S5')
# plt.legend()
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
    x_mod = x % 4
    return 8 if (x_mod < 2) else -8

# Generate x values
x = np.linspace(-4, 8, 1000)
y = np.array([f(xi) for xi in x])

# Plot
plt.figure(figsize=(10, 4))
plt.plot(x, y, 'b')
plt.title('Graph of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--')
plt.ylim(-9, 9)
plt.show()