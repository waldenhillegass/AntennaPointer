import board
import adafruit_bno055
import busio
import math
from calculations import *
class IMU:
   def __init__ (self):
      i2c = busio.I2C(board.SCL, board.SDA)
      self.sensor = adafruit_bno055.BNO055_I2C(i2c)
      self.rollingAverage = []


   def printStatus(self):
      print("Magnetometer (microteslas): {}".format(self.sensor.magnetic))
      print("Euler angle: {}".format(self.sensor.euler))
      print("Compass angle: {}".format(self.magneticNorth()))
      print()
   
   def getAverageOffset(self):
      return sum(self.rollingAverage) / len(self.rollingAverage)
   
   def pokeMovingAverage(self):
      offset = dTheta(self.magneticNorth(), self.sensor.euler[0])
      self.rollingAverage.append(offset)
      if(len(self.rollingAverage) > 100):
         self.rollingAverage.pop(0)

   def getHeading(self):
      heading = dTheta(self.sensor.euler[0], getAverageOffset())
      return heading
   
   def magneticNorth(self):
      y = self.sensor.magnetic[0]
      x = self.sensor.magnetic[1]

      if x != 0:
         angle = math.atan(y/x)
      elif y > 0:
         angle = 0
      else:
         angle = 180
      angle *= -57.2958
      angle += 12.6 # declination angle

      if angle < 0: 
         angle = 360 + angle
      
      return angle