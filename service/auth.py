import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore

import requests
import re


cred = credentials.Certificate("service_account.json")

firebase_admin.initialize_app(cred)

db = firestore.client()



#add account with known ID
def cUser(name,email,password):
    data = {'name':f'{name}','password': f"{password}",'email':f"{email}"}
    db.collection('person').document(name).set(data) #document reference



def get_user(email):
    try:
        user = auth.get_user_by_email(email)
        return user.uid, user.display_name,user.email
    except:
        return None

def register_user(name, email,password):
    try:
        user = auth.create_user(
        email=email,
        password=password,
        display_name=name,)
        return user.uid
    except:
        return None

def authenticate(email,password):
  auth_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key="
  api_key = "AIzaSyBzaJHUo5_3axwV0Zjq8N_VemwREW5tmJ0"
  
  payload = {
      "email": email,
      "password": password,
      "returnSecureToken": True
  }
  
  response = requests.post(auth_url + api_key, json=payload)
  
  if response.status_code == 200:
      id_token = response.json()["idToken"]
      return id_token
  else:
      return None


async def verify_token(token):
  try:
    decoded_token = auth.verify_id_token(token)
    return decoded_token
  except Exception as e:
      return None


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None