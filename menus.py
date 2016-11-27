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
            ['Q', '', f.quit]
        ], "Main Menu", 0


more = [
            ['d', 'Diff', f.diff],
            ['s', 'Status', f.status],
            ['l', 'Log', f.log],
            ['b', 'Branching Menu', f.branching],
            ['i', 'Init new repo', f.init],
            ['a', 'add All files', f.addAll],
            ['e', 'even More', f.evenMore],
            ['r', 'Return', f.main]
        ], "More", 1


evenMore = [
            ['r', 'Return', f.more]
        ], "Even More", 2


branching = [
            ['r', 'Return', f.more]
        ], "Branching", 2
