import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Pendulum class definition
class Pendulum:
    def __init__(self, theta1, theta2, dt, l1=1, l2=1, p1=0, p2=0, m1=1, m2=1):
        self.theta1 = theta1
        self.theta2 = theta2

        self.p1 = p1
        self.p2 = p2

        self.l1 = l1
        self.l2 = l2

        self.m1 = m1
        self.m2 = m2

        self.dt = dt

        self.g = 9.81

        self.trajectory = [self.polar_to_cartesian()]
        self.time = 0.0

    def polar_to_cartesian(self):
        x1 = self.l1 * np.sin(self.theta1)
        y1 = -self.l1 * np.cos(self.theta1)

        x2 = x1 + self.l2 * np.sin(self.theta2)
        y2 = y1 - self.l2 * np.cos(self.theta2)

        return np.array([[0.0, 0.0], [x1, y1], [x2, y2]])

    def derivatives(self, state):
        theta1, theta2, p1, p2 = state
        l1, l2 = self.l1, self.l2
        m1, m2 = self.m1, self.m2
        g = self.g

        sin_diff = np.sin(theta1 - theta2)
        cos_diff = np.cos(theta1 - theta2)
        denom = l1 * l2 * (m1 + m2 * sin_diff**2)

        # Angular velocities
        dtheta1 = (l2 * p1 - l1 * p2 * cos_diff) / (l1**2 * denom)
        dtheta2 = (l1 * (m1 + m2) * p2 - l2 * m2 * p1 * cos_diff) / (l2**2 * m2 * denom)

        # Generalized momenta derivatives
        dp1 = -(m1 + m2) * g * l1 * np.sin(theta1) - (
            (p1 * p2 * sin_diff) / denom
        ) + (
            ((l2**2 * m2 * p1**2 + l1**2 * (m1 + m2) * p2**2 - l1 * l2 * m2 * p1 * p2 * cos_diff)
            * np.sin(2 * (theta1 - theta2))) / (2 * denom**2)
        )

        dp2 = -m2 * g * l2 * np.sin(theta2) + (
            (p1 * p2 * sin_diff) / denom
        ) - (
            ((l2**2 * m2 * p1**2 + l1**2 * (m1 + m2) * p2**2 - l1 * l2 * m2 * p1 * p2 * cos_diff)
            * np.sin(2 * (theta1 - theta2))) / (2 * denom**2)
        )

        return np.array([dtheta1, dtheta2, dp1, dp2])

    def evolve(self):
        # Current state
        state = np.array([self.theta1, self.theta2, self.p1, self.p2])

        # Runge-Kutta 4th order integration
        k1 = self.derivatives(state)
        k2 = self.derivatives(state + self.dt * k1 / 2)
        k3 = self.derivatives(state + self.dt * k2 / 2)
        k4 = self.derivatives(state + self.dt * k3)
        new_state = state + self.dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6

        # Update variables
        self.theta1, self.theta2, self.p1, self.p2 = new_state

        # Record new position
        self.time += self.dt
        new_position = self.polar_to_cartesian()
        self.trajectory.append(new_position)
        return new_position

    def velocities(self):
        dtheta1, dtheta2, _, _ = self.derivatives(
            [self.theta1, self.theta2, self.p1, self.p2]
        )
        v1 = self.l1 * dtheta1
        v2 = self.l2 * dtheta2
        return v1, v2


# Streamlit UI
st.title("Real-Time Double Pendulum Simulation with Velocity and Position Table")

# Sidebar inputs for pendulum attributes
with st.sidebar:
    st.header("Pendulum Settings")
    theta1 = st.slider("Initial Angle 1 (radians)", 0.0, 2 * np.pi, np.pi)
    theta2 = st.slider("Initial Angle 2 (radians)", 0.0, 2 * np.pi, np.pi - 0.01)
    l1 = st.slider("Length of Rod 1", 0.5, 2.0, 1.0)
    l2 = st.slider("Length of Rod 2", 0.5, 2.0, 1.0)
    m1 = st.slider("Mass of Bob 1", 0.5, 5.0, 1.0)
    m2 = st.slider("Mass of Bob 2", 0.5, 5.0, 1.0)
    dt = st.slider("Time Step (s)", 0.001, 0.1, 0.01)

    num_steps = st.slider("Number of Steps", 100, 2000, 500)
    trace_switch = st.checkbox("Show Bob 2 Trace", value=True)
    start_button = st.button("Start/Restart Simulation")

# Session state to manage simulation status
if "pendulum" not in st.session_state or start_button:
    st.session_state.pendulum = Pendulum(theta1, theta2, dt, l1, l2, m1=m1, m2=m2)

pendulum = st.session_state.pendulum

# Create placeholders
plot_placeholder = st.empty()
table_placeholder = st.empty()

# Real-time animation
trace_x = []
trace_y = []

for _ in range(num_steps):
    position = pendulum.evolve()
    v1, v2 = pendulum.velocities()
    x2, y2 = position[2]

    # Update trace if enabled
    if trace_switch:
        trace_x.append(x2)
        trace_y.append(y2)

    # Create figure
    fig, ax = plt.subplots()
    ax.set_xlim(-l1 - l2 - 0.5, l1 + l2 + 0.5)
    ax.set_ylim(-l1 - l2 - 0.5, l1 + l2 + 0.5)
    ax.grid(True)

    # Plot the pendulum
    ax.plot([position[0, 0], position[1, 0]], [position[0, 1], position[1, 1]], "o-", lw=2, color="blue")
    ax.plot([position[1, 0], position[2, 0]], [position[1, 1], position[2, 1]], "o-", lw=2, color="red")
    ax.plot(position[2, 0], position[2, 1], "ro", markersize=10)  # Second bob as red circle

    # Plot trace if enabled
    if trace_switch:
        ax.plot(trace_x, trace_y, "r--", lw=1)

    # Update plot
    plot_placeholder.pyplot(fig)
    plt.close(fig)

    # Update table
    table_placeholder.table({
        "Time (s)": [round(pendulum.time, 2)],
        "Velocity of Mass 1 (m/s)": [round(v1, 2)],
        "Velocity of Mass 2 (m/s)": [round(v2, 2)],
        "Bob 2 Position (x, y)": [(round(x2, 2), round(y2, 2))]
    })

    # Simulate real-time delay
    time.sleep(0.01)
