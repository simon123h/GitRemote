from functions import *
# execute git actions and return the output


def commit(emptyMessage = False, amend = False):
	message = prompt('Commit message', '')
	if message == None:
		return "Commit aborted."
	if emptyMessage:
		pass
	return git('commit -m "' + message + '"')
	
	
	
