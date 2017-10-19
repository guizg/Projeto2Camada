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
        """Grava audio por tempo determinado no construtor e retorna o sinal """
        print('Gravando...')
        audio = sd.rec(int(self.recordingDuration * self.fs),self.fs,channels=1)
        sd.wait()
        y = audio[:,0]
        print('Gravação concluida')
        return y

    def main(self):
        # Grava 10s de audio e plota no tempo e fourier
        audio = self.record()
        faudiox,faudioy = self.transmissor.getFFT(audio)
        plt.plot(faudiox,faudioy)
        plt.show()
        plt.plot(np.linspace(0, len(audio)/self.fs, len(audio)),audio)
        plt.show()

        # Recria os carriers a partir do audio gravado
        c1x,c1y = self.transmissor.createCarrier(7000,audio)
        c2x,c2y = self.transmissor.createCarrier(14000,audio)

        print('Len carrier 1',len(c1y))
        print('Len carrier 2',len(c2y))

        # Multiplica o audio gravado pelos carriers para demodular,exibe o fourrier
        dam1 = audio * c1y
        dam2 = audio * c2y
        fdam1x,fdam1y = self.transmissor.getFFT(dam1)
        fdam2x,fdam2y = self.transmissor.getFFT(dam2)
        fig, (ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
        ax1.plot(fdam1x,fdam1y)
        ax2.plot(fdam2x,fdam2y)
        plt.show()

        fig2, (ax3,ax4) = plt.subplots(1,2,figsize=(15,5))
        ax3.plot(np.linspace(0,len(dam1)/self.fs,len(dam1)),dam1)
        ax4.plot(np.linspace(0,len(dam2)/self.fs,len(dam2)),dam2)
        plt.show()

        # Faz um filtro passa baixa e reproduz os sons recuperados
        recovered_sample1 = self.transmissor.LPF(dam1,3000,self.fs)
        recovered_sample2 = self.transmissor.LPF(dam2,3000,self.fs)
        
        fig3, (ax5,ax6) = plt.subplots(1,2,figsize=(15,5))
        ax5.plot(np.linspace(0,len(recovered_sample1)/self.fs,len(recovered_sample1)),recovered_sample1)
        ax6.plot(np.linspace(0,len(recovered_sample2)/self.fs,len(recovered_sample2)),recovered_sample2)
        plt.show()

        frecovered1x , frecovered1y = self.transmissor.getFFT(recovered_sample1)
        frecovered2x , frecovered2y = self.transmissor.getFFT(recovered_sample2)
        
        fig4, (ax7,ax8) = plt.subplots(1,2,figsize=(15,5))    
        ax7.plot(frecovered1x,frecovered1y)
        ax8.plot(frecovered2x,frecovered2y)
        plt.show()

        self.transmissor.play(recovered_sample1)
        self.transmissor.play(recovered_sample2)

        # Salva os samples recuperados e filtrados
        sf.write('recovered_sample1.wav', recovered_sample1, self.fs)
        sf.write('recovered_sample2.wav', recovered_sample2, self.fs)


Receptor().main()