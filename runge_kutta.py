import numpy as np
import matplotlib.pyplot as plt

def dydt(t, y):
    return -2 * y

def runge_kutta_4(f, y0, t0, tf, h):
    t_values = np.arange(t0, tf + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        t = t_values[i-1]
        y = y_values[i-1]

        k1 = f(t, y)
        k2 = f(t + h/2, y + h*k1/2)
        k3 = f(t + h/2, y + h*k2/2)
        k4 = f(t + h, y + h*k3)

        y_values[i] = y + h*(k1 + 2*k2 + 2*k3 + k4)/6

    return t_values, y_values

# Parameters
y0 = 1
t0 = 0
tf = 2
h = 0.1

# Solve the ODE using RK4
t_values, y_values_rk4 = runge_kutta_4(dydt, y0, t0, tf, h)

# Exact solution
y_exact = np.exp(-2 * t_values)

# Plot the results
plt.plot(t_values, y_values_rk4, 'b-', label='RK4 Approximation')
plt.plot(t_values, y_exact, 'r--', label='Exact Solution')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title('Runge-Kutta 4th Order Method vs Exact Solution')
plt.show()

# Calculate and print the error
error = np.abs(y_exact - y_values_rk4)
print("Maximum error:", np.max(error))
