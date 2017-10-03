# -*- coding: utf-8 -*-

import socket
import wave
import sounddevice as sd
import numpy as np
import matplotlib
import math
# matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from threading import Thread
from flask import Flask
import sys
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
from scipy import signal

class Servidor:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.before_request(lambda: Thread(target=self.listen).start())
        self.app.add_url_rule('/listen','listen',self.onRequest)
        self.fs = 44100
        self.listenDuration = 1
        self.x = np.linspace(0, self.listenDuration, self.fs * self.listenDuration)
        self.app.run(host=self.get_ip_address())
        
    def onRequest(self):
        return "OK"

    def listen(self):
        print('Listening...')
        # f, (ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
        
        audio = sd.rec(int(self.listenDuration * self.fs),self.fs,channels=1)
        sd.wait()
        y = audio[:,0]
        print(len(y))
        fouriery = np.fft.fft(y)
        fourierx = np.fft.fftfreq(self.x.shape[-1]) * self.fs * (1/self.listenDuration)
        plt.clf()
        plt.plot(self.x[40000:40200],y[40000:40200])
        plt.show()
        plt.plot(np.abs(fourierx),fouriery.real)
        # ax1.plot(self.x[40000:40200],y[40000:40200])
        # ax2.plot(np.abs(fourierx),fouriery.real)
        # ax2.set_ylim(bottom=0.)
        print('Finished listening...')
        # f.show()
        plt.show()
    
    def get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

class Decoder:
    def __init__(self):
        self.fs = 44100
        self.listenDuration = 1
        self.x = np.linspace(0, self.listenDuration, self.fs * self.listenDuration)
        self.listening = False

    def listen(self):
        self.listening = True
        self.listenThread()
        # # listenThread = Thread(target=self.listenThread)
        # listenThread.start()

    def listenThread(self):
        freqrange = [0,20000]
        plt.ion()
        fig, (ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
        l1, = ax1.plot([],[])
        l2, = ax2.plot([],[])
        ax2.set_xlim(freqrange)
        ax1.set_xlim([0,self.listenDuration])
        ax2.set_ylim([-50,100])
        # fig.draw()
        # plt.show(block=False)

        while self.listening:
            # f, (ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
            print('Listening...')
            audio = sd.rec(int(self.listenDuration * self.fs),self.fs,channels=1)
            sd.wait()
            y = audio[:,0]

            fouriery = np.multiply(np.log10(np.fft.fft(y)) , 20)
            fouriery = fouriery.real
            fourierx = np.abs(np.fft.fftfreq(self.x.shape[-1]) * self.fs * (1/self.listenDuration))

            l1.set_xdata(self.x)
            l1.set_ydata(y)

            l2.set_xdata(fourierx)
            l2.set_ydata(fouriery)

            peaks = self.getPeaks(fourierx,fouriery)

            fig.canvas.draw()
            fig.canvas.start_event_loop(0.001)

            # peakind = signal.find_peaks_cwt(fouriery, np.arange(1,3), noise_perc=0)
            # print(peakind, fourierx[peakind], fouriery[peakind])

            # soundfig.draw()
            # plt.draw()

            # plt.plot(self.x[40000:40200],y[40000:40200])
            # plt.show()
            # plt.plot(np.abs(fourierx),fouriery.real)
            # ax1.plot(self.x[40000:40200],y[40000:40200])
            # ax2.plot(np.abs(fourierx),fouriery.real)
            # ax2.set_ylim(bottom=0.)
            # print('Finished listening...')
            # plt.show()
            # f.show()
            # plt.show()

    def openWavFile(self,fileDir):
        print(fileDir)
        spf = wave.open(fileDir,'r')

        #Extract Raw Audio from Wav File
        s = spf.readframes(-1)
        s = np.fromstring(s, 'Int16')
        fs = spf.getframerate()
        duration = spf.getnframes()/spf.getframerate()

        #If Stereo
        if spf.getnchannels() == 2:
            print('Just mono files')
            sys.exit(0)

        t = np.linspace(0, len(s)/fs, num=len(s))

        fouriery = np.fft.fft(s)
        fourierx = np.fft.fftfreq(t.shape[-1]) * fs * (1/duration)

        plt.figure(1)
        plt.title('Signal Wave...')
        # plt.plot(t,signal)
        plt.plot(np.abs(fourierx),fouriery.real)
        plt.show()

    def getPeaks(self,x,y):
        peaks = []
        for i in range(len(x)):
            if y[i] > 40 and x[i] > 600 and x[i] < 1800:
                # print('A frequencia {} é maior que 40db'.format(x[i]))
                if x[i] not in peaks:
                    peaks.append(x[i])

        pdic = {}
        print(peaks)

        for p in peaks:
            p = math.floor(p)
            f = 0
            for k in pdic.keys():
                if p >= k-10 and p <= k+10:
                    pdic[k].append(p)
                    f=1
            if f == 1:
                continue
            pdic[p] = [p]
            
        freq = []
        for k in pdic.keys():
            mean = np.average(pdic[k])
            freq.append(mean)

        freq = sorted(freq)
        

        print('As principais frequências que compôem o sinal sao:')
        freqsUpper = [1209, 1336, 1477, 1633]
        freqsLower = [697, 770, 852, 941]
        
        i = -1
        j = -1

        for k in freq:
            print('-> {} Hz '.format(k))
    
            for l in range(len(freqsUpper)):
                if k >= (freqsUpper[l] - 25) and k <= (freqsUpper[l] + 25):
                    j = l
            
            for g in range(len(freqsLower)):
                if k >= (freqsLower[g] - 25) and k<= (freqsLower[g] + 25):
                    i = g 

        dtmf = [
            ['1','2','3','a'],
            ['4','5','6','b'],
            ['7','8','9','c'],
            ['*','0','#','d']
        ]
        
        if i != -1 and j != -1:
            print('O TOM ENCONTRADO FOI {}'.format(dtmf[i][j]))

        return freq
            
            
