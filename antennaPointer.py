from navx import NAVX

imu = NAVX(1);


while(True):
   sleep(1)
   print(imu)


