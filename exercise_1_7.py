from psychopy import visual, gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1] for name in names]
Names = firstNames + lastNames

userVar = {'Name':'Enter a first name '}
dlg = gui.DlgFromDict(userVar) # for pop-up box

def popupError(text):
    errorDlg = gui.Dlg(title="Error", pos=(200,400))
    errorDlg.addText('Error: '+text, color='Red')
    errorDlg.show()


if userVar['Name'].split(' ')[4] not in firstNames:
    popupError("'Name does not exisit' error!")
