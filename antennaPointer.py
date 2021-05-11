from gps import GPS
from matrixBubble import Matrix
from time import sleep
from imu import IMU
from calculations import *
import serial

# GPS Imports
from time import gmtime, strftime
import sqlite3
import serial
from sqlite3 import Error
import json
import logging

# tPosLat = 35.3025
# tPosLong = -120.6974
# tPosElv = 471

# Read data from serial
def get_balloon_gps():
   payload = ser.readline()
    prstrip = payload.rstrip().decode('utf8')
    if len(prstrip) > 0:
      print(prstrip)
      try:
        p = json.loads(prstrip)
      except:
         print(prstrip)
         print("Invalid Packet")
   return p['latitude'], p['longitude'], p['altitude']

imu = IMU()
gps = GPS()

scale = int(input("Enter scale: "))
matrix = Matrix(scale)


while(True):
   imu.printStatus()

   gps.readGPS()
   print(gps)

   tPosLat, tPosLong, tPosElv = get_balloon_gps() 

   sweepElv = calcAngles(gps.getLatitude(), gps.getLongitude(), gps.elevation, tPosLat, tPosLong, tPosElv)

   try:
      dx = sweepElv[0] - imu.sensor.euler[0]
      dy = sweepElv[1] - imu.sensor.euler[2]
      dx *= -1

      print(sweepElv)

      if dx < -180:
         dx += 360
      if dx > 180:
         dx -= 360
      print(f"dy = {dy}")
      print(f"dx = {dx}")

   except Exception as e:
      print("IMU READ ERROR")
      print(e)


   matrix.updateFromErrors(dx,dy)
   sleep(.1)


# Must be in degrees and elev in meters



