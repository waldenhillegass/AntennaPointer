import time
import serial

# assumes we are operating in the north and west hemispheres (sue me)
class GPS:
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

   def __init__(self):
      self.ser = self.set_up_gps()
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
      self.elevation = -1

   
   def readGPS(self):
      newData = False
      try:
         while(self.ser.in_waiting > 0):
            data = str(self.ser.read_until(), 'UTF-8')
            if data.startswith("$GPGLL"):
               #$GPGLL,3517.98388,N,12040.57134,W,061920.00,A,D*73\r\n
               #0      7 9      1   1  2       3
               #                6   9  2       0
               self.lat["degrees"] = int(data[7:9])
               self.lat["minutes"] = float(data[9:17])
               self.lat["time"] = time.time()

               self.long["degrees"] = -int(data[20:23])
               self.long["minutes"] = float(data[23:31])
               self.long["time"] = time.time()
               newData = True
            
            if data.startswith("$GPGGA"):
               arr = data.split(",")
               self.elevation = float(arr[9])

      except Exception as e:
         self.ser.close()
         self.ser = self.set_up_gps()
         print(e)
         print("GPS READ ERROR")
         return False
      return newData
            

   # Returns decimal degrees of current longitude
   def getLongitude(self):
      decimalDegrees = float(self.long["degrees"]) + float(self.long["minutes"]) / 60
      return float(decimalDegrees)

   def getLatitude(self):
     decimalDegrees = float(self.lat["degrees"]) - float(self.lat["minutes"]) / 60
     return float(decimalDegrees)

   def __str__(self):
      return f'longitude: {self.getLongitude()}, latitude: {self.getLatitude()}, elvation: {self.elevation}'
