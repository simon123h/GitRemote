from gitAPI import git
from gitRemote import openMenu
import menus


def pull():
    git("pull")
    main()


def commit():
    git("pull")


def push():
    git("pull")


def more():
    openMenu(menus.more)


def main():
    openMenu(menus.main)


def status():
    git("status")
