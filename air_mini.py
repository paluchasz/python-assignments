USER = "Szymon Palucha"
USER_ID = "ggjv86"

"put doc string here"
def trajectory (launch_speed, launch_angle_deg, num_samples):
  #launch_speed is the initial speed of the air sampling projectile
  #launch_angle_deg is the angle in degrees from the horizontal at which the air sampling projectile is launched
  #num_samples is 
  launch_speed=raw_input('enter launch_speed')
  
  import numpy
  x = numpy.array(num_samples, dtype=float)
  y = numpy.array(num_samples, dtype=float)
  t = numpy.array(num_samples, dtype=float)

x = launch_speed*numpy.cos(launch_angle_deg)*t
y = launch_speed*numpy.sin(launch_angle_deg)*t-0.5*9.81*t^2
t = (2*y/g)**0.5

print x
print y
print t

if__name__="__main__"
def simplePlot(xVals,yVals):
  import matplotlib.pyplot as pyplot
  pyplot.figure()
  pyplot.plot(xVals, yVals)
  pyplot.xlabel('x (m)')
  pyplot.ylabel('y (m)')
  pyplot.show()
  