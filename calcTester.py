from calculations import *
import numpy

# this is a driver script to test the calculations that relate the cordinates to each other

def main():
   myPosLat = 35.28292
   myPosLong = -120.68196
   myPosElv = 90

   tPosLat = 35.3025
   tPosLong = -120.6974
   tPosElv = 471

   print(calcAngles(myPosLat, myPosLong, myPosElv, tPosLat, tPosLong, tPosElv))


main()

   
   