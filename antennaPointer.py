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

   x = float(input("Enter X error:"))
   y = float(input("Enter Y error:"))
   matrix.updateFromErrors(x,y)


# Must be in degrees and elev in meters



