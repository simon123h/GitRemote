import functions as f


main = [
            ['u', 'Pull', f.pull, 'Pull from Remote'],
            ['c', 'Commit', f.commit, 'Commit new changes'],
            ['p', 'Push', f.push, 'Push commits to server'],
            ['m', 'More', f.more, ''],
            ['d', '', f.diff, 'Check difference to last commit'],
            ['s', '', f.status, 'Git Status'],
            ['l', '', f.log, 'Git Commit Log'],
            ['b', '', f.branching, ''],
            ['i', '', f.init, 'Initiate new repo'],
            ['e', '', f.evenMore, ''],
            ['P', '', f.pulling, ''],
            ['U', '', f.updateAllRepos, 'Recursively updating all git repos in folder'],
            ['o', '', f.console, 'Opening Console'],
            ['Q', '', f.quit, 'Quitting']
        ], "Main Menu", 0


more = [
            ['d', 'Diff', f.diff, 'Check difference to last commit'],
            ['s', 'Status', f.status, 'Git Status'],
            ['l', 'Log', f.log, 'Git Commit Log'],
            ['b', 'Branching Menu', f.branching, ''],
            ['i', 'Init new repo', f.init, 'Initiate new repo'],
            ['Q', 'Quit', f.quit, 'Quitting'],
            ['m', 'even More', f.evenMore, ''],
            ['r', 'Return', f.main, '']
        ], "More", 1


evenMore = [
            ['o', 'Open Console', f.console, 'Opening Console'],
            ['C', 'Committing Options', f.committing, ''],
            ['P', 'Pulling Options', f.pulling, ''],
            ['i', 'Simple GitRemote', f.openSimple, ''],
            ['r', 'Return', f.more, '']
        ], "Even More", 2


branching = [
            ['n', 'New branch', f.newBranch, ''],
            ['l', 'List branches', f.listBranches, 'Listing all branches'],
            ['s', 'Switch to branch', f.switchBranch, ''],
            ['d', 'Delete branch', f.deleteBranch, ''],
            ['x', 'Work on previous version', f.setNewMaster, ''],
            ['m', 'Merge', f.merge, ''],
            ['b', 'Rebase', f.rebase, ''],
            ['p', 'Push all branches', f.pushAllBranches, 'Pushing all branches'],
            ['x', 'Set branch as new master', f.setNewMaster, 'Set current branch as new master'],
            ['r', 'Return', f.main]
        ], "Branching", 2


committing = [
            ['q', 'Add all, commit and push', f.addAllCommitPush, 'Quickly commit all changes and push them'],
            ['a', 'Re-Commit', f.recommit, 'Re-Commit (Amend commit)'],
            ['e', 'Empty message commit', f.emptyCommit, 'New commit (empty message allowed)'],
            ['r', 'Return', f.main, '']
        ], "Committing Options", 3


pulling = [
            ['d', 'Pull and discard local changes', f.pullDiscardLocal, 'Pulling from server, all local changes will be discarded'],
            ['k', 'Pull and keep local changes', f.pullKeepLocal, 'Pulling from server, but local changes are kept for the next commit'],
            ['U', 'Pull all repos', f.updateAllRepos, 'Recursively updating all git repos in folder'],
            ['r', 'Return', f.main, '']
        ], "Pulling Options", 3


simple = [
            ['s', 'Sync', f.simpleSync, 'Syncing..'],
            ['r', 'Return', f.main, '']
        ], "Simple GitRemote", 0
