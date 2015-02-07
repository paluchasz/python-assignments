USER = "Szymon Palucha"
USER_ID = "ggjv86"

def trajectory (launch_speed, launch_angle_deg, num_samples):
  ''' This method creates three arrays for x y and t. It then uses suvat equations to add values to these arrays'''
  #launch_speed is the initial speed of the air sampling projectile
  #launch_angle_deg is the angle in degrees from the horizontal at which the air sampling projectile is launched
  #num_samples is the number of time samples distributed evenly over the time of flight 

  import numpy
  import math

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
	
	import numpy
	import math
	
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
	
if __name__=='__main__':  
	# call compare_trajectores function with given parameters
	compare_trajectories(9.81, 45, 200, 5, -9.81, 0.43)



