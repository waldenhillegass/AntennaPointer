from gps import GPS
from matrixBubble import Matrix
from time import sleep
from imu import IMU
from calculations import *
import serial

tPosLat = 35.3025
tPosLong = -120.6974
tPosElv = 471

imu = IMU();
gps = GPS()

scale = int(input("Enter scale: "))
matrix = Matrix(scale)


while(True):


   imu.printStatus()

   gps.readGPS()
   print(gps)

   sweepElv = calcAngles(gps.getLatitude(), gps.getLongitude(), gps.elevation, tPosLat, tPosLong, tPosElv)
   dx = sweepElv[0] - imu.sensor.euler[0]
   dy = sweepElv[1] - imu.sensor.euler[1]

   print(sweepElv)

   if(dy > 360):
      dx = dx - 360
   if(dy < -360):
      dx = dx + 360
   
   print(f"dy = {dy}")
   print(f"dx = {dx}")

   matrix.updateFromErrors(dx,dy)
   sleep(.1)


# Must be in degrees and elev in meters



