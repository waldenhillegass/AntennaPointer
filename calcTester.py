from calculations import *
import numpy

# this is a driver script to test the calculations that relate the cordinates to each other

def main():
   lam = 20
   phi = 30

   x = 20
   y = 20
   z = 45
   print(tiltCorrectCalcs(lam, phi, x,y,z))

   


main()
   