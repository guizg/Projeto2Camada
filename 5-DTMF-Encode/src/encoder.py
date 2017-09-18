import sounddevice as sd

fs = 44100
duration = 2

audio = sd.rec(int(duration*fs), fs, channels=1)
sd.wait()

y = audio[:,0]

# reproduz o som
sd.play(y, fs)

# aguarda fim da reprodução
sd.wait()