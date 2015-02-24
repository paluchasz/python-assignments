'''The module in task 1 creates three arrays for x y and t for motion with drag and without drag and it adds values to the arrays.'''
'''The module in task 2 draws two graphs (one with drag and one without drag) for the vertical distance against horizontal difference.'''
'''The module in task 3 uses the Newton Raphson method to calculate the time for when the projectle hits the ground, then the horizontal distance is calculated'''
'''The module in task 4 draws a 3D graph of the horizontal impact distance travelled against the launch speed and launch angle'''
USER = "Szymon Palucha"
USER_ID = "ggjv86"

import numpy
import math

#Task 1
def trajectory (launch_speed, launch_angle_deg, num_samples):
        #launch_speed is the initial speed of the air sampling projectile
        #launch_angle_deg is the angle in degrees from the horizontal at which the air sampling projectile is launched
        #num_samples is the number of time samples distributed evenly over the time of flight 


        launch_angle_deg = launch_angle_deg*math.pi/180
        #This is to convert the angle to radians so the sine/cosine functions can be applied
        x = numpy.arange(num_samples, dtype=float)
        y = numpy.arange(num_samples, dtype=float)
        time = numpy.arange(num_samples, dtype=float)

        t_earth = 2*launch_speed*numpy.sin(launch_angle_deg)/9.81
        #This equation gives the total time of flight
        dt = t_earth/(num_samples-1)
        #dt is the time interval

        for t in range(0,num_samples):
          time[t] =dt*t
          x[t] = launch_speed*numpy.cos(launch_angle_deg)*time[t]
          y[t] = launch_speed*numpy.sin(launch_angle_deg)*time[t]-0.5*9.81*time[t]**2

        return(x,y,time)

def trajectory_drag(launch_speed, launch_angle_deg, num_samples, m, g=-9.81, k=0.043):
	#launch_speed is the initial speed of the air sampling projectile
	#launch_angle_deg is the angle in degrees from the horizontal at which the air sampling projectile is launched
	#num_samples is the number of time samples distributed evenly over the time of flight 
	#m is the projectile mass in kg
	#g is the acceleration due to gravity
	

	
	launch_angle_deg = launch_angle_deg*math.pi/180
	#This is to convert the angle to radians so the sine/cosine functions can be applied
	x = numpy.arange(num_samples, dtype=float)
	y = numpy.arange(num_samples, dtype=float)
	time = numpy.arange(num_samples, dtype=float)
   

	t_earth = -2*launch_speed*numpy.sin(launch_angle_deg)/g
	#This equation gives the total time of flight
	dt = t_earth/(num_samples-1)
	#dt is the time interval
	
	initial_horiz_speed = launch_speed*numpy.cos(launch_angle_deg)
	initial_vert_speed = launch_speed*numpy.sin(launch_angle_deg)
	
	for t in range(0,num_samples):
		time[t] =dt*t
		x[t]=m*initial_horiz_speed*(1-numpy.exp(-k*time[t]/m))/k
		y[t]=1/k*(m*g*time[t]+m*(initial_vert_speed-m*g/k)*(1-numpy.exp(-k*time[t]/m)))
	
	return(x,y,time)

#Task2
def compare_trajectories(launch_speed, launch_angle_deg, num_samples, m, g=-9.81, k=0.043):
	#This function calculates and plots a graph for chosen parameters
	import matplotlib.pyplot as pyplot
	(x,y,time) = trajectory(launch_speed, launch_angle_deg, num_samples)
	(x_drag,y_drag,time) = trajectory_drag(launch_speed, launch_angle_deg, num_samples, m, g, k)
	
	#The below plots the graphs of vertical distance against horizontal distance
	pyplot.figure()
	pyplot.plot(x,y)
	pyplot.plot(x_drag,y_drag)
	pyplot.xlabel('x(m)')
	pyplot.ylabel('y(m)')
	pyplot.title('Vertical distance against horizontal distance for drag (green line) and no drag (blue line)')
	pyplot.show()

#Task3
def impact_drag(launch_speed, launch_angle_deg, m, g=-9.81, k=0.043):

	#Make the initial time equal the launch_speed so that the function converges to the correct time
	#i.e the time when the projectile touches the Earth for the second time instead of t=0
        t = launch_speed

	#This function will calculate x-f(x)/f'(x) for the Newton Raphson method
	launch_angle_deg = launch_angle_deg*math.pi/180
	initial_vert_speed = launch_speed*numpy.sin(launch_angle_deg)
	initial_horiz_speed = launch_speed*numpy.cos(launch_angle_deg)
	#The equation below equals 0 when y is 0 and it gives the solutions 
	#for the time when it hits the ground
	y_t = m*g*t+m*(initial_vert_speed-m*g/k)*(1-numpy.exp(-k*t/m))
 	y_first_deriv = m*g+(k*initial_vert_speed-m*g)*numpy.exp(-k*t/m)
	
	#This is the Newton Raphson method:
	t_imp = t - y_t/y_first_deriv
	
	#Do the for loop 20 times to give the Newton raphson enough steps to converge to a time to 11dp
	for l in range(0, 20):
		y_t = m*g*t_imp+m*(initial_vert_speed-m*g/k)*(1-numpy.exp(-k*t_imp/m))
 		y_first_deriv = m*g+(k*initial_vert_speed-m*g)*numpy.exp(-k*t_imp/m)
		t_imp = t_imp - y_t/y_first_deriv
	
	x_imp = m*initial_horiz_speed*(1-numpy.exp(-k*t_imp/m))/k

	return x_imp, t_imp
#Task4
def plot_impact_drag(launch_speed, launch_angle_deg, m, g=-9.81, k=0.043):
	#This function will plot the horizontal impact distance against launch speed and launch angle
	#The below is taken from http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html and it allows a 3D graph to be drawn
	import matplotlib.pyplot as plt
	from mpl_toolkits.mplot3d import Axes3D

	u = launch_speed
	b = launch_angle_deg

	fig = plt.figure()
	diag3D = fig.add_subplot(111, projection = '3d')
		
	U, B = numpy.meshgrid(u,b) #Creates two 2-d arrays of launch speed and launch angle
	zs = numpy.array([impact_drag(v, d, m, g, k)[0] for v, d in zip(numpy.ravel(U), numpy.ravel(B))]) #Creates an array of impact posotion for every combination of launch speed and launch angle
	Z = zs.reshape(U.shape) #Reshapes the array of impact position t the same 2D shape as U and B.
	
	diag3D.plot_surface(U, B, Z)
	diag3D.set_xlabel('launch_speed(m/s)')
	diag3D.set_ylabel('launch_angle_deg')
	diag3D.set_zlabel('x_imp')
	diag3D.set_title('Horiztontal impact distance against launch speed and launch angle')
	plt.show()

if __name__=='__main__':  
	# Task2: call compare_trajectores function with given parameters
	#compare_trajectories(9.81, 45, 200, 5, -9.81, 0.043)
	
	# Task3: call time_y0 function with given parameter
        launch_speed = 9.81
        mass = 1
	print impact_drag(launch_speed, 45, mass) 
	compare_trajectories(launch_speed, 45, 2000, mass)
        #launch_speed = 3*10^3
        #mass = 0.005
	#print impact_drag(launch_speed, 45,mass) 
	#compare_trajectories(launch_speed, 45, 2000, mass)
	
	speeds = numpy.arange(1, 90, 1)
	angles = numpy.arange(1, 90, 1)
	plot_impact_drag(speeds, angles,50)
