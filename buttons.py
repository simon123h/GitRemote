
	
newButton('Pull', ['git pull']).pack(in_=top, side=LEFT)

newButton('Commit', ['git add .', 'git commit -m']).pack(in_=top, side=LEFT)

newButton('Push', ['git push']).pack(in_=top, side=LEFT)

newButton('Status', ['git status']).pack(in_=top, side=LEFT)

newButton('Log', ['git log']).pack(in_=top, side=LEFT)