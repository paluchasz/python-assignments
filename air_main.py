USER = "Szymon Palucha"
USER_ID = "ggjv86"

import numpy
import math

def trajectory (launch_speed, launch_angle_deg, num_samples):
        ''' This method creates three arrays for x y and t. It then uses suvat equations to add values to these arrays'''
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
	#print x,y
	#print x_drag,y_drag
	pyplot.figure()
	pyplot.plot(x,y)
	pyplot.plot(x_drag,y_drag)
	pyplot.xlabel('x(m)')
	pyplot.ylabel('y(m)')
	pyplot.title('Vertical distance against horizontal distance for drag and no drag')
	pyplot.text(7,0,'k_drag='+str(k))
	pyplot.show()

#Task3
def impact_drag(launch_speed, launch_angle_deg, m, g=-9.81, k=0.043):

	#Make the initial time equal the launch_speed so that the function converges to the correct time
	#i.e the time when the projectile touches the Earth for the second time
        t = launch_speed

	#This function will calculate x-f(x)/f'(x) for the Newton Raphson method
	launch_angle_deg = launch_angle_deg*math.pi/180
	initial_vert_speed = launch_speed*numpy.sin(launch_angle_deg)
	initial_horiz_speed = launch_speed*numpy.cos(launch_angle_deg)
	# The equation below equals 0 when y is 0 and it gives the solutions 
	# for the time when it hits the ground
	y_t = m*g*t+m*(initial_vert_speed-m*g/k)*(1-numpy.exp(-k*t/m))
 	y_first_deriv = m*g+(k*initial_vert_speed-m*g)*numpy.exp(-k*t/m)
	
	t_imp = t - y_t/y_first_deriv
	
	#Do the loop 20 times to give the Newton raphson enough steps to converge to a time to 11dp
	for l in range(0, 20):
		y_t = m*g*t_imp+m*(initial_vert_speed-m*g/k)*(1-numpy.exp(-k*t_imp/m))
 		y_first_deriv = m*g+(k*initial_vert_speed-m*g)*numpy.exp(-k*t_imp/m)
		t_imp = t_imp - y_t/y_first_deriv
	
	x_imp = m*initial_horiz_speed*(1-numpy.exp(-k*t_imp/m))/k

	return x_imp, t_imp
#Task4
def plot_impact_drag(launch_speed, launch_angle_deg, m, g=-9.81, k=0.043):
	import matplotlib.pyplot as plt
	from mpl_toolkits.mplot3d import Axes3D

	u = launch_speed
	b = launch_angle_deg

	fig = plt.figure()
	diag3D = fig.add_subplot(111, projection = '3d')
		
	U, B = numpy.meshgrid(u,b)
	zs = numpy.array([impact_drag(u, b, m, g, k)[0] for u, b in zip(numpy.ravel(U), numpy.ravel(B))])
	Z = zs.reshape(U.shape)
	
	diag3D.plot_surface(U, B, Z)
	diag3D.set_xlabel('launch_speed(m/s)')
	diag3D.set_ylabel('launch_angle_deg')
	diag3D.set_zlabel('x_imp')
	
	plt.show()

	#for i in range(0,len(launch_speed)):
		#x_imp, t_imp = impact_drag(launch_speed[i], launch_angle_deg[i], m, g, k)


	#the below doesnt work	
	#plt.figure()
	#plt.plot(launch_speed, launch_angle_deg, x_imp)
	#plt.xlabel('launch_speed(m/s)')
	#plt.ylabel('launch_angle_deg')
	#plt.zlabel('x_imp')
	#plt.title('3D graph')
	#plt.show()

if __name__=='__main__':  
	# Task2: call compare_trajectores function with given parameters
	#compare_trajectories(9.81, 45, 200, 5, -9.81, 0.043)
	
	# Task3: call time_y0 function with given parameter
        launch_speed = 9.81
        mass = 5
	print impact_drag(launch_speed, 45, mass) 
	compare_trajectories(launch_speed, 45, 2000, mass)
        #launch_speed = 3*10^3
        #mass = 0.005
	#print impact_drag(launch_speed, 45,mass) 
	#compare_trajectories(launch_speed, 45, 2000, mass)
	
	speeds = numpy.arange(1, 90, 1)
	angles = numpy.arange(1, 90, 1)
	plot_impact_drag(speeds, angles,50)
