import navx

ahrs = navx.AHRS.create_i2c()
while(True):
   print(ahrs.getYaw())

