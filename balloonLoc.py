import requests
import time
import os

def authenticate():
   usrPass = {
     "Username": os.getenv('API_USER'),
     "Password": os.getenv('API_PASS')
   }
   r = requests.post('https://owl-dms-api.us-south.cf.appdomain.cloud/api/userData/authenticate',
      json = usrPass, 
      headers={'Content-Type': 'application/json'}
   )
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

def get_balloon_gps(token):
   try:
      getJson(token)
      return 35.3025, -120.6974, 471
   except Exception:
      return None
   





#tok = authenticate()
#getLocation(tok)



