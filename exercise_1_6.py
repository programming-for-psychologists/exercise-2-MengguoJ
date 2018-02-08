import time
import sys
import random
from psychopy import visual,event,core, gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1] for name in names]
Names = firstNames + lastNames

win = visual.Window([800,600],color="black", units='pix')
NameStim = visual.TextStim(win,text="???", height=40, color="white",pos=[0,0])

while True:
    nameShown = random.choice(Names)
    NameStim.setText(nameShown)
    NameStim.draw()
    win.flip()
    core.wait(1) # dont use other timer-out function
    if event.getKeys(['f']):
        if nameShown in firstNames:
            fb = visual.TextStim(win, text='O', color='green')
        else:
            fb = visual.TextStim(win, text='X', color='red')
        fb.draw()
        win.flip()
        core.wait(1)
    elif event.getKeys(['l']):
        if nameShown in lastNames:
            fb = visual.TextStim(win, text='O', color='green')
        else:
            fb = visual.TextStim(win, text='X', color='red')
        fb.draw()
        win.flip()
        core.wait(1)

    else:
        fb = visual.TextStim(win, text='X', color='red')
        fb.draw()
        win.flip()
        core.wait(1)

    if event.getKeys(['q']): # evet.waitKeys(keyList=['q','qd','o'])
        break
