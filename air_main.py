USER = "Szymon Palucha"
USER_ID = "ggjv86"

def trajectory_drag(launch_speed,launch_angle_deg, num_samples, m, g, k):
	#launch_speed is the initial speed of the air sampling projectile
	#launch_angle_deg is the angle in degrees from the horizontal at which the air sampling projectile is launched
	#num_samples is the number of time samples distributed evenly over the time of flight 
	#m is the projectile mass in kg
	#g is the acceleration due to gravity
	
	import numpy
	import math
	
	g=-9.81, k=0.043
	
	launch_angle_deg = launch_angle_deg*math.pi/180
	#This is to convert the angle to radians so the sine/cosine functions can be applied
	x = numpy.arange(num_samples, dtype=float)
    y = numpy.arange(num_samples, dtype=float)
	time = numpy.arange(num_samples, dtype=float)
   

 t_earth = -2*launch_speed*numpy.sin(launch_angle_deg)/g
	#This equation gives the total time of flight
	dt = t_earth/(num_samples-1)
	#dt is the time interval
	
	
  for t in range(0,num_samples):
    time[t] =dt*t
	x[t]=m*launch_speed*numpy.cos(launch_angle_deg)*(1-numpy.exp(-k*time[t]/m))/k
	y[t]=1/k*(m*g*time[t]+m*(launch_speed*numpy.sin(launch_angle_deg)-m*g/k)*(1-numpy.exp(-k*time[t]/m)))
	
        	

