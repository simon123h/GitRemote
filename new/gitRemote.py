import msvcrt
import menus
from gitBridge import cmd


def menuInput(menu, k):
    contents, title, indentDepth = menu
    for entry in contents:
        if k == entry[0]:
            entry[2]()


def openMenu(menu):
    listeners = []
    contents, title, indentDepth = menu
    indentDepth = indentDepth * " "

    print
    print title

    for entry in contents:
        if entry[1] != '':
            print indentDepth + entry[1]
        listeners.append(entry[0])

    while True:
        if msvcrt.kbhit():              # TODO: make UNIX/Mac friendly
            k = msvcrt.getch()
            if k in listeners:
                print k
                menuInput(menu, k)
                break


def start():
    openMenu(menus.main)
