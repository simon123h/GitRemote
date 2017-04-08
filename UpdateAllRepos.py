from __future__ import print_function
import os
# import system

cwd = os.getcwd()


# subdirs = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]


# recursively find all git repos within currend working dir
def findRepos(curdir):
    res = []
    subdirs = [name for name in os.listdir(curdir) if os.path.isdir(os.path.join(curdir, name))]
    if ".git" in subdirs:
        res.append(curdir)
    for subdir in subdirs:
        res += findRepos(os.path.join(curdir, subdir))
    return res


print(findRepos(cwd))
