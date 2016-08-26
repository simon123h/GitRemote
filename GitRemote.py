import subprocess
from tkinter import *


def commandOutput(cmd):
	return subprocess.check_output(cmd.split(' ')).decode('utf-8')
	
def commandText(cmd):
	text.insert('end', commandOutput(cmd))

def onKeyPress(event):
	text.insert('end', 'You pressed %s\n' % (event.char, ))
	print('key pressed')
	

def pull():
	commandText('git pull')
	
def commit():
	commandText('git add .')
	commandText('git commit --allow-empty-message -m ""')
	
def push():
	commandText('git push')

root = Tk()
#root.geometry('300x200')


top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)


# Pull Button
pullButton = Button(root, text="Pull", command=pull)
pullButton.pack(in_=top, side=LEFT)
# Commit Button
commitButton = Button(root, text="Commit", command=commit)
commitButton.pack(in_=top, side=LEFT)
# Push Button
pushButton = Button(root, text="Push", command=push)
pushButton.pack(in_=top, side=LEFT)


# Console window
text = Text(root, width=35, height=15, background='black', foreground='green', font=('Courier', 11))
scrollbar = Scrollbar(root)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
scrollbar.pack(in_=bottom, side=RIGHT, fill=Y)
text.pack(in_=bottom, side=LEFT, fill=BOTH, expand=True)



root.bind('<KeyPress>', onKeyPress)
#root.mainloop()

