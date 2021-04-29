from navx import AHRS
import time

ahrs = AHRS.create_i2c()
while(True):
   print(ahrs.getYaw())
   time.sleep(1)

