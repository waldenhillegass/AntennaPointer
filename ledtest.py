import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30)

while(True):
   pixels[0] = (255, 0, 0)
   sleep(30)
   pixels.fill((0,128,0))
   sleep(30)
