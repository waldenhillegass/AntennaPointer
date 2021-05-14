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

UPDATE_INTERVAL = 60

def main():
   imu = IMU()
   gps = GPS()

   scale = 20
   matrix = Matrix(scale)

   authTok = None
   matrix.toggleStatusIndicator()
   try:
      while authTok == None:
         matrix.toggleStatusIndicator()
         authTok = authenticate()

   except Exception as e:
      while True:
         sleep(.1)
         matrix.toggleStatusIndicator()

   calibrate(imu, matrix)
   matrix.clear()
   lastUpdated = 0
   tPosLat = None
   while(True):
      
      if (time.time() - lastUpdated > UPDATE_INTERVAL):
         while(tPosLat is None):
            matrix.toggleStatusIndicator()
            cords = get_balloon_gps(authTok)
            if cords is not None:
               tPosLat, tPosLong, tPosElv = cords
            else:
               matrix.strobeRed()
            lastUpdated = time.time()
            matrix.toggleStatusIndicator()

      imu.printStatus()

      gps.readGPS()
      print(gps)

      print(f'Target long: {tPosLong}, lat: {tPosLat}, alt: {tPosElv}')
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
   

def calibrate(imu, matrix):
   complete = False
   quad = 0
   while (not complete):
      imu.printStatus()

      dy = imu.getPitch()
      dx = imu.getRoll()
      matrix.updateFromErrors(dx,dy, True)

      if dx < matrix.scale / 2 and dy < matrix.scale / 2:
         imu.pokeMovingAverage()

      if quad == 0:
         if imu.getYaw() < 90:
            quad += 1
      if quad == 1:
         if imu.getYaw() > 90 and imu.getYaw() < 180:
            quad += 1
      if quad == 2:
         if imu.getYaw() < 90:
            complete = True
main()
   # Must be in degrees and elev in meters