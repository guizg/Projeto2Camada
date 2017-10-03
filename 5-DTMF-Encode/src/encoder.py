import sounddevice as sd
import numpy as np
import math
import time
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import requests
import wave

global fs,duration,x,hostip
hostip = '10.92.203.245'
fs = 44100
duration = 1
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
	# outfile = wave.open('sound.wav',mode='wb')
	# outfile.setparams((1, 1, fs, 0,'NONE','not compressed'))
	# outfile.writeframes(freq)
	# outfile.close()
	res = requests.get('http://{}:5000/listen'.format(hostip))
	if res.ok:
		print('Decoder ouvindo, tocando')
		print(len(freq))
		fouriery = np.fft.fft(freq)
		fourierx = np.fft.fftfreq(x.shape[-1]) * fs * (1/duration)
		f, (ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
		sd.play(freq,fs)
		sd.wait()
		# plt.subplot(1,2,1)
		ax1.set_title('Frequência')
		ax1.plot(x[:200],freq[:200])
		# plt.subplot(1,2,2)
		ax2.set_title('Fourier')
		ax2.plot(np.abs(fourierx),fouriery.real)
		# plt.figure(figsize=(20,10))
		f.show()

def humanMusic():
	x = np.linspace(0, 0.5, fs * 0.5)
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


