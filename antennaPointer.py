from navx import NAVX
from time import sleep

imu = NAVX(1);


while(True):
   sleep(1)
   print(imu)


