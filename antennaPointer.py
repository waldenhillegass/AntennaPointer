from navx import AHRS

ahrs = AHRS.create_i2c()
while(True):
   print(ahrs.getYaw())

