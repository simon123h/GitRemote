import subprocess


# retrieve the output of a CMD command or a list of CMD commands
def cmd(command, printOutput=True):
    if type(command) is str:
        command = command.split(' ')
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()[0:2]
        return output, error
    elif type(command) is list:
        output = []
        error = []
        for elem in command:
            curOut, curErr = cmd(elem)
            output.append(curOut)
            error.append(curErr)
        output = "\n".join(output)
        if error == [None]:
            error = [""]
        else:
            error = None
        if printOutput:
            print output
        return output, error


# execute any list of git commands and return output
def git(command):
    if type(command) is str:
        command = [command]
    return cmd(["git " + c for c in command])
