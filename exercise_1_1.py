import time
import sys
import random
from psychopy import visual,event,core, gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]

"""
the two line above are a more compact way of writing:
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
TextStim = visual.TextStim(win,text='+',color='white')

while True:
    nameShown = random.choice(firstNames)
    firstNameStim.setText(nameShown)
    TextStim.draw()
    win.flip()
    core.wait(0.5)
    win.flip()

    firstNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']): # evet.waitKeys(keyList=['q','qd','o'])
        break
