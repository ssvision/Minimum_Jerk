import matplotlib.pyplot as plt
import numpy as np



current = 2    #current value of trajectory (initial value)
setpoint = -2  #final setpoint value of trajectory (final value)
move_time = 0.5 #amount of time trajectory should take to reach from current value to final value
dt = 0.01 #step size


def mjtg(current, setpoint, move_time):
    trajectory = []
    trajectory_derivative = []
    trajectory_acceleration = []
    trajectory_jerk = []
    
    
    time_array = np.arange(0,move_time+dt,dt)
    for time in time_array:
        trajectory.append(current + (setpoint - current) * 
            (10.0 * (time/move_time)**3 - 15.0 * (time/move_time)**4 + 6.0 * (time/move_time)**5))
        trajectory_derivative.append((1/move_time) * (setpoint - current) *
            (30.0 * (time/move_time)**2.0
             - 60.0 * (time/move_time)**3.0
             + 30.0 * (time/move_time)**4.0))
        trajectory_acceleration.append((1/(move_time**2)) * (setpoint - current) *
            (60 * (time/move_time)
             - 180 * (time/move_time)**2.0
             + 120 * (time/move_time)**3.0))
        trajectory_jerk.append((1/(move_time**3)) * (setpoint - current) *
            (60 - 360 * (time/move_time)
             + 360 * (time/move_time)**2.0))
    
    return trajectory, trajectory_derivative, trajectory_acceleration, trajectory_jerk



traj, traj_derivative, trajectory_accn, trajectory_jerk = mjtg(current, setpoint, move_time)

# convert the list into numpy arrays
traj_array = np.array(traj)
traj_derivative_array = np.array(traj_derivative)
traj_accn_array = np.array(trajectory_accn)
traj_jerk_array = np.array(trajectory_jerk)

# prepare the x axis (time axis)
x_axis = np.arange(0,move_time+dt,dt)




################### Plotting Results ###############################
plt.figure(1)
plt.plot(x_axis, traj_array)
plt.xlabel("Time [s]")
plt.ylabel("Angle [deg] ")
plt.legend()
plt.show()

plt.figure(2)
plt.plot(x_axis, traj_derivative_array)
plt.xlabel("Time [s]")
plt.ylabel("Angular velocity [deg/s]")
plt.legend()
plt.show()

plt.figure(3)
plt.plot(x_axis, traj_accn_array)
plt.xlabel("Time [s]")
plt.ylabel("Angular acceleration [deg/s^2]")
plt.legend()
plt.show()

plt.figure(3)
plt.plot(x_axis, traj_jerk_array)
plt.xlabel("Time [s]")
plt.ylabel("Angular Jerk [deg/s^3]")
plt.legend()
plt.show()




if __name__ == 'main':
    main()




