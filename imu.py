import board
import adafruit_bno055
import busio
import math
from calculations import *
import numpy as nPi

class IMU:
   def __init__ (self):
      i2c = busio.I2C(board.SCL, board.SDA)
      self.sensor = adafruit_bno055.BNO055_I2C(i2c)
      self.rollingAverage = []
      self.lastYaw = 0
      self.lastPitch = 0
      self.lastRoll = 0

   def printStatus(self):
      print("Magnetometer (microteslas): {}".format(self.sensor.magnetic))
      print("Euler angle: {}".format(self.sensor.euler))
      print("Heading: {}".format(self.getHeading()))
      print("Unadjusted Compass angle: {}".format(self.magneticNorth()))
      #print("Adjusted Compass angle: {}".format(self.tiltCorrectedCompass()))
      print("Average offset: {}".format(self.getAverageOffset()))
      print()
   def getAverageOffset(self):
      if len(self.rollingAverage) == 0:
         return 0
      return sum(self.rollingAverage) / len(self.rollingAverage)
   
   def pokeMovingAverage(self):
      offset = dTheta(self.magneticNorth(), self.getYaw())
      self.rollingAverage.append(offset)
      if(len(self.rollingAverage) > 100):
         self.rollingAverage.pop(0)

   def getHeading(self):
      heading = self.getYaw() + self.getAverageOffset()
      if heading > 360:
         heading -= 360
      if heading < 0:
         heading += 360
      return heading

   def getYaw(self):
      yaw = self.sensor.euler[0]
      if yaw is not None:
         self.lastYaw = yaw
      else:
         print("IMU READ ERROR")
      return self.lastYaw
   
   def getPitch(self):
      pitch = self.sensor.euler[2]
      if pitch is not None:
         self.lastPitch = pitch
      else:
         print("IMU READ ERROR")
      return self.lastPitch
   
   def getRoll(self):
      roll = self.sensor.euler[1]
      if roll is not None:
         self.lastRoll = roll
      else:
         print("IMU READ ERROR")
      return self.lastRoll

   def magneticNorth(self):
      y = -self.sensor.magnetic[0]
      x = -self.sensor.magnetic[1]
      z = self.sensor.magnetic[2]

      angle = math.atan2(y, x)
      angle *= -57.2958
      angle += 12.6 # declination angle

      if angle < 0: 
         angle = 360 + angle
      return angle

   def tiltCorrectedCompass(self):
      phi = self.getRoll()
      lam = self.getPitch()

      x = self.sensor.magnetic[0]
      y = self.sensor.magnetic[1]
      z = self.sensor.magnetic[2]

      return tiltCorrectCalcs(lam, phi, x,y,z)
      
