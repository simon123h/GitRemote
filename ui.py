from __future__ import print_function
from getchMod import getKey
from analytics import hit

currentMenu = None


def menuInput(menu, k):
    contents, menuTitle, indentDepth = menu
    for entry in contents:
        if k == entry[0]:
            if entry[3] != '':
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


def prettyPrint(str=""):
    indent = "  " + currentMenu[2] * "| "
    print("\n".join([indent + s for s in str.split("\n")]))


def welcomeScreen():
    print()
    print(" ############################################")
    print(" ##                GitRemote               ##")
    print(" ############################################")
    print(" navigate by pressing the corresponding keys!")
    print()
