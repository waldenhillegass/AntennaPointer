import requests
import time
import os

PAPA_ID = "AQUILA01"

def authenticate():
   usrPass = {
     "Username": os.getenv('API_USER'),
     "Password": os.getenv('API_PASS')
   }
   r = requests.post('https://owl-dms-api.us-south.cf.appdomain.cloud/api/userData/authenticate',
      json = usrPass, 
      headers={'Content-Type': 'application/json'}
   )
   print("auth:")
   print(r)
   if r.status_code != 200:
      return None
   return r.content.decode('utf-8') # return the token

def getJson(token):
   tenMinsAgo = time.time() - 30
   tenMinsAgo = int(tenMinsAgo)
   tenMinsAgo = 1620463881000
   r = requests.get(f'https://owl-dms-api.us-south.cf.appdomain.cloud/api/userData/getDataByCount?count=1',
         headers={'Authorization': f'Bearer {token}',
                  'Content-Type': 'application/json'
                  },
   )
   resp = r.json()
   print(resp)
   return resp

def get_balloon_gps(token):
   try:
      js = getJson(token)
      innerPayload = js[PAPA_ID][PAPA_ID][0]["innerPayload"]
      innerPayload = innerPayload.split(",")
      lat = float(innerPayload[7])
      lon = float(innerPayload[8])
      alt = float(innerPayload[3])

      return lat, lon, alt
   except Exception as e:
      return None
      
   

tok = authenticate()
get_balloon_gps(tok)