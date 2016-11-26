from gitAPI import git
from ui import openMenu
import menus


def pull():
    git("pull")


def commit():
    git("add .")
    git("commit")


def push():
    git("push")


def more():
    openMenu(menus.more)


def main():
    openMenu(menus.main)


def status():
    git("status")
    # main()
