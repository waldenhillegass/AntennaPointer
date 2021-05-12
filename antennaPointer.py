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

   calibrate(imu, matrix)

   while(True):
      tPosLat = 35.3025
      tPosLong = -120.6974
      tPosElv = 471
      #if i % 100 == 0:
      #   pullCords()
      #i += 1
      # tPosLat, tPosLong, tPosElv = get_balloon_gps() 

      imu.printStatus()

      gps.readGPS()
      print(gps)


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
   

def calibrate(imu, matrix):
   complete = False
   quad = 0
   while (not complete):
      imu.printStatus()
      
      dy = imu.getPitch()
      dx = imu.getRoll()
      matrix.updateFromErrors(dx,dy, True)

      if dx < matrix.scale / 3 and dy < matrix.scale:
         imu.pokeMovingAverage()

      if quad == 0:
         if imu.getYaw() > 90:
            quad += 1
      if quad == 1:
         if imu.getYaw() > 180:
            quad += 1
      if quad == 2:
         if imu.getYaw() < 90:
            complete = True
   
      
      


main()
   # Must be in degrees and elev in meters