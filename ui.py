from __future__ import print_function
import msvcrt


currentMenu = None


def menuInput(menu, k):
    contents, menuTitle, indentDepth = menu
    # print(k)
    for entry in contents:
        if k == entry[0]:
            r = entry[2]()
            if r is None:
                usageStat(entry[1], menuTitle)
                openMenu(currentMenu)


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
            print(indentDepth + "| " + entry[1])
        listeners.append(entry[0])

    while True:
        if msvcrt.kbhit():              # TODO: make UNIX/Mac friendly
            k = msvcrt.getch()
            if k in listeners:
                break
    menuInput(menu, k)


def prettyPrint(str=""):
    indent = "  " + currentMenu[2] * "| "
    print("\n".join([indent + s for s in str.split("\n")]))


def usageStat(functionName, menuTitle):
    with open("usageStats/stats.dat", "a+") as f:
        print(menuTitle + " / " + functionName, file=f)
