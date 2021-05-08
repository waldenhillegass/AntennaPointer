import board
import adafruit_bno055
import busio

class IMU:
   def __init__ (self):
      i2c = busio.I2C(board.SCL, board.SDA)
      self.sensor = adafruit_bno055.BNO055_I2C(i2c)

   def printStatus(self):
      print("Magnetometer (microteslas): {}".format(self.sensor.magnetic))
      print("Euler angle: {}".format(self.sensor.euler))
      print()

   def calibrate(self):
      self.sensor
 


