import time
import sys
import random
from psychopy import visual,event,core, gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
LastNames = [name.split(' ')[1] for name in names]

"""
the two line above are a more compact way of writing:
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""

win = visual.Window([800,600],color="black", units='pix')
NameStim = visual.TextStim(win,text="???", height=40, color="white",pos=[0,0])
while True:
    win.flip() # how to wait smartly
#core.wait(10) # how to wait smartly


    if event.getKeys(['f']):
        while True:
            nameShown = random.choice(firstNames)
            NameStim.setText(nameShown)
            NameStim.draw()
            win.flip()
            core.wait(.75)
            win.flip()
            core.wait(.15)

            if event.getKeys(['q']): # evet.waitKeys(keyList=['q','qd','o'])
                break

    if event.getKeys(['l']):
        while True:
            nameShown = random.choice(LastNames)
            NameStim.setText(nameShown)
            NameStim.draw()
            win.flip()
            core.wait(.75)
            win.flip()
            core.wait(.15)

            if event.getKeys(['q']): # evet.waitKeys(keyList=['q','qd','o'])
                break

    if event.getKeys(['q']): # how to break with 1 q instead of 2
        break
