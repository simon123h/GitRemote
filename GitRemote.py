from tkinter import *
#from functions import *
#import actions

def main():
	root = Tk()
	root.geometry('720x480')
	# splitting the window in button area and command output window
	top = Frame(root)
	bottom = Frame(root)
	top.pack(side=TOP)
	bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

	# easy creation of a button
	def newButton(label, command = None):
		command = lambda: text.insert('end', command())
		return Button(root, text = label, command = command, padx = 7, pady = 7)
		
	# Buttons
	newButton('Pull',
				lambda: git('pull')
	).pack(in_=top, side=LEFT)

	newButton('Commit',
				actions.commit
	).pack(in_=top, side=LEFT)

	newButton('Push', 
				lambda: git('push')
	).pack(in_=top, side=LEFT)

	newButton('Status', 
				lambda: git('status')
	).pack(in_=top, side=LEFT)

	newButton('Log', 
				lambda: git('log')
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