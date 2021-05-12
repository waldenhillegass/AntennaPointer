from gps import GPS
from matrixBubble import Matrix
from time import sleep
from imu import IMU
from calculations import *
from time import gmtime, strftime
import sqlite3
import serial
from sqlite3 import Error
import json
import logging
from balloonLoc import *

def main():
   imu = IMU()
   gps = GPS()

   scale = 20
   matrix = Matrix(scale)

   tok = None
   matrix.toggleStatusIndicator()
   try:
      while tok == None:
         matrix.toggleStatusIndicator()
         tok = authenticate()

   except Exception as e:
      while True:
         sleep(.1)
         matrix.toggleStatusIndicator()

   while(True):
      #if i % 100 == 0:
      #   pullCords()
      #i += 1
      # tPosLat, tPosLong, tPosElv = get_balloon_gps() 

      imu.printStatus()

      gps.readGPS()
      print(gps)
      imu.pokeMovingAverage()


      sweepElv = calcAngles(gps.getLatitude(), gps.getLongitude(), gps.elevation, tPosLat, tPosLong, tPosElv)

      
      dx = 0 - imu.getHeading()
      dy = sweepElv[1] - imu.getPitch()
      dx *= -1

      print(sweepElv)

      if dx < -180:
         dx += 360
      if dx > 180:
         dx -= 360
      print(f"dy = {dy}")
      print(f"dx = {dx}")
      matrix.updateFromErrors(dx,dy)

      #except Exception as e:
      #  print("IMU READ ERROR")
      #  print(e)
      sleep(.1)


main()
   # Must be in degrees and elev in meters