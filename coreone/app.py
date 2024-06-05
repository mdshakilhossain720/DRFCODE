import requests
import json

URL="http://127.0.0.1:8000/updates/"

def get_data(id = None):
    data={}
    if id is not None:
        
     data={'id':id}
    json_data=json.dumps(data)

    r=requests.get(url=URL,data = json_data)
    data=r.json()
    print(data)
get_data(1)


def post():
   data={
      'name':'shakil',
      'rool':100,
      'city':'dhaka',
   }
   json_data=json.dumps(data)
   r=requests.post(url=URL, data= json_data)
   data=r.json()
   print(data)
post()


def Update_data():
   data={
      'id':1,
      'name':'shakil',
      'rool':100,
      'city':'dhaka',
   }
   json_data=json.dumps(data)
   r=requests.put(url=URL, data= json_data)
   data=r.json()
   print(data)
Update_data()

def deleted_data():
   data={
      'id':1}
   json_data=json.dumps(data)
   r=requests.delete(url=URL, data= json_data)
   data=r.json()
   print(data)
deleted_data()


