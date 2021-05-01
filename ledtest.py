import board
import neopixel
from time import sleep
pixels = neopixel.NeoPixel(board.D18, 30)

while(True):
   pixels[0] = (255, 0, 0)
   pixels.show()
   sleep(3)
   pixels.fill((0,128,0))
   pixels.show()
   sleep(3)
