
import matplotlib.pyplot as plt
import numpy as np
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyC_dBJfyF7UkV7nnpbLz_HRwKhPOtZt6dA",
  "authDomain": "vibration-project-9f1df.firebaseapp.com",
  "databaseURL": "https://vibration-project-9f1df-default-rtdb.firebaseio.com",
  "projectId": "vibration-project-9f1df",
  "storageBucket": "vibration-project-9f1df.appspot.com",
  "messagingSenderId": "1057518338294",
  "appId": "1:1057518338294:web:017498a4f027dc888dacd7",
  "measurementId": "G-TXZKQQ03WL"
};
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
rawX = db.child("vibration").child("machine-ex-01").child("X-axis").child("X").get()
rawY = db.child("vibration").child("machine-ex-01").child("Y-axis").child("Y").get()
rawZ = db.child("vibration").child("machine-ex-01").child("Z-axis").child("Z").get()


plt.figure(figsize=(10,8))
# (row,column,pos)
ax1 = plt.subplot(3, 2, 1)
ax2 = plt.subplot(3, 2, 2)
ax3 = plt.subplot(3, 2, 3)
ax4 = plt.subplot(3, 2, 4)
ax5 = plt.subplot(3, 2, 5)
ax6 = plt.subplot(3, 2, 6)


dataX = np.array(rawX.val())
dataY = np.array(rawY.val())
dataZ = np.array(rawZ.val())


x = ax1.plot(dataX)
y = ax3.plot(dataY)
z = ax5.plot(dataZ)

# adx 480 mpu 335   #s2 mpu130

dataSpectrumX = ax2.magnitude_spectrum(dataX, Fs=335, color='C1')
dataSpectrumY = ax4.magnitude_spectrum(dataY, Fs=335, color='C1')
dataSpectrumZ = ax6.magnitude_spectrum(dataZ, Fs=335, color='C1')

# plt.show()

