import matplotlib.pyplot as plt
import numpy as np

bColor = '#fff'
fColor = '#000'
pColor = '#ff0049'

def gravity(x):
    me = 5.972 * 10**24  
    r = 6378100 + x  
    G = 6.673 * (10**-11)  
    g = (G * me) / (r**2)
    return g

def rocket_motion(mass_initial, height_initial, velocity_initial, thrust, burn_time, time_total, dt):
    t = np.arange(0, time_total, dt)
    x_vals = np.zeros(len(t))
    v_vals = np.zeros(len(t))
    a_vals = np.zeros(len(t))
    m_vals = np.zeros(len(t))
    
    mass = mass_initial
    height = height_initial
    velocity = velocity_initial
    
    for i, time in enumerate(t):
        g = gravity(height)
        m_vals[i] = mass
        x_vals[i] = height
        v_vals[i] = velocity
        
        if time < burn_time:
            acceleration = (thrust - mass * g) / mass
            mass -= 0.05 * dt  
        else:
            acceleration = -g
        a_vals[i] = acceleration
        
        height += velocity * dt + 0.5 * acceleration * dt**2
        velocity += acceleration * dt

        if height < 0:
            t = t[:i+1]
            x_vals = x_vals[:i+1]
            v_vals = v_vals[:i+1]
            a_vals = a_vals[:i+1]
            m_vals = m_vals[:i+1]
            break
        
    return t, x_vals, v_vals, a_vals, m_vals

# Adjusted Parameters
mass_initial = 20 # Initial mass of the rocket in kg
height_initial = 500  # Initial height of the rocket from the Earth's surface in meters
velocity_initial = 0 # Initial velocity of the rocket in m/s
thrust =300 # Thrust of the rocket's engines in Newtons (reduced for realism)
burn_time = 15  # Duration of the burn phase in seconds (increased for realism)
time_total = 1000  # Total time of the simulation in seconds (increased for realism)
dt = 0.1  # Time step size in seconds (decreased for better accuracy)

t, x_vals, v_vals, a_vals, m_vals = rocket_motion(mass_initial, height_initial, velocity_initial, thrust, burn_time, time_total, dt)
plt.figure(facecolor=bColor, figsize=(10, 8))

# Plot for Mass
plt.subplot(2, 2, 1)
plt.plot(t, m_vals, color='yellow')
plt.xlabel('Time (s)', color=fColor)
plt.ylabel('Mass (kg)', color=fColor)
plt.title('Mass-Time', color=fColor)
plt.grid(color=fColor)

# Plot for Velocity
plt.subplot(2, 2, 2)
plt.plot(t, v_vals, color='green')
plt.xlabel('Time (s)', color=fColor)
plt.ylabel('Velocity (m/s)', color=fColor)
plt.title('Velocity-Time', color=fColor)
plt.grid(color=fColor)

# Plot for Acceleration
plt.subplot(2, 2, 3)
plt.plot(t, a_vals, color='red')
plt.xlabel('Time (s)', color=fColor)
plt.ylabel('Acceleration (m/s^2)', color=fColor)
plt.title('Acceleration-over Time', color=fColor)
plt.grid(color=fColor)

# Plot for Height
plt.subplot(2, 2, 4)
plt.plot(t, x_vals, color='blue')
plt.xlabel('Time (s)', color=fColor)
plt.ylabel('Height (m)', color=fColor)
plt.title('Height-Time', color=fColor)
plt.grid(color=fColor)

# Adjust y-axis limits for each plot
plt.subplot(2, 2, 1)
plt.ylim(np.min(m_vals) - 10, np.max(m_vals) + 10)

plt.subplot(2, 2, 2)
plt.ylim(np.min(v_vals) - 50, np.max(v_vals) + 50)

plt.subplot(2, 2, 3)
plt.ylim(np.min(a_vals) - 5, np.max(a_vals) + 5)

plt.subplot(2, 2, 4)
plt.ylim(np.min(x_vals) - 1000, np.max(x_vals) + 1000)

plt.tight_layout()
plt.show()
