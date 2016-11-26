import subprocess
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog


# retrieve the output of a CMD command or a list of CMD commands
def commandOutput(cmd):
	if type(cmd) is str:
		return subprocess.check_output(cmd.split(' ')).decode('utf-8')	
	elif type(cmd) is list:
		output = []
		for command in cmd:
			output.append(commandOutput(command))
		return "\n".join(output)	

		

# execute any list of git commands and return output
def git(commands):
	if type(commands) is str:
		commands = [commands]
	return commandOutput(["git "+c for c in commands])
	
	
# show a prompt for user input
def prompt(title, text):
	return tkinter.simpledialog.askstring(title, text)
	

def message(title, text):
	return tkinter.messagebox.showinfo(title, text)