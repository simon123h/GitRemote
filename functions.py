from __future__ import print_function
from gitAPI import git
from ui import openMenu
import menus


def main():
    openMenu(menus.main)


def more():
    openMenu(menus.more)


def evenMore():
    openMenu(menus.evenMore)

def branching():
    openMenu(menus.branching)



def pull():
    git("pull")


def commit(message=""):
    git("add .")
    if message == "":
        git("commit")
    else:
        git("commit -m ''" + str(message) + "'")


def push():
    git("push")


def status():
    git("status")


def diff():
    git("diff")


def log():
    git("log")


def init():
    git("init")
    url = input("Remote server url: ")
    if url != "":
        addAll()
        commit("Initial commit")
        git("remote add origin " + url)
        git("push --set-upstream origin master")


def addAll():
    git("add .")


def quit():
    exit()
