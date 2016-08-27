import subprocess


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
	return commandOutput(["git "+c for c in commands])