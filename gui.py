from tkinter import *
from functions import *

def main():
	root = Tk()
	root.geometry('720x480')
	# splitting the window in button area and command output window
	top = Frame(root)
	bottom = Frame(root)
	top.pack(side=TOP)
	bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

	# easy creation of a button
	def newButton(label, cmds = None, command = None):
		if cmds is not None:
			command = lambda: writeCommandOutput(cmds)
		return Button(root, text = label, command = command, padx = 7, pady = 7)
		
	# Buttons
	newButton('Pull',
				['git pull']
	).pack(in_=top, side=LEFT)

	newButton('Commit',
				['git add .', 'git commit -m "refactor"']
	).pack(in_=top, side=LEFT)

	newButton('Push', 
				['git push']
	).pack(in_=top, side=LEFT)

	newButton('Status', 
				['git status']
	).pack(in_=top, side=LEFT)

	newButton('Log', 
				['git log']
	).pack(in_=top, side=LEFT)


	# Console window
	text = Text(root, width=35, height=15, background='black', foreground='white', font=('Courier', 11))
	scrollbar = Scrollbar(root)
	scrollbar.config(command=text.yview)
	text.config(yscrollcommand=scrollbar.set)
	scrollbar.pack(in_=bottom, side=RIGHT, fill=Y)
	text.pack(in_=bottom, side=LEFT, fill=BOTH, expand=True)
	
	# function to write the output of a batch command or a list of batch commands into the textbox
	def writeCommandOutput(commands):
		text.insert('end', commandOutput(commands)+'\n')


	root.mainloop()