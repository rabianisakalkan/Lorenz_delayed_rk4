# Lorenz_delayed_rk4

This repository contains a Python implementation of the Lorenz system with delay, utilizing the fourth-order Runge-Kutta method for numerical integration. The Lorenz system is a classic example of a deterministic chaotic system that describes the behavior of a simplified atmosphere, exhibiting complex, non-linear dynamics.

The Lorenz system is represented by three coupled ordinary differential equations (ODEs) that govern the evolution of three state variables - x, y, and z. The parameters σ, ρ, and β are constants that define the system's behavior. In this implementation, we consider the addition of delay terms τx, τy, and τz to the system. These delay terms introduce memory effects into the system, making it even more intriguing.

Numerical Integration with Runge-Kutta 4th Order Method

To simulate the Lorenz system with delay, we employ the fourth-order Runge-Kutta method, a robust and accurate numerical integration technique. This method allows us to compute the future values of the state variables (x, y, and z) by solving the DDEs iteratively.
Interpolation Technique

Incorporating delay terms into the Lorenz system introduces a temporal component, requiring us to interpolate past values of the state variables to compute the delayed terms accurately. In this project, we use cubic spline interpolation to approximate the state variables' values at earlier time points. This interpolation technique ensures smooth and continuous approximations of the delayed variables, allowing for precise calculations in the Runge-Kutta integration.

Importance of Initial Conditions

The choice of initial conditions plays a crucial role in understanding and simulating the behavior of chaotic systems like the Lorenz system with delay. Even minor variations in the initial conditions can lead to significantly different trajectories, highlighting the sensitivity of chaotic systems to their starting points. Therefore, understanding the system's behavior and its sensitivity to initial conditions is fundamental to interpreting the simulation results.

Visualization

The simulation results are visualized using matplotlib. We provide both 3D trajectory plots and time series plots of the individual components (x, y, and z) to facilitate the analysis and visualization of the system's behavior.

Conclusion

This project showcases the integration of the Lorenz system with delay using the fourth-order Runge-Kutta method, providing insights into the complex dynamics of chaotic systems. By considering delay terms, we explore the system's memory effects, highlighting the importance of interpolation and the sensitivity to initial conditions. The visualization tools presented here help in understanding and visualizing the system's behavior over time.

Feel free to explore the code and experiment with different parameters to gain a deeper understanding of chaotic systems and their behavior in the presence of delays.


