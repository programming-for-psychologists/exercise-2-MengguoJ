import time
import sys
import random
from psychopy import visual,event,core, gui

userVar = {'Name':'Enter a first name '}
dlg = gui.DlgFromDict(userVar)

names = open('names.txt', 'r').readlines()
new_document = open('output_file', "w")
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
    core.wait(3) # dont use other timer-out function

    clock = core.Clock()

    if event.getKeys(['space']):

#        print "RT:",clock.getTime()*1000

        if nameShown != userVar['Name'].split(' ')[4]:
            fb = visual.TextStim(win, text='X', color='red')
            accuracy = 0
        else:
             fb = visual.TextStim(win, text='O', color='green')
             accuracy = 1

    #    print "Accuracy:", accuracy

        fb.draw()
        win.flip()
        core.wait(1)

        Line = "RT: " + str(clock.getTime()*1000)+ " and Accuracy: "+ str(accuracy)
        new_document.write(Line+"\n")

    elif nameShown == userVar['Name'].split(' ')[4]:
        fb = visual.TextStim(win, text='X', color='red')
        fb.draw()
        win.flip()
        core.wait(1)

    elif event.getKeys(['q']): # evet.waitKeys(keyList=['q','qd','o'])
        break

new_document.close()
