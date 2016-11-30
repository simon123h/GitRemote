import functions as f

main = [
            ['u', 'Pull', f.pull],
            ['c', 'Commit', f.commit],
            ['p', 'Push', f.push],
            ['m', 'More', f.more],
            ['d', '', f.diff],
            ['s', '', f.status],
            ['l', '', f.log],
            ['b', '', f.branching],
            ['i', '', f.init],
            ['e', '', f.evenMore],
            ['a', '', f.addAll],
            ['b', '', f.branching],
            ['C', '', f.committing],
            ['P', '', f.pulling],
            ['Q', '', f.quit]
        ], "Main Menu", 0


more = [
            ['d', 'Diff', f.diff],
            ['s', 'Status', f.status],
            ['l', 'Log', f.log],
            ['b', 'Branching Menu', f.branching],
            ['a', 'add All files', f.addAll],
            ['i', 'Init new repo', f.init],
            ['C', 'Committing Options', f.committing],
            ['P', 'Pulling Options', f.pulling],
            ['e', 'even More', f.evenMore],
            ['r', 'Return', f.main],
            ['Q', 'Quit', f.quit]
        ], "More", 1


evenMore = [
            ['r', 'Return', f.more]
        ], "Even More", 2


branching = [
            ['n', 'New branch', f.newBranch],
            ['l', 'List branches', f.listBranches],
            ['s', 'Switch to branch', f.switchBranch],
            ['d', 'Delete branch', f.deleteBranch],
            ['m', 'Merge', f.merge],
            ['b', 'Rebase', f.rebase],
            ['p', 'Push all branches', f.pushAllBranches],
            ['x', 'Set branch as new master', f.setNewMaster],
            ['r', 'Return', f.main]
        ], "Branching", 1


committing = [
            ['q', 'Add all, commit and push', f.addAllCommitPush],
            ['a', 'Re-Commit', f.recommit],
            ['e', 'Empty message commit', f.emptyCommit],
            ['r', 'Return', f.main]
        ], "Committing Options", 1


pulling = [
            ['d', 'Pull and discard local changes', f.pullDiscardLocal],
            ['k', 'Pull and keep local changes', f.pullKeepLocal],
            ['r', 'Return', f.main]
        ], "Pulling Options", 1
