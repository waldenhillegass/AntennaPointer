from navx import NAVX
from gps import GPS
from matrixBubble import Matrix
from time import sleep
import serial

imu = NAVX(1);
gps = GPS()

scale = int(input("Enter scale: "))
matrix = Matrix(scale)


while(True):
   print(imu)

   gps.readGPS()
   print(gps)

   x = float(input("Enter X error:"))
   y = float(input("Enter Y error:"))
   matrix.updateFromErrors(x,y)