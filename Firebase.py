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
this_millis = 0
time_period = 1000
sec = 0
min = 0
hour = 0
occupancy = 1
last_millis = 0


def timeCount():
  globals()["sec"] = globals()["sec"] +1
  if globals()["sec"] > 60:
    globals()["sec"] = 0
    globals()["min"] = globals()["min"] + 1
  if globals()["min"] > 60:
    globals()["min"] = 0
    globals()["hour"] = globals()["hour"] + 1  
  print("Time: ")
  print(globals()["sec"])  

while True:
  globals()["this_millis"] = int(time.time()*1000)#nanosec to millisec
  print("Reading Firebase")
  # occupancy_ref=db.child("data/occupancy/status").get()
  # occupancy=occupancy_ref.val()
  if occupancy == 1:
    if globals()["this_millis"] - last_millis > time_period:
      print("Triggered")
      last_millis = globals()["this_millis"]
      timeCount()
      
  print()
  print(occupancy)
  print()
  print("All data collected")
  print()
  


  print("Updating Firebase") 
  print()

  data = {
    "data/online": {
      "state":0
    },
    "data/occupancy":{
      "status":0
    },
    "data/time":{
      "minutes":globals()["min"],
      "hours":globals()["hour"]
    }
  }
  db.update(data)
  print("Firebase Successfully Updated")
