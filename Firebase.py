import time
import board
import busio as io
import adafruit_mlx90614
import pyrebase

config = {
  "apiKey": "AIzaSyAHmdwFtSJ7YgBuNHSVdR9mTFHPBYi3Ta4",
  "authDomain": "habit-chair.firebaseapp.com",
  "databaseURL": "https://habit-chair-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "habit-chair",
  "storageBucket": "habit-chair.appspot.com",
  "messagingSenderId": "49817452985",
  "appId": "1:49817452985:web:74ee05a89d9e22c3bd3668",
  "measurementId": "G-XKVYRZ7BPJ"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

print("Send Data to Firebase Using Raspberry Pi")
print("----------------------------------------")
print()

while True:
  

  print("Updating Firebase")
  print()

  data = {
    "data/online": {
      "state":0
    }
  }
  db.update(data)
  print("Firebase Successfully Updated")

  time.sleep(2)