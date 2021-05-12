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
   if r.status_code != 200:
      return None


   return r.content.decode('utf-8')

def getLocation(token):
   tenMinsAgo = time.time() - 30
   tenMinsAgo = int(tenMinsAgo)
   tenMinsAgo = 1620463881000
   r = requests.get(f'https://owl-dms-api.us-south.cf.appdomain.cloud/api/userData/getDataByCount?count=10',
         headers={'Authorization': f'Bearer {token}',
                  'Content-Type': 'application/json'
                  },
   )
   resp = r.json()
   print(resp)


#tok = authenticate()
#getLocation(tok)



