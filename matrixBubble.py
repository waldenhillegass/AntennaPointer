import board
import neopixel
import atexit

class Matrix:
   def __init__(self, scale):
      self.pixels = neopixel.NeoPixel(board.D18, 64)
      self.gpsLight = False
      self.scale = scale
      atexit.register(self.clear)
   
   def updateFromErrors(self, dx, dy):
      graph = [[False] * 8] * 8
      x = round((dx / self.scale * 3) + 3)
      x = max(6, min(0, x))

      y = round((dx / self.scale * 3) + 3)
      y = max(6, min(0, x))

      print(f'X: {x}')
      print(f'Y: {y}')


      graph[x][y] = True
      #graph[x + 1][y] = True
      #graph[x][y + 1] = True
      #graph[x + 1][y + 1] = True
      
      for row in graph:
         print(row)

      self.setMatrix(graph)
      
   def setMatrix(self, matrix):
      x = 0
      y = -1
      for i in range(0, 64):
         if i % 8 == 0:
            y += 1
            x = 0
         if matrix[x][y]:
            self.pixels[i] = (50, 0, 0)
         else:
            self.pixels[i] = (0, 0, 0)
         x += 1
      self.pixels.show()

   def clear(self):
      self.pixels.fill((0,0,0))
      self.pixels.show()

   def toggleGpsIndicator(self):
      self.gpsLight = not self.gpsLight
      if(self.gpsLight):
         self.pixels[0] = (255, 0, 0)
      else:
         self.pixels[0] = (0, 0, 0)
