import sounddevice as sd
import numpy as np
import math
import time
import matplotlib.pyplot as plt

global fs,duration,x
fs = 44100
duration = 0.5
x = np.linspace(0, duration, fs * duration)

def createTonesArray():
	freqsUpper = [1209, 1336, 1477, 1633]
	freqsLower = [697, 770, 852, 941]
	
	tons = []
	for i in range(4):
		line = []
		for j in range(4):
			line.append(np.sin(2*math.pi*x*freqsUpper[j]) + np.sin(2*math.pi*x*freqsLower[i]))
		tons.append(line)
	return tons

def playSound(freq):
	sd.play(freq,fs)
	plt.plot(x,freq)
	sd.wait()

def humanMusic():
    yh = np.sin(2*math.pi*x*512)
    ym = np.sin(2*math.pi*x*576)
    while True:
        # reproduz o som
        sd.play(yh, fs)
        # aguarda fim da reprodução
        sd.wait()
        # reproduz o som
        sd.play(ym, fs)
        # aguarda fim da reprodução
        sd.wait()
        # reproduz o som
        sd.play(yh, fs)
        # aguarda fim da reprodução
        sd.wait()
        time.sleep(0.5)


