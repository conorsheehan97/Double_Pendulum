# Double Pendulum Simulation

This project is an exploration of the dynamics of the double pendulum system using Python. It covers theoretical derivations, numerical simulations, and visualizations of this fascinating system.

If you want to skip all of the boring stuff, I have the app deployed over yonder on Streamlit [here](https://conors-double-pendulum.streamlit.app/):
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

Special thanks to:

- Sir William Rowan Hamilton (Irishman) for foundational work in mechanics.
- Everyone online who had the derivation already done so I could act like I did it.
