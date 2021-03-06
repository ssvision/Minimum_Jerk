import matplotlib.pyplot as plt
import numpy as np



current = np.array([3,5])   #current value of trajectory (initial value)
setpoint = np.array([6,9]) #final setpoint value of trajectory (final value)
move_time = 0.5 #amoun of time trajectory should take to reach from current value to final value
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
plt.plot(x_axis, traj_array[:,0],label='X-Position')
plt.plot(x_axis, traj_array[:,1],label='Y-Position')
plt.xlabel("Time [s]")
plt.ylabel("Position [m] ")
plt.legend()
plt.show()

plt.figure(2)
plt.plot(x_axis, traj_derivative_array[:,0], label='X-Velocity')
plt.plot(x_axis, traj_derivative_array[:,1], label='Y-Velocity')
plt.xlabel("Time [s]")
plt.ylabel("Velocity [m/s]")
plt.legend()
plt.show()

plt.figure(3)
plt.plot(x_axis, traj_accn_array[:,0], label='X-Acceleration')
plt.plot(x_axis, traj_accn_array[:,1], label='Y-Acceleration')
plt.xlabel("Time [s]")
plt.ylabel("Acceleration [m/s^2]")
plt.legend()
plt.show()

plt.figure(3)
plt.plot(x_axis, traj_jerk_array[:,0], label='X-Jerk')
plt.plot(x_axis, traj_jerk_array[:,1], label='Y-Jerk')
plt.xlabel("Time [s]")
plt.ylabel("Jerk [deg/s^3]")
plt.legend()
plt.show()

plt.figure(4)
plt.plot(traj_array[:,0], traj_array[:,1], label='XY trajectory')
plt.xlabel("X axis[m]")
plt.ylabel("Y axis[m]")
plt.legend()
plt.show()


if __name__ == 'main':
    main()




