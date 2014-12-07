USER = "Szymon Palucha"
USER_ID = "ggjv86"

def trajectory (launch_speed, launch_angle_deg, num_samples):
  import numpy
  x = numpy.array(num_samples, dtype=float)
  y = numpy.array(num_samples, dtype=float)
  t = numpy.array(num_samples, dtype=float)

  x = launch_speed*cos(launch_angle_deg)*t
  y = launch_speed*sin(launch_angle_deg)*t-0.5*9.81*t^2

