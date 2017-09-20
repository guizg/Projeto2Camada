from flask import Flask
import sounddevice as sd
from numpy import linspace
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
class Servidor:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/listen','listen',self.onRequest)
        self.fs = 44100
        self.listenDuration = 1
        self.x = linspace(0, self.listenDuration, self.fs * self.listenDuration)
        self.app.before_request(self.listen)
        self.app.run()

    def onRequest(self):
        return "OK",

    def listen(self):
        print('Listening...')
        audio = sd.rec(int(self.listenDuration * self.fs),self.fs,channels=1)
        sd.wait()
        y = audio[:,0]
        plt.plot(self.x,y)
        print('Finished listening...')
        plt.show()


server = Servidor()