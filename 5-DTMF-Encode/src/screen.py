from tkinter import Tk, Button, RAISED
from functools import partial
import sounddevice as sd
import numpy as np
import math
import time
import encoder as encoder

# audio = sd.rec(int(duration*fs), fs, channels=1)
# sd.wait()
# y = audio[:,0]
class Screen:    
    def __init__(self):
        self.root = Tk()
        self.root.title = 'Human music generator (and DTMF)'
        self.fs = 44100
        self.buttons = [
            ['1','2','3','a'],
            ['4','5','6','b'],
            ['7','8','9','c'],
            ['*','0','#','d']
        ]
        self.sounds = [512,576,640,682,768,854,960]
        self.tons = encoder.createTonesArray()
        
        for r in range(4):
            for c in range(4):
                button = Button (
                    self.root,
                    relief = RAISED,
                    padx = 10,
                    text = self.buttons[r][c],
                    command = partial(encoder.playSound, self.tons[r][c])
                )
                button.grid(row = r, column = c)
                # freq = np.sin(2*math.pi*x*freqsUpper[2]) + np.sin(2*math.pi*x*freqsLower[2])
        humanMusicButton = Button(
            self.root,
            relief = RAISED,
            padx = 10,
            text='HM',
            command=encoder.humanMusic
        ).grid(row=3)

                
    def buttonClicked(self,buttonVal):
        print(buttonVal)


        
Screen().root.mainloop()

