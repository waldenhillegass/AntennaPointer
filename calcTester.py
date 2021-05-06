from calculations import *
import numpy

# this is a driver script to test the calculations that relate the cordinates to each other

def main():
   myPosLat = 35.28292
   myPosLong = -120.68196
   myPosElv = 289.56

   tPosLat = 35.30173
   tPosLong = -120.69650
   tPosElv = 471.2208

   print(calcAngles(myPosLat, myPosLong, myPosElv, tPosLat, tPosLong, tPosElv))


main()

   
   