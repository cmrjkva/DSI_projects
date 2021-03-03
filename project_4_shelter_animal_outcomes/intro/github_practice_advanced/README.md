# Github for Teams

In addition to the attached lesson, the below may serve as a quick reference for helping through your git difficulties.

```
repo:
fork on git.generalassemb.ly
git clone the link to your folder   --> Be sure not to nest git repos!

change branches:
git branch --> list existing branches (* by current branch)
git checkout -b working  -->  make new working branch and switch to it
git checkout working  --> switches to existing working branch



submit changes to work
git add . (or filenames) --> label files to be tracked
git commit -m "message"  --> commit changes to local git repo
git push origin working  (or other branch name)  --> upload local git repo to the GHE website

set up links to GHE upstream
git remote -v  --> print out current connections
git remote rm upstream --> remove connection named upstream if it exists
git remote add upstream git@git.......username.....reponame.....git  --> add new link to online repo

update your local repo to match upstream repo
[close jupyter NBs and submit changes to all your work (git add/commit/push)]
git status   --> verify all your work is saved
git checkout master  --> be on master branch
git fetch upstream  --> download the new material from the upstream link
git merge upstream/master --> sync up your master branch with the upstream version of master
git push origin master  --> push your now updated master branch to the GHE website

update your working branch from your new master
[make sure all your work is committed and pushed to GHE]
git checkout working --> make sure you are in the working branch
git rebase master  --> try to update working branch to have the new files from master

At this point you may be done.... unless some files were updated in both branches
[fix all the merge conflicts (see an instructor if you are not comfortable)]

after all the conflicts are resolved:
git rebase --continue   --> will finish the rebase
git status --> verify your work
git push origin working  --> upload your work

or if you are in over your head:
git rebase --abort  --> will revert to the last commit to your working branch
then find an instructor or ask in slack
```
