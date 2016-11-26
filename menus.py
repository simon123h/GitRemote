import functions as f

main = [
            ['u', 'P[u]ll', f.pull],
            ['c', '[c]ommit', f.commit],
            ['p', '[p]ush', f.push],
            ['m', '[m]ore', f.more],
            ['Q', '', f.quit]
        ], "Main Menu", 0


more = [
            ['s', '[s]tatus', f.status],
            ['C', '[C]ommit', f.commit],
            ['P', '[P]ush', f.push],
            ['r', '[r]eturn', f.main]
        ], "More Menu", 1
