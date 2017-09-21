import socket
from flask import Flask
import sounddevice as sd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from threading import Thread
import wave

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



server = Servidor()