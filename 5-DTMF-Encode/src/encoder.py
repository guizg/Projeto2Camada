import sounddevice as sd
import numpy as np
import math
import time

fs = 44100
duration = 0.5
freqsUpper = [1209, 1336, 1477, 1633]
freqsLower = [697, 770, 852, 941]

# audio = sd.rec(int(duration*fs), fs, channels=1)
# sd.wait()

# y = audio[:,0]

x = np.linspace(0, duration, fs*duration)

y9 = np.sin(2*math.pi*x*freqsUpper[2]) + np.sin(2*math.pi*x*freqsLower[2])
y5 = np.sin(2*math.pi*x*freqsUpper[1]) + np.sin(2*math.pi*x*freqsLower[1])

yh = np.sin(2*math.pi*x*512)
ym = np.sin(2*math.pi*x*576)

# reproduz o som
sd.play(yh, fs)
# aguarda fim da reprodução
sd.wait()

time.sleep(0.2)

# reproduz o som
sd.play(ym, fs)
# aguarda fim da reprodução
sd.wait()

time.sleep(0.2)

# reproduz o som
sd.play(yh, fs)
# aguarda fim da reprodução
sd.wait()
