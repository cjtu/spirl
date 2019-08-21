# Lesson 0: Bash Basics

This "pre-lesson" will help familiarize you with the shell, a tool that we will use throughout the scientific coding course!


## Talking to your computer at a low level

If you have mainly used a Windows or Mac computer your whole life like me, you might get a tightness in your chest every time you see something like this:

![terminal angst](./data/terminal.gif)

Even though the pretty graphical user interfaces we're used to using are excellent for most things, the plain old shell can be your best friend if we can get over the anxiety of using it. The motivation for making this part of the course is 3-fold:

1) As someone who is interested in scientific coding, you will probably encounter a shell promt at some point (maybe you have already). Might as well get over the shell angst now while we're all learning!

2) Working in the shell makes things like version control with Git much easier (stay tuned until lesson1 for my motivation behind making Git a part of this course). 

3) Using the shell makes you look like a total hacker!


### Terminal? Command line? Shell? Bash?

I've thrown the word shell around a lot, so let's take a quick step back to understand what we'll be doing.

Every click, scroll, and letter typed on your computer gets translated to a basic language of 0s and 1s that your computer can understand. While we won't be learning binary for this course, nor should you ever have to, we will learn to talk to the computer on a slightly lower level that we might be used to.

All operating systems come with a text based prompt that you can use to talk to your computer on a level between clicks and binary. This prompt has different names on different machines. On Windows, it is called the **Command Prompt**, on Macs, it is called the **Terminal**, and on Linux it is called the **shell** or **Bash**. 

Each type of shell has slight differences in its *shell-scripting* language. The one I will use is **bash**, and I recommend that you do the same for the following reasons: 

1) We will be speaking the same language.

2) Windows command prompt is not as powerful when it comes to installing new software and handling file permissions (more on both of these later).

3) Bash is the default shell you will see on many servers, cloud computing platforms, superclusters, etc. Knowing the basics of bash is the first step to running your code on computers many times faster than the one you are reading this on.

*Disclaimer*: Bash and the Mac Terminal are different flavors of the standard UNIX shell, so this lesson is probably also doable on a Mac (but I have not tested this). I highly reccommend that you use a Linux distribution (e.g. Ubuntu) for this course (this course is developed and tested on Ubuntu 16.04).

If your computer is running Windows or OS X, see below for how to get a bash shell on your computer.

### Lament not, ye weary and burdened Windows and Mac users
There are many ways to get access to a Linux environment for this course. 

#### Edwards group
If you are in the Edwards Research Group, I suggest using a **vpn** to gain access to the computer lab network from your laptop, and then using **ssh** to "talk" to one of the lab computers. This will open a bash shell on your laptop that you will use to run commands on the lab computer. 

A consequence of doing the course this way is that, in less than 6 weeks, you will have a Python environment set up on the speedy lab computers that you can access from the comfort of your own home (or your favorite coffee shop, or anywhere with internet). Also, you couldn't ask for a better way to learn to do "cloud computing", because you will literally be running all of your code on a computer that isn't yours (e.g. *in the cloud*). How exciting!


#### Alternatives to the vpn + ssh method:

If you do not have a convenient Linux machine to ssh to, you have a couple options which I will contrast briefly (but don't take my word for it, you can do your own research too).

| Option                | Pros   | Cons |
| --------------------- | ------ | ----------------------------- |
| Running a *Virtual Machine* (VM) on your computer | You have access to your familiar operating system while your Linux machine just runs in a window. | VM's are limited resource-wise like any other program on your computer, meaning they can be quite slow (depending on your PC). Some are also expensive. |
| Dual-booting your OS (Windows/Mac) and Linux | You get the full Linux experience with your PC's full resources. | This requires you to split your hard drive in two, which may not be feasible if you're low on space. Also, any time you mess with your hard drive you run the risk of corrupting all of your data. |
| Use a cloud service (Google, Amazon, Microsoft) to make you a Linux VM | You can whip up a simple VM for pretty cheap that you can make more powerful as you need it (scalable). | A bit more technical setup than the others. Generally charges by the hour. Starting a VM in the cloud and forgetting it can lead to unexpected monthly bills. |
| *Windows only*: Windows Subsystem for Linux (aka WSL, aka "Bash on Ubuntu on Windows") | Setup is easy and free. You get the best of bash and can still access your Windows files (imposible when using a VM) |Certain things *just don't quite work* yet. Programs are tricked into thinking they are running on Ubuntu, but might malfunction unexpectedly because under the hood it's still Windows. |


## Let's bash it up

Now that we're all on the same page, open up your bash shell and let's practice some basic navigation.

Throughout this course, the code that you should type will be written in blocks like these (while you can copy and paste these blocks, I encourage typing them out to build some muscle memory):

```bash
echo "Hello World"
```

Did you type it into your bash shell? Seriously try it! Coding is a language and you need to practice it to become fluent.

### Navigation

Before we decide where to go, we can always check where we are with the `pwd` (print working directory) command. 

(Note: the `#` (hash) symbol below denotes a comment in bash. I will use comments to show my output so that you can compare. You don't need to type the comment into your shell, but you can try it and see what happens!):

```bash
pwd
#/home/ctaiudovicic
```

The *path* shows me I am in my *home directory* (or folder). Each user on a Linux computer has their own home directory. The symbol `~` (tilde) is shorthand for your home directory. To make sure we're on the same page, we can use the `cd` (change directory) command to navigate to home (`~`).

```bash
cd ~
pwd
#/home/ctaiudovicic
```

Your computer's file system can be thought of as a tree. We will learn to navigate up and down directories (branches) and make new files (leaves). Your home directory is the trunk from which all your files and folders branch out. This isn't the start of the tree, though. 

All Unix filesystems branch out from a single **root directory** (get it? like the root(s) of a tree?). The root directory is simply the `/` at the start of every file path. 

![file_tree, CSE 124 Fall 2017. (c) George Porter 2017](./data/file_tree.png)

Let's go to the root directory.

```bash
cd /
pwd
#/
```

Okay, our path is now `/` so we know we're in root, but what if we want to know what files and folders we can go to from here? Try using the `ls` (list) command.

```bash
ls
#bin             lib         net   srv
#boot            lib64       nfs   sys
#data            local       opt   tmp
#dev             localdata   proc  usr
#etc             lost+found  root  var
#home            media       run   vmlinuz
#initrd.img      misc        sbin  vmlinuz.old
#initrd.img.old  mnt         snap  work
```

Here are the non-hidden files and folders that branch out from root. Many of them are system files that you don't need to worry about. 

Recall the path to your home directory `/home/<your_username>`. Let's see if we can get there from the root directory. First we want to change directory to `/home/`.

```bash
cd home # or 'cd home/' works too
pwd
# /home
```

If we want to check out which other users are on this machine, we can use list to see all of the home directories.

```bash
ls
#ctaiudovicic  jbuz
```

Now we're one step away from our home directory (replace `<your_username>` with your username).

```bash
cd <your_username>
pwd
#/home/ctaiudovicic
```

We made it back home! Now let's check out two shortcuts bash has for navigating, (`.`) and (`..`). Try to change directory to (`.`).

```bash
cd .
pwd
#/home/ctaiudovicic
```

Were you surprised you didn't move? The `.` is shorthand for the current directory that we are in. Why would we ever want to do this? Well, we probably wouldn't want to change directory to our current one, but it will be convenient to use `.` to refer to our current path later on.

Now let's try to cd to `..`

```bash
cd ..
pwd
#/home
```

This appears to have moved up one level to the `/home` directory. The `..` is shorthand for the parent directory of the diectory you are currently in. In our tree analogy `..` is a way to move up the branches towards root `/`. Now change directory to `..` once more.

```bash
cd ..
pwd
#/
```

Great! What do you think happens if we cd `..` while we are in the root directory?

```bash
cd ..
pwd
#/
```

Since root is the highest level directory, it has no parent directory, so cd `..` keeps us here at `/`.

Now let's take our handy shortcut back to home and start making our own directories.

```bash
cd ~
pwd
#/home/ctaiudovicic
```

### Making files and directories

If this is your first time on this Linux machine, your home directory might look pretty empty. 

```bash
ls
#
```

There may be some hidden files, though. Let's check with the `-a` option to the list command.

```bash
ls -a
#.bash_profile .bashrc
```

My home directory has a `.bashrc` and a `.bash_profile` in it (it is ok if you do not have these, we will work with them in the next lesson). The `.bashrc` lets you customize your local bash shell (i.e. on your computer), and your `.bash_profile` lets you customize your remote bash shell (i.e. one that you ssh to). We won't worry about them for now.

Let's make a directory that we can practice in. We do this with the **mkdir** (make directory) command. I will call mine `test`.

```bash
mkdir test
```

You can check if you were successful with the **ls** command.

```bash
ls
#test
```

Now navigate to your new directory.

```bash
cd test
pwd
#/home/ctaiudovicic/test
```

Now let's make a new file. A combination of the `echo` (print) command and bash's `>` (redirection) command can do this quite quickly. Let's make a new file called `test_file.txt` containing one line with the words `Hello World`.

```bash
echo 'Hello world' > test_file.txt
```

We know how to check if the file was created,

```bash
ls
#test_file.txt
```

And we can quickly view (but not edit) a file with the `less` command.

```bash
less test_file.txt
#
#
#Hello World
#(END)
q
```

Press `q` to exit less. Great! We've now learned to navigate directories, make our own directories and files, and read files, all without leaving the shell.

### Manipulating files

Say we want to duplicate a file. To do this, we use the `cp` command. Let's give our copy a creative new name like `test_file2.txt`. 

```bash
cp test_file.txt test_file2.txt
ls
#test_file.txt test_file2.txt
```

You can check using `less` that your important file contents got copied over too.

```bash
less test_file2.txt
#
#
#Hello World
#(END)
q
```

Let's try to move our new file to our home directory using the `mv` (move) command. As we know, there are many ways to specify the home directory. Try one of the following:

```bash
mv test_file2.txt ~ 
mv test_file2.txt ..
mv test_file2.txt /home/<your_username>
```

To test if we were successful, we *could* `cd ~` to go to home and run `ls` to see what is there. But we can also check without changing directories by giving a path to `ls`.

```bash
ls ~
#test test_file2.txt
```

Great! The `mv` command also has another fun trick which is renaming files. To do this, you "move" the file to the same directory, but with a new name. Rename `test_file.txt` to `awesome_file.txt`.

```bash
mv test_file.txt awesome_file.txt
ls
#awesome_file.txt
```

What if we want to delete a file or directory? We do this with the `rm` (remove) command.

```bash
rm awesome_file.txt
ls
#
```

We deleted our file, now let's delete our directory. First navigate up to the parent directory then remove the test directory with `rm`.

```bash
cd ..
rm test/
#rm: cannot remove 'test/': Is a directory
```

Here, rm is making sure we don't accidentally delete a directory full of files we may need. To proceed with removing a directory we need to add an **option** to the `rm` command. Options are used to modify the behavious of bash commands. To see what options are available, we can use the `info` (information) command.

```bash
info rm
# 11.5 ‘rm’: Remove files or directories
# ... Lots of boring info ...
# '-d'
# '--dir'
#      Remove the listed directories if they are empty.
# ...
q
```

Remember to hit `q` to leave most scary dialogs in the shell. Did you notice the `-d` or `--dir` option? It sounded like the one we need. Both `-d` and `--dir` do the same thing, as do other options that you see listed together. The `-d` is just shorter (because programmers are lazy and typing the 3 extra characters is too much work).

Let's give it a shot.

```bash
rm -d test
ls
#
```

And it's gone! Great, you now know how to move, copy, and delete files and directories. You also know how to get help on any command with `info`. Now let's cover one more important basic shell option.

### Permissions
Each file and folder in a UNIX filesystem has specific perissions defined for who on the system can read, write or execute that file.

To show this, let's make a special type of text file called a **bash script**. A bash script is a text file that you can put bash commands into, and run by *executing* that file. All bash scripts start with a **shebang** (yes that's what it is called) and have a filename ending in `.sh`. Print the shebang (`#!/bin/bash`) to a new file called `test_script.sh`. Make sure to use single quotes.

```bash
echo '#!/bin/bash' > test_script.sh
```

We added the shebang, but we haven't added any commands yet. Let's open `test_script.sh` to edit it. 

There are several basic text editors that different people will try to convince you is best. The actual best one is the one you are most comfortable with. Some common editors are vi/vim, emacs, nano and gedit. If you've never used any of these, I recommend emacs because it works pretty similarly to Windows/Mac basic editors.

```bash
emacs test_script.sh # or 'nano test_script.sh'
```

In the text editor, start a new line after the shebang and add `echo "Hello World"`.

```bash
"#!/bin/bash"
echo "Hello World"
```

Make sure to save and then quit the text editor (some editors try to trap you in. If this is the case, Google "How to exit <my_text_editor>"). Now let's run our bash script. We do this by specifying the file location with the `.` shorthand we learned earlier.

```bash
./test_script.sh
# -bash: ./test_script.sh: Permission denied
```

What happened? We ran into a permission issue. To diagnose what is going on, let's list the permissions of the files in our directory with `ls -l`.

```bash
ls -l
# -rw-r--r-- 1 ctaiudovicic users  12 Oct 29 13:09 test_script.sh
```

The permissions of your files and folders are shown in the first 10 characters. It may look like gibberish, but we'll break it down.

Char 1: `d` means directory, `-` means file.

Chars 2-10: `rwx` means yes the specified user has permission to `read/write/execute` and `-` means no they cannot do that action. It goes `rwx` (User), `rwx` (Group), `rwx` (Others).

![File Permissions in Linux (c) 2017 Clofus innovations](./data/permissions.jpg)

To visualize this in a table:

For our test_script.sh, the first character is `-`, so we know it is a file.

| Type |
| ---- |
| - |

| Who | Read | Write | Execute |
| --- | ---- | ----- | ------- |
| User | r | w | - |
| Group | r | - | - |
| Others | r | - | - |

**User**: you, because you made and own the file.

**Group**: other users on this machine that are lumped into the same group.

**Others**: everyone else that can access this machine, that isn't you and doesn't belong to your group.

So, bringing it back to executing the command in `test_script.sh`, what happened? Notice the permissions `-rw-r--r--`. We can translate this to: the user, group and others (i.e. everyone) has permission to read `test_script.sh`, while only the owner has permission to write (edit) it, and nobody has permission to execute it.

Now let's get to the fun part of giving ourself permission to run our script. We do this with the `chmod` (change mode) command. To specify who to change permissions for (user / group / others / all) we will use `u/g/o/a`, and to specify which permission to change, we will use `r/w/x`. To add a permission, we use `+`, and to remove a permission, we use `-`.

Let's give (`+`) ourselves (user or `u`) permission to execute (`x`) the file `test_script.sh`.

```bash
chmod u+x test_script.sh
ls -l
#-rwxr--r-- 1 ctaiudovicic users  12 Oct 29 13:09 test_script.sh
```

Notice the `x` in your user permissions? Now try to run the script.

```bash
./test_script.sh
#Hello World
```

There's a whole rabbit hole of permissions you can read about, but the key takeaways are:

- when you make a new file, nobody else can change it unless you give them permission, and not even you can execute it until you give yourself explicit permission
- you can make your own bash scripts executable with `chmod u+x file.sh`
- you don't have to worry about inadvertantly editing or deleting system files or other users' file on your shared computer, *because you don't have permission*


## Downloading and Installing Anaconda
This course will rely heavily on the use of [Anaconda](https://www.anaconda.com/), a package manager for Python packages and their dependencies. Several useful scientific coding package are available by default in Anaconda, and we will explore how to install and manage additional packages in the coming lessons.

Anaconda provides a setup `.sh` script that we can run to install Anaconda for a given user on a machine. This script does not require administrator privilidges, so don't worry if you normally do not have access to install programs. This will be a 5 step process.

1) We will go to the Anaconda website to get the **url** of the Linux version of Anaconda.

2) We will use `wget <url>` to download the setup script from the shell.

3) We will change the permissions of the script to allow us to execute it.

4) We will run the script and let it install Anaconda for us.

5) We will add Anaconda to our system **PATH** so that we can use the `conda` command from the shell.

### 1) Copy the url
Head to the downloads section of the Anaconda website [here](https://www.anaconda.com/download/#linux). We want the **Linux** version, so click on the Linux tab. Now you will have an option of Python 3.x or Python 2.7. We want the Python 3.x version, but **don't click the Download button**. Under the download button there is a link, `64-Bit (x86) Installer`. Right click (or cmd-click) this link and choose "Copy link address" or "Copy url". This is the url to the Linux installer for the Python 3 version of Anaconda that we will `wget` from the command line.

![download anaconda](./data/download.png)

### 2) Downloading with wget

The `wget` command allows you to download files from the internet without leaving the command line. It simply needs the url of the file to download. 

First change directory to home.
```bash
cd ~
```

You should have the Anaconda installer link still copied, so type `wget` and paste the url (either right click, or ctrl+shift+v) into the shell. 

Note: Anaconda may have changed versions since this was written, so your `<url>` may be slightly different. It should end in something like `Anaconda3-X.X.X-Linux-x86_64.sh`.
```bash
wget <url> # https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh
```

You will see the progress of the download in the shell. When it is done, you should have a `.sh` script from Anaconda in your `~` directory. Let's double check.
```bash
ls
#... Anaconda3-5.3.0-Linux-x86_64.sh ...
```

Great! Now we just need to run this script to get Anaconda installed.

### 3) Changing permissions
Remember that by default, users can only read and write to new files. We can verify this with `ls -l`. 

Note: your script may have a slightly different name, make sure to replace `<script>` with the one you downloaded.
```bash
ls -l <script> # Anaconda3-5.3.0-Linux-x86_64.sh
# -rw-r--r-- 1 christian christian 45071119 Nov  6 13:32 Anaconda3-5.3.0-Linux-x86_64.sh
```

Notice at the start, we have `rw-`, meaning we (the user) can read and write, but not execute the file. Recall: to change permissions, we use the `chmod` command and to allow users to execute a script, we specify `u+x`. 
```bash
chmod u+x <script> # Anaconda3-5.3.0-Linux-x86_64.sh
ls -l <script> # Anaconda3-5.3.0-Linux-x86_64.sh
-rwxr--r-- 1 christian christian 45071119 Nov  6 13:32 Anaconda3-5.3.0-Linux-x86_64.sh
```

Now when we check the permissions, users are able to `rwx`, meaning we're ready to execute the file.

### 4) Running the install script
To run a bash script, we just need to specify its path. Since it is in our current directory, we can use the `.` shorthand.
```bash
./<script> # ./Anaconda3-5.3.0-Linux-x86_64.sh
```

The script will first give you a license to read. Scroll to the bottom and type 'yes'. Then it will take a little while to install all of the packages included in Anaconda. I suggest using the default options for the other questions it asks you. You **do not** need to install VS Code.

When the installation is done, try checking Anaconda's version with `conda --version`.
```bash
conda --version
# Command 'conda' not found
```

Oh no. Anaconda was installed, but bash doesn't know where to find the `conda` command. We can tell it where to look using the system path.

### 5) Adding conda to the system path
Anaconda comes with a bash command called `conda`, which is simply a shell script somewhere on your machine. By default, bash doesn't know about this new script, so we need to tell it to look in the right place.

The system path is a list of locations where bash looks for commands that you type into the shell. Bash keeps this path list in an **environment variable** appropriately named `PATH`. We can access environment variables using the `$` symbol. For example, if we wanted to see the environment variable `HOME` (the path to our home directory), we could type `echo $HOME`.
```bash
echo $HOME
# /home/ctaiudovicic
```  

We can also show the system path with `echo $PATH`. This one is probably quite a bit longer than `$HOME`.
```bash
echo $PATH
# /home/ctaiudovicic/bin:/usr/local/bin:/usr/bin
```

Notice these are just a bunch of directories, each separated by a colon `:`. We want to add the `conda` script directory to this list, but first we need to know where Anaconda was installed. If you used the default location (`/home/<user>/`) then the `conda` script is located in `/home/<user>/anaconda3/bin/` (if you specified a different install loation, replace `/home/<user>/` with the path you specified). Let's check that it is there. Remember to type your username instead of `<user>`.
```bash
ls /home/<user>/anaconda3/bin
# lots of files
```

This should show a huge list of anaconda files, one of which should be `conda`. If you'd like to narrow down the list, we can use the search command `grep`.
```bash
ls /home/<user>/anaconda3/bin | grep conda
# only files that have conda in the name
```

Great! Now we just need to change `PATH` to include this directory. We can change environment variables with `export`. We want to make sure to keep the old system path, `$PATH`, to add a `:`, and finally to add `/home/<user>/anaconda3/bin` (remember to replace `<user>` with your username).
```bash
export PATH=$PATH:/home/<user>/anaconda3/bin
echo $PATH
# /home/ctaiudovicic/bin:/usr/local/bin:/usr/bin:/home/ctaiudovicic/anaconda3/bin
```

Do you see the Anaconda path at the end of `PATH`? Now bash should know where to find the `conda` command! Let's try it.
```bash
conda --version
# conda 4.5.11
```

Great! You successfully added the Anaconda path to your system path and can now use the `conda` command.

There is one small problem. All environment variables revert to normal every time you open a new shell. We don't want to remember to type `export PATH=$PATH:/home/<user>/anaconda3/bin` every single time we login or open a new shell. Luckily, bash allows us to define commands to run every time a new shell is opened.

### 5b) Adding the path to your bashrc / bash profile
There is a special config file with a list of bash commands that you can put in your home directory. Every time bash opens a new shell, it will look for this file and run all of the commands in it. The name of the file it looks for is different depending on how you open your shell.

1) If you open a local bash shell (one on your Linux computer), it will run `~/.bashrc`.

2) If you open a remote shell (one you access via ssh) it will run `~/.bash_profile`.

Determine whether you are case 1 or 2, and edit the appropriate file below (Note: if you are using the Mac Terminal, it does not follow the rules above and *always* looks for the `.bash_profile` when opening a new Terminal).

First we should check if the `.bash_profile` (or `.bashrc`), already exists. Note that because it starts with a `.`, it is an hidden file and we need to use `ls -a` to see it.
```bash
cd ~
ls -a
# .bashrc .bash_profile ...
```

Now use your favorite text editor (vim, emacs, nano, etc) to open your `.bash_profile` (or `.bashrc`). At the bottom, add the following lines.
```bash
# Added by Anaconda3
export PATH=$PATH:/home/<user>/anaconda3/bin
```

The comment `# Added by Anaconda3` doesn't get run, it just reminds you why you put this line in your `.bash_profile` (or `.bashrc`).

Now the system path will have the `conda` path added to it every time you open a shell. To try it, close your shell and re-open it, then type `conda --version`.
```bash
# Closed my shell and opened this new one
conda --version
# conda 4.5.11
```

Great! Now you know how to download from a link with `wget` and Anaconda and the `conda` command is ready to be used for the rest of the course.

### Wrapping up
I hope this foray into the basics of bash has helped with your aversion to using the shell. We will build on these basics and apply them to actual scientific coding through the next 5 lessons. 

I think a big source of shell anxiety comes from thinking you'll destroy the computer that you are using if you start typing into the black box. Now that you know about permissions, you know you literally couldn't erase all the data on the machine if you tried. You can inadvertantly delete all of *your* data (never run `rm -rf ~`), which is why it is useful to always have backups and snapshots of your super important files.

How you ask?

Tune in next time when we learn about the power of Git and version control. Don't forget to work through the [Learn Git](https://www.codecademy.com/learn/learn-git) modules before the next class!
