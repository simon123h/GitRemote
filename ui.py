from __future__ import print_function
from getch import getKey
from analytics import hit

currentMenu = None


def menuInput(menu, k):
    contents, menuTitle, indentDepth = menu
    for entry in contents:
        if k == entry[0]:
            if entry[3] != '':
                prettyPrint()
                prettyPrint(entry[3])
            r = entry[2]()
            if r is None:
                hit(entry[2].__name__)
                openMenu(currentMenu)
            else:
                prettyPrint()


def openMenu(menu):
    global currentMenu
    currentMenu = menu
    listeners = []
    contents, title, indentDepth = menu
    indentDepth = "  " + indentDepth * "|  "

    print(indentDepth)
    print(indentDepth + title)

    for entry in contents:
        if entry[1] != '':
            print(indentDepth + "| [" + entry[0] + "] " + entry[1])
        listeners.append(entry[0])

    while True:
        k = getKey()
        if ord(k) == 3:
            break
        if k in listeners:
            menuInput(menu, k)


def prettyPrint(message="", *messages):
    message = " ".join([str(m) for m in ([message] + list(messages))])
    indent = "  " + (currentMenu[2] + 1) * "|  "
    print("\n".join([indent + s for s in message.split("\n")]))


# a simple user confirmation dialog, returns True on confirmation, False otherwise
def confirmDialog(message="Are you sure? (y/n)", confirmKey="y", *keys):
    confirmKeys = [confirmKey] + list(keys)
    prettyPrint(message + " ")
    k = getKey()
    if str(k) in confirmKeys:
        return True
    return False


def welcomeScreen():
    print()
    print(" ############################################")
    print(" ##                GitRemote               ##")
    print(" ############################################")
    print(" navigate by pressing the corresponding keys!")
    print()
    print()
    print()
    print("             Don't forget to pull!")
    print("  Hit [u] to update your code from the server!")
    print()
    print()
