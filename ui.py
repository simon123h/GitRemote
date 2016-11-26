import msvcrt


currentMenu = None


def menuInput(menu, k):
    contents, title, indentDepth = menu
    print k
    for entry in contents:
        if k == entry[0]:
            entry[2]()
            openMenu(currentMenu)


def openMenu(menu):
    global currentMenu
    currentMenu = menu
    listeners = []
    contents, title, indentDepth = menu
    indentDepth = 2 * indentDepth * " "

    print
    print indentDepth + title

    for entry in contents:
        if entry[1] != '':
            print indentDepth + "  " + entry[1]
        listeners.append(entry[0])

    while True:
        if msvcrt.kbhit():              # TODO: make UNIX/Mac friendly
            k = msvcrt.getch()
            if k == "Q":
                break
            if k in listeners:
                menuInput(menu, k)
                break
