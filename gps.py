import time
import serial

class GPS:
   def __init__(self):
      self.ser = set_up_gps()
      self.ser.flush()
      
      self.long = {
         "degrees":0,
         "minutes":0.0,
      }
      self.lat = {
         "degrees":0,
         "minutes":0.0,
         "time":0
      }

   def set_up_gps(self):
      ser = serial.Serial(
        port = '/dev/ttyS0',
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout=1
      )
      return ser
   def readGPS(self):
      newData = False
      while(ser.in_waiting() > 0):
         data = str(ser.read_until(), 'UTF-8')
         if data.startswith("$GPGLL"):
            #$GPGLL,3517.98388,N,12040.57134,W,061920.00,A,D*73\r\n
            #0      7 9      1   1  2       3
            #                6   9  2       0
            self.long["degrees"] = int(data[7:9])
            self.long["minutes"] = float(data[9:17])
            self.long["time"] = time.time()

            self.lat["degrees"] = int(data[19:22])
            self.long["minutes"] = float(data[22:30])
            self.long["time"] = time.time()
            newData = True
      return newData
            

   # Returns a dictionary with degrees and minutes
   def getLongitude(self):
      return self.long
   
   def getLatitude(self):
      return self.lat

   def __str__(self):
      return f'longitude: {self.long}, latitude: {self.long}'
