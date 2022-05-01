from fastapi import FastAPI
from database import dataX,dataY,dataZ,dataSpectrumX,dataSpectrumY,dataSpectrumZ
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dataX = dataX.tolist()
dataY = dataY.tolist()
dataZ = dataZ.tolist()
dataSpectrumX = [dataSpectrumX[0].tolist(),dataSpectrumX[1].round(2).tolist()]
dataSpectrumY = [dataSpectrumY[0].tolist(),dataSpectrumY[1].round(2).tolist()]
dataSpectrumZ = [dataSpectrumZ[0].tolist(),dataSpectrumZ[1].round(2).tolist()]

@app.get("/")
def read_root():
    return {"msg": "hello vibration api :)" }

@app.get("/vibration")
def read_firebase():
    return {"machine-ex01": {
        "waveformX": dataX,
        "waveformY": dataY,
        "waveformZ": dataZ,
        "spectrumX": dataSpectrumX,
        "spectrumY": dataSpectrumY,
        "spectrumZ": dataSpectrumZ,
    }}