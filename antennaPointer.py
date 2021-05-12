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

def main():
   imu = IMU()
   gps = GPS()

   scale = int(input("Enter scale: "))
   matrix = Matrix(scale)


   while(True):
      tPosLat = 35.3025
      tPosLong = -120.6974
      tPosElv = 471
      # tPosLat, tPosLong, tPosElv = get_balloon_gps() 

      imu.printStatus()

      gps.readGPS()
      print(gps)
      imu.pokeMovingAverage()


      sweepElv = calcAngles(gps.getLatitude(), gps.getLongitude(), gps.elevation, tPosLat, tPosLong, tPosElv)

      
      dx = sweepElv[0] - imu.getHeading()
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