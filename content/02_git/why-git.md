# Lesson 1: Version control with Git

## Version control

Has one of these happened to you?

- "I accidentally deleted my code and now I'm sad"
- "I broke something in my code and I can't remember how it was"
- "I don't know if I meant to send my collaborator `code_v3_oct31_2018_A1.py` or `code_v3_oct31_2018_B7.py`"
- "My collaborator changed half of my code, but I've updated it a bunch since I sent it to them 6 months ago and now I don't know how to combine the two"


Version control systems were developed to solve these challenges of collaborating on code that changes over time. Different version control systems differ in the nitty gritty of their inner workings, but they all allow multiple collaborators to work on the same code, and to revert code to old snapshots if something breaks.

If you are working with collaborators on code, having a version control system in place will make your lives much easier.

### I fly solo, why bother?
If you mostly work on your science and your code by yourself, you might wonder why you would ever need version control. Non-collaboration bonuses:

1) You always have time-stamped snapshots of your code that you can revert to if something breaks.

2) Version control makes it really easy to host a backup of your code on a local or remote server.

3) You can easily keep code up to date on multiple machines, say, if you're working via ssh on a remote computer or in the cloud. :wink:

4) Git hosting sites (like GitHub) provide a well-established way to share your beautiful science analysis and/or code that won't fit in the footnotes of a paper.


## WTG?! (What the Git)
You should have an idea of what Git *does* from the pre-class homework, but what *is* Git? 

**Git: the software** is a super efficient and popular choice of version control system.

**Git: the philosophy** or **gitflow** is a workflow and set of practices about how to develop and share code. **Gitflow** can make our academic coding a lot more organized, reproducible and shareable in the long run.

### The basics: repos
A Git **repository** or **repo** is simply a directory that is tracked by Git. Any old directory can be turned into a Git repository with the `git init` command. This command dumps some files in a hidden `.git` folder, and from then on Git will track all changes to the new repo and its contents.

### The basics: commits
You can think of Git **commits** as snapshots or checkpoints in the history of your repo. You have complete freedom over how often you make commits and what message you leave to descibe your commit.

Take a walk with me to the year 2020 (or <current_year>+2 if you're joining us from the future). You've been tracking your research in a git repo and a collaborator asks for a function, `awesome_func()` that you remember writing about 2 years ago. The problem is you deleted that function because you didn't need it. Thanks to the magic of git, you have a checkpoint with it somewhere... 

When you look at your git commit history to find it, which would you rather see?

> s87f6s9 - I added stuff (Thu Nov 1, 2018)  
> klh54as - deleting stuff (Fri Nov 30, 2018)  
> f984jst - whoops (Sat Dec 1, 2018)  
> un23hc8 - adds a whoooole lotta stuff from December (Fri Dec 28, 2018)  

Or:

> s87f6s9 - Add awesome_func() to improve performance of slow_func() (Thu Nov 1, 2018)  
> klh54as - Fix a bug in awesome_func() that made it crash (Fri Nov 2, 2018)  
> f984jst - Remove awesome_func() in favor of even_better_func() (Fri Nov 9, 2018)  
> un23hc8 - Added figures to even_better_func() (Tue Nov 13, 2018)  

An important part of **Git: the philosophy** is making commits that are retrievable later. Some guiding principles will have you committing like a pro in no time:

1) Commit often
2) Leave descriptive commit messages 
3) Make commits atomic (single units of work)

1: How often depends on your work. When in doubt, commit more.

2: Descriptive mesages can save a lot of headache later. This is an easy habit to make, while leaving bad messages is a hard habit to break. Note: Git convention is to start the commit message with a singular verb ("Add...", "Fix...", "Revert...", etc).

3: Commits are the building blocks of your repo. If a mistake slips into your code in an enormous commit, it will be much harder to find that mistake later than if you commit in small, single units of work. This is the hardest of the 3 rules and takes a bit of practice. When in doubt, ask yourself: "Does this commit add/change/fix one thing?" if not, consider splitting it up into 2 (or more) commits.

### The basics: branches
Git repos start out with one main **branch** called `master`. Branches are used to split off from the `master` history for awhile, usually with the eventual goal of **merging** back into `master`.

Why branch? Say you have a program `code.py` that reads a bunch of numbers from a text file and does some math on them. This code works and you're happy with it, but you want to also be able to read from Excel spreadsheets. You might be worried about breaking your code while you add this new feature. Without Git, you could make a copy of your code called `code_excel.py` and add the functionality. You get it working but you had to change `code.py` a bunch and now you have two different programs to do almost the same thing.

This is where **branches** come in. If, instead you make a Git branch called `import-excel` and developed your new feature in `code.py` on this branch, you don't have to worry about ever breaking `code.py` on the `master` branch. You can even continue to use your perfectly good `code.py` on `master` while you finish up the new version. When the new `code.py` is ready and you've verifie that it works on both Excel and text files, you can **merge** `import-excel` back into `master`.

The **gitflow** philosophy of branching:
- When working with others, all new features, bug fixes, or other changes should be made on their own **branch**. 
- When your feature is ready, a collaborator should *review your changes* to ensure they do not break `master`. 
- When it is ready, the feature can be **merged** back into `master`

This ensures that the `master` branch is always in good working order and usable by you and your collaborators.

### The basics: HEAD
The shorthand `HEAD` tells Git where you currently are in history (which **branch** and which **commit**). When you make a new commit, `HEAD` moves with you to that commit. When you undo a commit, `HEAD` move back to the last commit. When you switch to a new branch, Git moves HEAD to the most recent commit on that branch.

![git commit](../../images/commit.png)

If you ever end up in `detached HEAD` state, it simply means that Git got lost somehow (e.g. if you deleted the branch you were currently on), and it doesn't know where to point `HEAD`. From here you can `git checkout` to move to any of your existing branches and re-atttach your `HEAD`.

## Git on with it
We have some ideas to guide us, so let's practice. 

### Checking if Git is installed
Let's check if Git is installed.
```bash
git --version
#git version 2.17.1
```
If there is a version number, great! Skip to [Configuring your Git](#configuring-your-git).

If there is no version number, you will need to install Git (this requires administrator access). 

In Ubuntu, you can run: 
```bash
apt-get install git
```

For other Linux distributions, find guidance at https://git-scm.com/download/linux.

For Mac, the `git --version` command should have prompted you to install it.

For Windows see [lesson 0](../lesson0) for why we use a UNIX based OS for this course. If you are adamant about coding on windows and do not have the Windows Subsytem for Linux, you can use https://gitforwindows.org/. Git for Windows provides a bash-like shell called *Git BASH* that emulates the standard bash shell and should work with the same commands we will be using here.

### Configuring your Git
The first thing to do when using git on a new machine is to configure your credentials so that you get credit for your commits. To do this, use the `git config --global` command (`--global` configures all of current and future repos, `--local` configures a single repo).
```bash
git config --global user.name "<Your Full Name>"
git config --global user.email "<your.email@somewhere.com>"
```

If you have a GitHub account, I recommend using the same email that is associated with your account.

### Making a local repository from scratch
Create a new directory called `lesson1` and `cd` into it.
```bash
mkdir lesson1
cd lesson1
```

Let's initialize `lesson1/` as a Git repo.
```bash
git init
# Initialized empty Git repository in ~/projects/lesson1/.git/
```

You can check that the hidden `.git` folder was created using `ls -a`.
```bash
ls -a
# .  ..  .git
```

Great! That's all there is to it. Git will now track all changes in `lesson1/`.

### Making our first commit
Let's make a new file and see if Git notices. Let's use our bash redirection trick from lesson0.
```bash
echo 'Hello World' > file1.txt
```

Since Git is tracking this directory, it should have noticed the change. You can always check what Git is seeing with `git status`.
```bash
git status
# On branch master

# No commits yet

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)

#         file1.txt

# nothing added to commit but untracked files present (use "git add" to track)
```

Git status tells us that we have an *untracked file* in our directory. Before we commit file(s) to history, we must first `add` them to the **staging area**. 
```bash
git add file1.txt
git status
# On branch master

# No commits yet

# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)

#         new file:   file1.txt
```

Now Git status shows a *new file* in the **staging area** (i.e. under "Changes to be committed"). We can move files to and from the staging area at will without changing history. Only once we are happy and `commit` will all of the changes be recorded in Git history. Let's make our first commit (remember: *descriptive* commit messages!).
```bash
git commit -m "Add hello world to file1.txt"
# [master (root-commit) 8a7625f] Add hello world to file1.txt
#  1 file changed, 1 insertion(+)
#  create mode 100644 file1.txt
```

Great! Let's double check that everything got cleared from the staging area with one more `git status`.
```bash
git status
# On branch master
# nothing to commit, working tree clean
```

To summarize, your files can be in 3 possible places according to Git. The **working directory**, the **staging area**, or in **history**. You just moved `file1.txt` from your **working directory** to the **staging area** with `git add`, then into **history** with `git commit`. The following figure summarizes how to move between the 3 areas.

![git areas](../../images/git_at_a_glance.png)

### Reverting a commit
We can also move files out of history and out of the staging area too. Let's make a second test commit to practice this. Like before, make a file, add it to the staging area and then commit it. This time let's use `touch`, a command that makes new empty files.
```bash
touch f2.txt
git add f2.txt
git commit f2.txt -m "Make empty file f2.txt"
```

Let's check that our new commit is in history with the `git log` command.
```bash
git log
# commit 00eb672faf8aa02903de965e5cf91b0feee032c7 (HEAD -> master)
# Author: Christian Tai Udovicic <cj.taiudovicic@gmail.com>
# Date:   Sun Nov 4 22:36:37 2018 -0700

#     Make empty file f2.txt

# commit 8a7625fd943aacc1f9bb722ddffb210990b23d9b
# Author: Christian Tai Udovicic <cj.taiudovicic@gmail.com>
# Date:   Sun Nov 4 21:29:03 2018 -0700

#     Add hello world to file1.txt
```

Git log gives detailed info including the long commit address, the author, the full date and the commit message. This can be overwhelming, especially when dispaying a large number of commits. Let's make `git log` cleaner with the `--decorate` and `--oneline` flags.
```bash
git log --oneline
# 00eb672 (HEAD -> master) Make empty file f2.txt
# 8a7625f Add hello world to file1.txt
```

Now we can more clearly see that there are 2 commits, the first "hello world" commit, and the new "empty file" commit. Notice that `HEAD` is pointing to the most recent commit.

Now we try reverting a previous commit. Git reset needs a commit ID to reset to, in my case it would be **8a7625f** (you can check your git log for your commit ID). Alternatively, we can use the shorthand `HEAD~1` or simply `HEAD~` to mean the previous commit (Likewise, `HEAD~2` would be the second last commit, etc.). Here, the `--soft` flag dumps your most recent commit back into the **staging area** rather than the **working directory**
```bash
git reset --soft HEAD~
git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)

#         new file:   f2.txt
```

Great, now our last commit, which consisted of the new file `f2.txt`, is back in the staging area. What do you think happed to the commit history?
```bash
git log --decorate --oneline
# 8a7625f (HEAD -> master) Add hello world to file1.txt
```

The second commit was removed and `HEAD` was moved back to our first commit.

Finally we can remove files from the staging area with `git reset`.
```bash
git reset
git status
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)

#         f2.txt

# nothing added to commit but untracked files present (use "git add" to track)
```

Beware, `git reset --hard` will completely reset all files in the repo to the commit ID you supply. The changes you reset will be lost forever! Use with caution.

Finally, say you just committed some files but forgot to include a file in your staging area that was relevant to that commit. You have 3 options:

1) Add the missing file in another commit (this spreads your single unit of work over 2 commits which is not ideal)
2) Reset the last commit, make sure all your files are in the staging area, then commit again (this can be annoying if you had a lot of changes but only 1 missed file)
3) Make an *amendment* to the last commit with `git commit --amend`

Warning: Amend should be used carefully because it *rewrites history* by changing a commit which is already in the Git history. That being said, amend can make your Git history much cleaner and your collaborations easier.

We still have our empty `f2.txt` in our **working directory**. Say we wanted to include it in our first commit to the repo, but do not want to edit the commit message. We need to add `f2.txt` to the staging area and then use `git commit --amend --no-edit`.
```bash
git add f2.txt
git commit --amend --no-edit
# [master f7b2678] Add hello world to file1.txt
#  Date: Mon Nov 5 11:14:11 2018 -0700
#  2 files changed, 0 insertions(+), 0 deletions(-)
#  create mode 100644 f2.txt
#  create mode 100644 file1.txt
git status
# On branch master
# nothing to commit, working tree clean
git log --oneline
# f7b2678 (HEAD -> master) Add hello world to file1.txt
```

Note that there is still only one commit in history with the same message, but that the commit ID changed! You have re-written history! This is ok to do locally, but beware re-writing history in a repo shared with your collaborators.

Getting the hang of moving files from the working directory to the staging area and into history is the first step to becoming fluent in Git. Don't worry if it's still a little unnatural, we will get lots of practice in the coming weeks!

## Remotes and GitHub
Many git beginners (myself included) confuse **Git** and **GitHub** at first. Git is the software that has been keeping track of our files so far, while **GitHub** is a website where Git repos are stored/hosted. There are other websites that also specialize in hosting git repos (e.g. **GitLab**, **BitBucket**, etc). GitHub is by far the most used and most widely recognized open source platform in world. It is where many useful scientific packages are developed and made available to the community (e.g. astropy, emcee, scikit-learn). Using GitHub for this course will give you some insight into how these packages are developed and will hopefully help you find some open-source code to use in your research.

### Finding the remote

So far, our `lesson1/` repo only exists locally. This is fine for keeping track of our personal code, but what if our hard drive dies or we want to share our code?

This is where **remotes** come in. The remote tells git where another version of your repository on another computer is located. In our case, our remote will be on GitHub's servers. You could also use an internal lab server as your remote repo, but then you would only have access to it when you were connected to the same network (or through a **vpn**). The nice thing about hosting sites like GitHub is they are accessible from anywhere with an internet connection and are paid to be reliable.

### GitHub is super free for academics
GitHub allows unlimited free **public** repositories to encourage open-source collaboration. For today, our test repo will be public, but don't worry you can delete it right after if you want! GitHub also offers students and academics a `developer pack` with unlimited free **private** repositories (these are not visible to the public and only accessible by people you add as collaborators). To get these you will need to apply with your university email at one of the links below:

The [Student Developer Pack](https://help.github.com/articles/applying-for-a-student-developer-pack/) comes with unlimited private repos and a ton of extra free stuff.

[Educators and Academic Researchers](https://help.github.com/articles/about-github-education-for-educators-and-researchers/) can also apply for unlimited private repos.

### Our first GitHub repo
To make our first GitHub repository, first log in to https://github.com. If you are just signing up for GitHub, make sure to update your `git config --global user.email <you@somewhere.com>` with the same email address you use to sign up.

Next make a **new repository** (either with the new repository button on your profile, or with the `+` in the upper right).

![new repo](../../images/new_repo.png)

Here, you are given some options. You can name the repository `lesson1` and give it a description if you would like. You will probably only have the option of `Public` for now, but once your application for the Education developer pack comes through, you will be able to make a private repository (see image below). Finally, you can leave the last 3 options blank: no README, no .gitignore, no license (more on these soon).

![create new repo](../../images/create_new_repo.png)

You've made a GitHub repository! Right now it's blank, but GitHub offers some suggestions for starting our repository. Since we want our local `lesson1/` to be tracked by GitHub, we will follow the directions under **…or push an existing repository from the command line**.

The first of two commands will set up your GitHub **lesson1** repo to be the standard, or `origin`, remote for our local `lesson1/` repo. It will then push the `master` branch to `origin` (meaning our local lesson1 commits will be sent to the remote GitHub lesson1 repo). The `-u` tells git that `master` should always be pushed to `origin` from now on.
```bash
git remote add origin https://github.com/<your_github_username>/lesson1.git
git push -u origin master
```

You will need to input your GitHub username and password, and if all went well, you should get a message like:
```bash
# To https://github.com/cjtu/lesson1.git
#  * [new branch]      master -> master
# Branch 'master' set up to track remote branch 'master' from 'origin'.
```

Now head back to GitHub and click on the **Code** tab or on **lesson1**.

![code tab](../../images/code_tab.png)

Do you see your beautiful `file1.txt`? You just pushed to your first GitHub repo!


### Push and Pull

Now that your local repository is set up to track the remote repository on GitHub, we can `push` new commits to GitHub at any time. This is how we will back up our code and also make it available for collaborators.

If `push` is how we keep our remote repo up to date with our local repo, it would makes sense that `pull` will update our local repo with changes to our remote repo. Let's create a README on GitHUb so we have remote changes to `pull` in.

### Read the README!
On GitHub, the README is the first thing a visitor will see when they look at your repository. In my **lesson1** repo on GitHub, there is a link pestering me to add a `README`. Let's indulge it. From the `Code` tab of your **lesson1** repository on GitHub click on the green `Add README` button, or if you do not see it, click `Create New File`.

![add README](../../images/add_readme.png)

You will be given a text field to add a README to your project. GitHub auto-formats your README based on the rules of a simple text *mark-up* language contrarily named **MarkDown**. Fun fact: this whole couse is written in MarkDown, and it's super easy to pick up (see [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for a great cheatsheet with all you need to know).

![readme text](../../images/readme_text.png)

You can be creative, or here is what I wrote in mine.
```MarkDown
# Welcome to lesson1!

Hello World.

This is my first GitHub repository!

![woohoo](https://media.giphy.com/media/l2JdTAyoFqDY6nEis/giphy.gif)
```

Finally, write a desriptive commit message and click the commit button on GitHub.

![commit readme](../../images/commit_readme.png)

Now we have a commit in our **lesson1** repo on GitHub that is not yet reflected in our local `lesson1` repo.

Let's get our repositories back in sync. From your `lesson1` directory, type the `git pull` command.
```bash
git pull
# Unpacking objects: 100% (3/3), done.
# From https://github.com/cjtu/lesson1
#    8a7625f..b280ade  master     -> origin/master
# Updating 8a7625f..b280ade
# Fast-forward
#  README.md | 7 +++++++
#  1 file changed, 7 insertions(+)
#  create mode 100644 README.md
```

Finally let's verify that everything is in order with `git log`.
```bash
git log --oneline
# b280ade (HEAD -> master, origin/master) Add README.md
# 8a7625f Add hello world to file1.txt
```
Great! The last thing we will do is learn to check out an existing repository on GitHub.

### Clones and Forks

You can check out your `lesson1` repo at any time from any machine by clicking the green `clone or download` button on GitHub to get the url to clone (something like `https://github.com/<user>/lesson1.git`), and then typing `git clone <url>` into the shell.

![clone lesson1](../../images/clone_lesson1.png)

Only you will be able to clone your private repository because you need to supply your GitHub username and password. 

What if you want to clone somebody else's public repo on GitHub, either to use their work or to contribute to their repository?

In this case, we will first need to **fork** the repository on GitHub. This will make a complete copy of the repository under your GitHub profile that you can then clone and edit at will.

To demonstrate this, head over to the repository for this course at https://github.com/cjtu/sci_coding. 

### License and registration (or just license)
Before forking a repository, make sure you check for a [LICENSE](../../LICENSE) file, which should be in the top-level directory. The LICENSE tells you how you may use the contents of a repository and who to cite when using it.

Since open source licenses can be full of legal jargon, https://choosealicense.com is a great resource for choosing or understanding a license. The sci_coding repo is made available through the MIT License, which you can read about [here](https://choosealicense.com/licenses/mit/). Here is the TL;DR (Too Long; Didn't Read) version:

![mit](../../images/mit.png)

According to the MIT License, anybody can use and distribute this entire course, as long as they cite the authors, Christian Tai Udovicic and Alexandre Boivin. This is great news! We're free to fork.

### Forking a repository
On the main page of the [sci_coding](https://github.com/cjtu/sci_coding) repository, you should see a **Fork** button in the upper right.

![fork button](../../images/fork_button.png)

Click this button to make a copy of the repository. After a few seconds you should end up on a page that looks like the original sci_coding repository, but in the upper left, you will see `<your_user>/sci_coding` and below that, `forked from cjtu/sci_coding`.

Great. Now that you have a fork, you can clone the `sci_coding` repo locally. Again, you can click the green `Clone or download` button to get a link to the repository that you can paste in the shell.
```bash
git clone https://github.com/<user>/sci_coding.git
# Cloning into 'sci_coding'...
# remote: Enumerating objects: 69, done.
# remote: Counting objects: 100% (69/69), done.
# remote: Compressing objects: 100% (47/47), done.
# remote: Total 69 (delta 25), reused 56 (delta 16), pack-reused 
# Unpacking objects: 100% (69/69), done.
```

Now you have a copy of the coding course locally which you can edit at will! In a future lesson, we will look at how you can edit a fork of a repo and propose a change to the original repo via a **pull request**.

## Whew
Now that you know the basics of git, version control, and setting up remotes on GitHub, we're all set to start making reproducible and sharable scientific code with Python!

Remember the pre-class homework for next week is [Learn Python](https://www.codecademy.com/learn/learn-python), modules 1-3. 

## Refs
The Git diagrams were borrowed from [A Visual Git Reference](http://marklodato.github.io/visual-git-guide/index-en.html) by marklodato on GitHub. I highly recommend this resource for visualizing how various commands in Git actually work.
