@echo off
title Git Remote

echo  ------------------------
echo         Git Remote       
echo  ------------------------
echo.

echo  [U]pdate from server

:legend
echo  [C]ommit now
echo  [P]ush now
echo  [M]ore
goto choice

:more
echo  [U]pdate from server
echo  [D]iff
echo  [S]tatus
echo  [L]og
echo  [B]ranching
echo  [I]nit new repo
echo  [E]ven More
goto choice

:choice
choice /c cpmudslbie /n /m "> "
if %errorlevel%==1 goto newCommit
if %errorlevel%==2 goto push
if %errorlevel%==3 goto more
if %errorlevel%==4 goto pull
if %errorlevel%==5 echo. & git diff & goto startOver
if %errorlevel%==6 echo. & git status & goto startOver
if %errorlevel%==7 echo. & git log & goto startOver
if %errorlevel%==8 goto branching
if %errorlevel%==9 goto init
if %errorlevel%==10 goto evenMore

:startOver
echo.
echo.
goto legend


:newCommit
echo.
git add .
set /p msg="Commit message: "
git commit -m "%msg%"
set msg=
goto startOver

:push
echo.
REM git push origin master
git push
goto startOver

:pull
echo.
git pull
goto startOver

:init
echo.
git init
set /p url="Remote server url: "
if "%url%" == "" goto startOver
git add .
git commit -m "Initial commit"
git remote add origin %url%
set url=
git push origin master
goto startOver



:branching
echo.
echo Branching
echo  [N]ew branch
echo  [L]ist all
echo  [S]witch to branch
echo  [D]elete branch
echo  [M]erge
echo  re[B]ase
echo  [P]ush all branches
echo  [R]eturn

choice /c rlnsdmp /n /m ">> "
if %errorlevel%==1 goto startOver
if %errorlevel%==2 goto listBranches
if %errorlevel%==3 goto newBranch
if %errorlevel%==4 goto switchBranch
if %errorlevel%==5 goto deleteBranch
if %errorlevel%==6 goto mergeBranch
if %errorlevel%==7 goto rebaseBranch
if %errorlevel%==8 echo. & git push --all -u & goto startOver

:listBranches
echo.
git branch -av
goto startOver

:newBranch
echo.
set /p name="Create branch named: "
git checkout -b %name%
git push -u origin %name%
set name=
goto startOver

:switchBranch
echo.
set /p name="Switch to branch named: "
git checkout %name%
git push -u origin %name%
set name=
goto startOver

:deleteBranch
echo.
set /p name="Delete branch named: "
git branch -d %name%
set name=
goto startOver

:mergeBranch
echo.
set /p name="Merge with branch named: "
git merge %name%
set name=
goto startOver

:rebaseBranch
echo.
set /p name="Rebase with branch named: "
git rebase %name%
set name=
goto startOver



:evenMore
echo  Even More
echo   [E]mpty message Commit
echo   [A]mend Commit
echo   [Q]uick Commit ^& Push
echo   [G]itK
echo   [O]pen CMD
echo   [R]eturn

choice /c reaqgo /n /m ">> "
if %errorlevel%==1 goto startOver
if %errorlevel%==2 goto emptyCommit
if %errorlevel%==3 goto recommit
if %errorlevel%==4 goto quickCommitPush
if %errorlevel%==5 gitk & goto startOver
if %errorlevel%==6 goto console

:emptyCommit
echo.
git add .
git commit --allow-empty-message -m ""
set msg=
goto startOver

:recommit
echo.
git add .
set /p msg="Commit message: "
git commit -m "%msg%" --amend
set msg=
goto startOver

:quickCommitPush
echo.
git add .
set /p msg="Commit message: "
git commit --allow-empty-message -m "%msg%"
set msg=
goto push

:console
echo.
echo Console
echo return with 'exit' command
echo.
cmd
goto startOver









