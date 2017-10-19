import wave
import struct
import math
import numpy as np
import soundfile as sf
import sounddevice as sd
from scipy import signal as sg
from scipy.fftpack import fft, ifft
import matplotlib
matplotlib.use("TkAgg")
matplotlib.rcParams['agg.path.chunksize'] = 1000
from matplotlib import pyplot as plt

from transmissor import Transmissor

class Receptor:
    def __init__(self):
        self.transmissor = Transmissor()
        self.fs = 44100 # khz
        self.recordingDuration = 10 # segundos
    
    def record(self):
        audio = sd.rec(int(self.recordingDuration * self.fs),self.fs,channels=1)
        sd.wait()
        y = audio[:,0]
        return y

    def main(self):
        # Grava 10s de audio e plota o fourier
        audio = self.record()
        faudiox,faudioy = self.transmissor.getFFT(audio)
        # plt.plot(faudiox,faudioy)
        # plt.show()

        # Recria os carriers a partir do audio gravado
        c1x,c1y = self.transmissor.createCarrier(7000,audio)
        c2x,c2y = self.transmissor.createCarrier(14000,audio)

        # Multiplica o audio gravado pelos carriers para demodular e exibe o fourrier
        dam1 = audio * c1y
        dam2 = audio * c2y
        fdam1x,fdam1y = self.transmissor.getFFT(dam1)
        fdam2x,fdam2y = self.transmissor.getFFT(dam2)
        
        fig, (ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
        ax1.plot(fdam1x,fdam1y)
        ax2.plot(fdam2x,fdam2y)
        plt.show()


Receptor().main()