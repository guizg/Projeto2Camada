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

class Transmissor:
    def __init__(self):
        # PARAMS
        self.cutoff = 3000 #hz
        self.fs = 44100         
        # Ler dois arquivos wav
        self.m1 , self.sr1 = sf.read('../samples/smp2.wav')
        self.m2 , self.sr2  = sf.read('../samples/smp1.wav')

    def LPF(self,signal, cutoff_hz, fs):
        """Filtro passa baixa, recebe o sinal,cutoff e fs"""
        # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
        nyq_rate = fs/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = sg.kaiserord(ripple_db, width)
        taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        return(sg.lfilter(taps, 1.0, signal))

    def getFFT(self,signal):
        """Retorna uma tupla com os valores de x e y da FFT de um sinal de entrada"""
        N  = len(signal)
        T  = 1/self.fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)
        return(xf, yf[0:N//2])

    def createCarrier(self,freq,sample):
        """Retorna uma tupla com os valores de x e y de uma senóide com duracao igual
        ao do sample fornecido e frequencia fornecida"""
        x = np.linspace(0, len(sample)/self.fs, len(sample))
        y = np.sin(2 * math.pi * x * freq)
        return (x,y)

    def play(self,sample):
        """ Reproduz um sinal ou sample e aguarda o fim da reprodução """
        sd.play(sample,self.fs)
        sd.wait()

    def sum(self,signal1,signal2):
        """Recebe dois sinais e adiciona um padding para que ambos fiquem com
        mesmo tamanho. Retorna tupla com os valores de (x,y) do sinal somado"""
        if len(signal1) > len(signal2):
            largest = signal1
            smallest = signal2
        else:
            largest = signal2
            smallest = signal1
        
        x = np.linspace(0, len(largest)/self.fs, len(largest))        
        dif = len(largest) - len(smallest)
        smallest = np.pad(smallest,(0,dif),'constant',constant_values=(0,0))
        return x,largest + smallest 

    def main(self):
        samples_m1 = len(self.m1)
        samples_m2 = len(self.m2)

        # Filtra os samples - Passa baixa
        m1_filtered = self.LPF(self.m1,self.cutoff,self.fs)
        m2_filtered = self.LPF(self.m2,self.cutoff,self.fs)

        # Obtem o fourrier dos samples filtrados
        x1,y1 = self.getFFT(m1_filtered)
        x2,y2 = self.getFFT(m2_filtered)

        # Cria as portadoras
        c1x,c1y = self.createCarrier(7000,self.m1)
        c2x,c2y = self.createCarrier(14000,self.m2)

        # Obtêm o fourrier das portadoras
        fc1x,fc1y = self.getFFT(c1y)
        fc2x,fc2y = self.getFFT(c2y)
        
        # Reproduz um sample filtrado
        self.play(m1_filtered)

        # Plota o fourrier das portadoras
        fig, (ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
        ax1.plot(fc1x,fc1y)
        ax2.plot(fc2x,fc2y)
        plt.show()
    
        # Samples 1 e 2 modulados
        am1 = m1_filtered * c1y
        am2 = m2_filtered * c2y

        # Obtêm o fourrier dos samples modulados, plota e reproduz
        fam1x,fam1y = self.getFFT(am1)
        fam2x,fam2y = self.getFFT(am2)
        fig2, (ax3,ax4) = plt.subplots(1,2,figsize=(15,5))
        ax3.plot(fam1x,fam1y)
        ax4.plot(fam2x,fam2y)
        plt.show()
        self.play(am2)
        self.play(am1)

        # Soma os samples modulados para transmissão
        am_sumx,am_sumy = self.sum(am1,am2)
        fam_sumx,fam_sumy = self.getFFT(am_sumy)
        plt.plot(fam_sumx,fam_sumy)
        plt.show()
        self.play(am_sumy)

        # plt.plot(x1,y1)
        # plt.plot(x2,y2)
        # plt.show()

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   Transmissor().main()