import board
import neopixel
import atexit
import time

# This class controls the 8x8 matrix of LED that displays how to move
# the antenna. It holds the neoPixel object and maps error to the matrix
# as a 2x2 spot of lit LEDs

class Matrix:
   # scale is the beam width of the antenna
   def __init__(self, scale):
      self.pixels = neopixel.NeoPixel(board.D18, 64)
      self.gpsLight = False
      self.scale = scale
      atexit.register(self.clear)
   
   def updateFromErrors(self, dx, dy, calibrateMode = False):
      graph = [ [False]*8 for i in range(8)]
      x = round((dx / self.scale * 3) + 3)
      x = max(0, min(6, x))

      y = round((dy / self.scale * 3) + 3)
      y = max(0, min(6, y))

      print(f'X: {x}')
      print(f'Y: {y}')

      if (calibrateMode):
         graph[0][0] = True
         graph[0][7] = True
         graph[7][0] = True
         graph[7][7] = True


      graph[x][y] = True
      graph[x + 1][y] = True
      graph[x][y + 1] = True
      graph[x + 1][y + 1] = True
      
      self.setMatrix(graph)
      
   def setMatrix(self, matrix):
      x = 0
      y = -1
      for i in range(0, 64):
         if i % 8 == 0:
            y += 1
            x = 0
         if matrix[x][y]:
            if (x == 3 or x == 4) and (y == 3 or y == 4):
               self.pixels[i] = (0, 100, 0)
            else:
               self.pixels[i] = (100, 0, 0)
         else:
            if (x == 3 or x == 4) and (y == 3 or y == 4):
               self.pixels[i] = (10, 10, 0)
            else: 
               self.pixels[i] = (0, 0, 0)
         x += 1
      self.pixels[0] = (0, 0, 50)
      self.pixels.show()

   def clear(self):
      self.pixels.fill((0,0,0))
      self.pixels.show()

   def toggleStatusIndicator(self):
      self.gpsLight = not self.gpsLight
      if(self.gpsLight):
         self.pixels[0] = (50, 0, 0)
      else:
         self.pixels[0] = (0, 0, 0)
   
   def strobeRed(self):
      self.toggleStatusIndicator()
      time.sleep(.1)
      self.toggleStatusIndicator()
      time.sleep(.1)
      self.toggleStatusIndicator()
      time.sleep(.1)
      self.toggleStatusIndicator()

