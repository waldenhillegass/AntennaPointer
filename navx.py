# this file contains a simplified driver for the Kuali Labs NAVx Micro IMU 
# https://pdocs.kauailabs.com/navx-mxp/advanced/register-protocol/
from smbus import SMBus
from enum import Enum

# i2c address
DEV_ADDR = 0x32

#register addresses
WHO_AM_I = 0x00
STATUS = 0x08
YAW_LOW = 0x16
PITCH_LOW = 0x18

class NAVX:
   class Status(Enum):
      INITALIZING = 0
      SELFTEST = 1
      ERROR = 2
      CALIBRATING = 3
      NORMAL = 4

   def __init__(self, channel):
      self.bus = SMBus(channel)
      test = self.bus.read_byte_data(DEV_ADDR, WHO_AM_I)
      if test == DEV_ADDR:
         print("NAVX succesfully connected")
      else:
         print("NAVX failed to init")
   
   def getStatus(self):
      return self.bus.read_byte_data(DEV_ADDR, STATUS)
      
   def getYaw(self):
      # sensor returns hundreths
      number = self.bus.read_byte_data(DEV_ADDR, YAW_LOW)
      number = int.from_bytes(number, byteorder='little', signed=True)
      return number / 100

   def getPitch(self):
      number = self.bus.read_byte_data(DEV_ADDR, PITCH_LOW)
      number = int.from_bytes(number, byteorder='little', signed=True)
      return number / 100

   def __str__(self):
      sting = f'status: {self.getStatus()}\n Yaw: {self.getYaw()}\n Pitch: {self.getPitch}'
      return sting
