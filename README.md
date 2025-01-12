# Double Pendulum Simulation

This project is an exploration of the dynamics of the double pendulum system using Python. It covers theoretical derivations, numerical simulations, and visualizations of this fascinating system.

## Future Improvements

1. **Extend the code to include damping and external driving forces**: Adding damping forces and external forces (e.g., driven motion) will make the simulation more realistic and enable the study of energy dissipation.
2. **Explore the phase space of the system to analyze chaotic attractors**: Investigating the system's phase space can help to understand its chaotic nature more deeply.
3. **Add a graphical user interface (GUI) for parameter customization and real-time visualization**: This will allow users to interactively adjust the parameters, such as initial angles, lengths, and masses, and see the results in real-time.
4. **Implement 3D visualizations and trajectory plots for better insights into the system's behavior**: Enhancing the visualization with 3D plots will give users a more comprehensive understanding of the system's motion.
5. **Calculate and visualize Lyapunov exponents to measure the degree of chaos**: Lyapunov exponents are used to quantify the chaotic behavior of dynamic systems, and visualizing them will offer more insights into the system's sensitivity to initial conditions.

## Overview

The double pendulum consists of two pendulums connected end-to-end. While the system appears simple, it exhibits chaotic dynamics, where small differences in initial conditions result in vastly different outcomes. This makes it a compelling subject for both theoretical study and numerical simulation.

## Key Features

- **Theoretical Foundations**: Detailed derivation of equations of motion using Lagrangian mechanics.
- **Numerical Simulation**: Implementation of the equations in Python to solve and visualize the motion of the double pendulum.
- **Visualization**: Dynamic animations of the pendulum's motion to showcase its chaotic behavior.

## Project Content

- **PDF Documentation**: A detailed write-up explaining:
  - The physical system and its chaotic nature.
  - Derivation of the equations of motion using Newtonian and Lagrangian mechanics.
  - Hamiltonian formulation as an alternative framework.

- **Python Code**: Scripts for:
  - Numerically solving the equations of motion.
  - Generating visualizations of the pendulum's trajectories.

## Physics Background

### Equations of Motion

The double pendulum's motion is governed by nonlinear differential equations derived using the Lagrangian approach:
- Positions of the two masses are expressed in terms of polar coordinates.
- Kinetic and potential energy terms are used to form the Lagrangian, \( L = T - U \).
- Euler-Lagrange equations yield the dynamics for angles \( \theta_1 \) and \( \theta_2 \).

### Chaos and Sensitivity

The system's chaotic nature arises from the dependence on initial conditions. Even small changes in initial angles or velocities lead to drastically different trajectories, making the double pendulum an excellent example of chaos in classical mechanics.


## Acknowledgments

This project was inspired by the beauty and complexity of chaotic systems. Special thanks to:

- Sir William Rowan Hamilton (Irishman) for foundational work in mechanics.
