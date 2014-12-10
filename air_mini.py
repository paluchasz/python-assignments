USER = "Szymon Palucha"
USER_ID = "ggjv86"

"put doc string here"
def trajectory (launch_speed, launch_angle_deg, num_samples):
  #launch_speed is the initial speed of the air sampling projectile
  #launch_angle_deg is the angle in degrees from the horizontal at which the air sampling projectile is launched
  #num_samples is 
  
  import numpy
  x = numpy.arange(num_samples, dtype=float)
  y = numpy.arange(num_samples, dtype=float)
  time = numpy.arange(num_samples, dtype=float)
  
  t_earth = 2*launch_speed*numpy.sin(launch_angle_deg)/9.81
  dt = t_earth/num_samples

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
  # launch_speed=raw_input('enter launch_speed')
  tuples = trajectory(50,45,50)
  print tuples[0] #x
  print tuples[1] #y
  #print tuples[2] #time
  simplePlot(tuples[0],tuples[1])
