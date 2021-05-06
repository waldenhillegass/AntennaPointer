from gps import GPS
from matrixBubble import Matrix
from time import sleep
from imu import IMU
import serial

imu = IMU();
gps = GPS()

scale = int(input("Enter scale: "))
matrix = Matrix(scale)


while(True):
   imu.printStatus()

   gps.readGPS()
   print(gps)

   x = imu.sensor.euler[0]
   y = imu.sensor.euler[1]
   matrix.updateFromErrors(x,y)
   sleep(.5)


# Must be in degrees and elev in meters



