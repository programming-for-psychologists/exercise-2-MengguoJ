import time
import sys
import random
from psychopy import visual,event,core, gui

userVar = {'Name':'Enter a first name '}
dlg = gui.DlgFromDict(userVar)

names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1] for name in names]
Names = firstNames + lastNames

win = visual.Window([800,600],color="black", units='pix')
NameStim = visual.TextStim(win,text="???", height=40, color="white",pos=[0,0])


FirstAccuracy = 0
LastAccuracy = 0

while True:
    nameShown = random.choice(Names)
    NameStim.setText(nameShown)
    NameStim.draw()
    win.flip()
    core.wait(3) # dont use other timer-out function

    clock = core.Clock()

    if event.getKeys(['space']):

#        print "RT: ",clock.getTime()

        if nameShown != userVar['Name'].split(' ')[4]:
            fb = visual.TextStim(win, text='X', color='red')
            if nameShown in firstNames:
                FirstAccuracy -= 0
            else:
                LastAccuracy -= 0

        else:
             fb = visual.TextStim(win, text='O', color='green')
             if nameShown in firstNames:
                 FirstAccuracy += 1
             else:
                 LastAccuracy += 1

        fb.draw()
        win.flip()
        core.wait(1)


    elif nameShown == userVar['Name'].split(' ')[4]:
        fb = visual.TextStim(win, text='X', color='red')

        if nameShown in firstNames:
            FirstAccuracy += 0
        else:
            LastAccuracy += 0

    elif nameShown != userVar['Name'].split(' ')[4]:
        fb = visual.TextStim(win, text='O', color='green')

        if nameShown in firstNames:
            FirstAccuracy += 1
        else:
            LastAccuracy += 1

    fb.draw()
    win.flip()
    core.wait(1)

    print "So far, the First Name Accuracy is ", FirstAccuracy, ", while Last Name Accuracy is ", LastAccuracy

    if event.getKeys(['q']): # evet.waitKeys(keyList=['q','qd','o'])
        print "At the end, the First Name Accuracy is ", FirstAccuracy, ", while Last Name Accuracy is ", LastAccuracy
        break
