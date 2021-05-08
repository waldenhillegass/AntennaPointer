import numpy as nPi
import math

# Contains the math needed to calculate where the antenna needs to point
# when given two sets of cordinates and elevations. 

def geoToEcef(lat, lon, alt):
   earthRadius = 6378137 #m
   earthSemiMinor = 6356752.314245 #m

   f = (earthRadius - earthSemiMinor) / earthRadius

   finf = 1 / f

   sqOfEcentricity = f * (2 - f)
   lambd = nPi.radians(lat)
   phi = nPi.radians(lon)

   s = nPi.sin(lambd)

   n = earthRadius / math.sqrt(1 - (sqOfEcentricity * s * s))

   x = (alt + n ) * nPi.cos(lambd) * nPi.cos(phi)
   y = (alt + n) * nPi.cos(lambd) * nPi.sin(phi)
   z = (alt + (1 - sqOfEcentricity) * n) * nPi.sin(lambd)

   return nPi.matrix([x, y, z])

def calcAngles (mylat, mylon, myelv, blat, blon, belv): 

   myPos = geoToEcef(mylat, mylon, myelv)
   tPos = geoToEcef(blat, blon, belv)
   dPos = nPi.subtract(tPos, myPos)

   dPos = nPi.rot90(dPos, 3)

   lam = nPi.radians(mylat)
   phi = nPi.radians(mylon)

   rot1 = [
      [1, 0,             0],
      [0, -nPi.sin(lam), nPi.cos(lam)],
      [0, nPi.cos(lam), nPi.sin(lam)],
      ]
   rot1 = nPi.matrix(rot1)
   
   rot2 = [
      [-nPi.sin(phi), nPi.cos(phi), 0],
      [nPi.cos(phi), nPi.sin(phi), 0],
      [0,0,1]
   ]
   rot2 = nPi.matrix(rot2)
   
   rots = rot1 * rot2
   pos = rots * dPos

   hyp = math.sqrt([0] * pos[0] + pos[1] * pos[1])

   sweep = nPi.arcsin(pos[0]/hyp)
   elev = nPi.arctan(pos[2]/ hyp)

   sweep *= 57.2958
   elev *= 57.2958

   if (pos[1] < 0):
      sweep = 180 - sweep
   if(pos[1] > 0 and pos[0] < 0):
      sweep = 360 + sweep

   return (float(sweep[0]), float(elev[0]))



