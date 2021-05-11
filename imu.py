import board
import adafruit_bno055
import busio
import math

class IMU:
   def __init__ (self):
      i2c = busio.I2C(board.SCL, board.SDA)
      self.sensor = adafruit_bno055.BNO055_I2C(i2c)

   def printStatus(self):
      print("Magnetometer (microteslas): {}".format(self.sensor.magnetic))
      print("Euler angle: {}".format(self.sensor.euler))
      print("Compass angle: {}".format(self.magneticNorth()))
      print()

   def magneticNorth(self):
      y = self.sensor.magnetic[0]
      x = self.sensor.magnetic[1]

      angle = math.atan(y/x)
      angle *= 57.2958

      if angle < 0: 
         angle = 360 + angle
      
      return angle



      

      

      


