import atexit
import board
import neopixel
from time import sleep

def clearStrip():
   pixels.fill((0,0,0))
   pixels.show()

pixels = neopixel.NeoPixel(board.D18, 64)
atexit.register(clearStrip)
while(True):
   pixels[0] = (255, 0, 0)
   pixels.show()
   sleep(3)
   pixels.fill((0,100,0))
   pixels.show()
   sleep(3)

