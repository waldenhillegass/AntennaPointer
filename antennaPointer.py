from navx import NAVX
from gps import GPS
from time import sleep
import serial

imu = NAVX(1);
gps = GPS()

while(True):
   sleep(1)
   print(imu)

   gps.readGPS()
   print(gps)