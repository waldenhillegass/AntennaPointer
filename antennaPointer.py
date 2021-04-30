from navx import NAVX
from time import sleep
from serial import Serial

imu = NAVX(1);

def set_up_gps():
     ser = Serial(
        port = '/dev/ttyAMA0',
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout=1
        )
     counter=0
     return ser
gps = set_up_gps()

while(True):
   sleep(1)
   print(imu)

   print(gps.read_until())

  
   


