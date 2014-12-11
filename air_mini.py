'''This Module returns three one dimensional arrays for vertical and horizontal positions of the projectile at equal time intervals'''
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

def simplePlot(xVals,yVals):
  import matplotlib.pyplot as pyplot
  pyplot.figure()
  pyplot.plot(xVals, yVals)
  pyplot.xlabel('x (m)')
  pyplot.ylabel('y (m)')
  pyplot.show()
  
if __name__=='__main__':
  print 'test plot'
  tuples = trajectory(9.81,45,11)
  print tuples[0] #x
  print tuples[1] #y
  print tuples[2] #time
  simplePlot(tuples[0],tuples[1])
