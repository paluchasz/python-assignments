#!/usr/bin/env python

def simplePlot(xVals, yVals):
  """ simplePlot(xVals, yVals) will plot lines from passed x and y values """
  import matplotlib.pyplot as pyplot
  pyplot.figure()
  pyplot.plot(xVals, yVals)
  pyplot.xlabel('x (m)')
  pyplot.ylabel('y (m)')
  pyplot.show()

def returnTuples(array):
  """ funny function to return a tuple with two values
	value one an passed array and 
	value two an array of powers from value one """

  # range will generate a tuple of integers such as 0,1,2,3,...,num
  power = range(0,len(array))
 
  # take every element from array and create its power
  for i in range (len(array)):
    # write powers
    power[i] = array[i]**2
 
  # return a tuple with array and powwer values
  return ( array, power )

if __name__=='__main__':
  """ main programm to test simplePlot function 
	define two tuples with X and Y values
	call simplePlot function with X and Y tuples """ 
  print 'test plot'
  
  #This section could print a plot if # removed
  #tupleX = (1,2,3,4,5)
  #tupleY = (1,4,9,16,25)
  #simplePlot(tupleX,tupleY)
  
  #generate two tuples
  array = [1,2,3,4,5]
  tuples = returnTuples(array)
  #print simple plot from tuples values
  simplePlot(tuples[0],tuples[1])
