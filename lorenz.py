import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.interpolate import PchipInterpolator
from scipy.interpolate import InterpolatedUnivariateSpline

# Parameters
sigma, rho, beta = 10, 28, 8/3
τx, τy, τz = 0.0014, 0.01, 0.05
initial_conditions = [10, -10, 15]
dt = 0.001
T = 10

num_points = int(T/dt) + 1
t = np.linspace(0, T, num_points)
solution = np.zeros((num_points, 3))
solution[0, :] = initial_conditions

history_length = int(max(τx, τy, τz) / dt) + 1
print("Number of data points for interpolation:", history_length)
history = np.full((history_length, 3), initial_conditions)
initial_times = np.linspace(-max(τx, τy, τz), 0, history_length)

#initializing x-y-z
x_interp = InterpolatedUnivariateSpline(initial_times, history[:, 0], k=5)
y_interp = InterpolatedUnivariateSpline(initial_times, history[:, 1], k=5)
z_interp = InterpolatedUnivariateSpline(initial_times, history[:, 2], k=5)

def update_interpolators(history, t_idx):
    times = np.linspace(t_idx * dt - max(τx, τy, τz), t_idx * dt, history_length)
    
    global x_interp, y_interp, z_interp
    x_interp = InterpolatedUnivariateSpline(times, history[:, 0], k=5)
    y_interp = InterpolatedUnivariateSpline(times, history[:, 1], k=5)
    z_interp = InterpolatedUnivariateSpline(times, history[:, 2], k=5)




def lorenz_delayed(t_idx, y, history):
    
    update_interpolators(history, t_idx)


    x_delay = x_interp(t_idx*dt - τx)
    y_delay = y_interp(t_idx*dt - τy)
    z_delay = z_interp(t_idx*dt - τz)

    dx = sigma* (y_delay - x_delay)
    dy = x_delay * (rho - z_delay) - y_delay
    dz = x_delay * y_delay -  beta* z_delay
    return np.array([dx, dy, dz])

# Runge-Kutta 4th order method
def rk4_step(t_idx, y, dt, history):
    k1 = lorenz_delayed(t_idx, y, history)
    k2 = lorenz_delayed(t_idx, y + dt/2*k1, history)
    k3 = lorenz_delayed(t_idx, y + dt/2*k2, history)
    k4 = lorenz_delayed(t_idx, y + dt*k3, history)
    return y + dt/6 * (k1 + 2*k2 + 2*k3 + k4)

# Runge-Kutta integration
for i in range(1, num_points):
    y_current = solution[i-1, :]
    y_next = rk4_step(i, y_current, dt, history)
    
    
    
    # Debugging
    if i % 100 == 0:  
        print(f"Step {i}, t={i*dt:.2f}")
        print(f"Current y: {y_current}")
        print(f"Next y: {y_next}")
    
    # Check for overflow and break if detected
    if not np.isfinite(y_next).all():
        print(f"Overflow or invalid value detected at step {i}")
        break

    solution[i, :] = y_next
    history = np.roll(history, -1, axis=0)  # Shift history
    history[-1, :] = y_next  # Update latest value

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(solution[:, 0], solution[:, 1], solution[:, 2])
plt.show()


fig, axs = plt.subplots(3, 1, figsize=(12, 12))


axs[0].plot(t, solution[:, 0], label='x-component', color='blue')
axs[0].set_title('Time Series of X Component')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('X')
axs[0].grid(True)
axs[0].legend()


axs[1].plot(t, solution[:, 1], label='y-component', color='orange')
axs[1].set_title('Time Series of Y Component')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Y')
axs[1].grid(True)
axs[1].legend()


axs[2].plot(t, solution[:, 2], label='z-component', color='green')
axs[2].set_title('Time Series of Z Component')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Z')
axs[2].grid(True)
axs[2].legend()


plt.tight_layout()
plt.show()

