from __future__ import print_function
from gitAPI import git
from ui import openMenu
import menus

# Python 2 compitability
try:
    input = raw_input
except NameError:
    pass


"""
    MENUS
"""


def main():
    openMenu(menus.main)


def more():
    openMenu(menus.more)


def evenMore():
    openMenu(menus.evenMore)


def branching():
    openMenu(menus.branching)


def committing():
    openMenu(menus.committing)


def pulling():
    openMenu(menus.pulling)


"""
    Pulling & Pushing
"""


def pull():
    git("pull")


def pullDiscardLocal():
    git("reset --hard")
    git("pull")


def pullKeepLocal():
    git("add .")       # add local changes to staging area
    git("stash")       # save local changes in stash & remove from working tree
    git("pull")        # pull from remote
    git("stash pop")   # reapply local changes


def push():
    git("push")


def init():
    git("init")
    url = input("Remote server url: ")
    if url != "":
        git("add .")
        git("commit -m 'Initial commit'")
        git("remote add origin " + url)
        git("push --set-upstream origin master")


"""
    Committing
"""


def addAll():
    git("add .")


def commit(systemDialog=False, parameters=""):
    git("add .")
    if systemDialog:
        git("commit"+parameters)
    else:
        message = input("Commit message: ")
        git("commit -m ''" + message + "'"+parameters)


def recommit():
    commit(parameters=" --amend")


def emptyCommit():
    commit(False, "--allow-empty-message")


def addAllCommitPush():
    git("add .")
    message = input("Commit message: ")
    git("commit -m ''" + message + "'")
    push()


"""
    Minor functions
"""


def status():
    git("status")


def diff():
    git("diff")


def log():
    git("log")


def quit():
    exit()


"""
    Branching
"""


def listBranches():
    git("branch -av")


def newBranch():
    name = input("Create branch named: ")
    git("checkout -b "+name)
    git("push -u origin "+name)


def switchBranch():
    name = input("Switch to branch named: ")
    git("checkout "+name)
    git("push -u origin "+name)


def deleteBranch():
    name = input("Switch to branch named: ")
    git("branch -d "+name)


def merge():
    name = input("Merge with branch named: ")
    git("merge "+name)


def rebase():
    name = input("Switch to branch named: ")
    git("rebase "+name)


def setNewMaster():
    name = input("Name of branch to set as new master: ")
    git("checkout "+name)
    git("merge --strategy=ours master")
    git("checkout master")
    git("merge "+name)


def pushAllBranches():
    git("push --all -u")




















    pass
