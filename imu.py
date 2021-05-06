import board
import adafruit_bno055
import busio

class IMU:
   def __init__ (self):
      i2c = busio.I2C(board.SCL, board.SDA)
      self.sensor = adafruit_bno055.BNO055_I2C(i2c)

   def printStatus(self):
      print("Accelerometer (m/s^2): {}".format(self.sensor.acceleration))
      print("Magnetometer (microteslas): {}".format(self.sensor.magnetic))
      print("Gyroscope (rad/sec): {}".format(self.sensor.gyro))
      print("Euler angle: {}".format(self.sensor.euler))
      print("Quaternion: {}".format(self.sensor.quaternion))
      print("Linear acceleration (m/s^2): {}".format(self.sensor.linear_acceleration))
      print("Gravity (m/s^2): {}".format(self.sensor.gravity))
      print()

   def calibrate(self):
      self.sensor
 


