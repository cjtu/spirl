# Bash Basics

If you have access to a Mac Terminal or Bash shell, open it up to practice these basic commands. If not, you can use an online *emulator* like [JS/UNIX](https://www.masswerk.at/jsuix/index.html), but your capabilities may be slightly limited.

## Hello World

Type the following code into your shell and press enter:

```bash
echo "Hello World"
```

Did you type it out? Seriously try it!

## Navigating the shell

You can navigate your operating system's files using a few simple commands in the shell.

For starters, we can always check where we are with the `pwd` (print working directory) command.

```bash
pwd
```

The *path* that you see tells you where you are. Each `/` denotes a *directory* (or folder). The initial `/` is called the *root directory*. It is the very top level of your file system and contains all of your system's files and folders, at least for Mac and Linux (it's a little different on Windows).

### Going home

When you open a new shell, you typically start in your *home directory*. Each user on a Linux computer has their own home directory, typically at the path `/home/<username>`. The symbol `~` (tilde) is shorthand for your home directory. We can use the `cd` (change directory) command to navigate to the root directory, `/`, then back to home (`~`).

```bash
cd /
pwd
cd ~
pwd
```

### Listing files

Your computer's hierarchy of files are like a branching tree. Starting from the root directory, we will learn to navigate up and down directories (branches) and make new files (leaves).

![file_tree, CSE 124 Fall 2017. (c) George Porter 2017](../../images/file_tree.png)

Let's go back to the root directory.

```bash
cd /
pwd
```

Okay, our path is now `/` so we know we're in root, but what if we want to know what files and folders are in this directory? Try using the `ls` (list) command.

```bash
ls
```

Here are the files and folders that are in root. Many of them are directories maintained by the operating system that you don't need to worry about.

Recall the path to your home directory `/home/<your_username>`. Let's see if we can get there from the root directory. First we want to change directory to `/home/`.

```bash
cd home
pwd
```

If we use `ls` here, we can see all of the users with a home directory on this machine.

```bash
ls
```

Now we're one step away from our home directory (replace `<your_username>` with your username).

```bash
cd <your_username>
pwd
```

### Seeing dots

We made it back home! Now let's check out two shortcuts bash has for navigating, (`.`) and (`..`). Try to change directory to (`.`).

```bash
cd .
pwd
```

Were you surprised you didn't move? The `.` is shorthand for the current directory that we are in. While we probably never want to change directory to the one we're already in, this shortcut will come in handy later on.

Now let's try to cd to `..`

```bash
cd ..
pwd
```

You should have moved up one level to the `/home` directory. The `..` is shorthand for the parent directory of the directory you are currently in. In our tree analogy `..` is a way to move up the branches towards root `/`. Now change directory to `..` once more.

```bash
cd ..
pwd
```

Great! What do you think happens if we cd `..` while we are in the root directory?

```bash
cd ..
pwd
```

Root is the highest level directory (it has no parent directory), so cd `..` keeps us here at `/`.

Now let's take our handy `~` shortcut back to home and start making our own directories.

```bash
cd ~
pwd
```

## Making files and directories

If this is your first time on this Linux machine, your home directory might look pretty empty. 

```bash
ls
```

There may be some hidden files, though. Let's check with the `-a` option to the list command.

```bash
ls -a
```

My home directory has a `.bashrc` and a `.bash_profile` in it (it is ok if you do not have these, we will work with them in the next lesson). The `.bashrc` lets you customize your local bash shell (i.e. on your computer), and your `.bash_profile` lets you customize your remote bash shell (i.e. one that you ssh to). We won't worry about them for now.

Let's make a directory that we can practice in. We do this with the **mkdir** (make directory) command. I will call mine `test`.

```bash
mkdir test
```

You can check if you were successful with the **ls** command.

```bash
ls
```

Now navigate to your new directory.

```bash
cd test
pwd
```

Now let's make a new file. A combination of the `echo` (print) command and bash's `>` (redirection) command can do this quite quickly. Let's make a new file called `test_file.txt` containing one line with the words `Hello World`.

```bash
echo 'Hello world' > test_file.txt
```

We know how to check if the file was created,

```bash
ls
```

And we can quickly view (but not edit) a file with the `less` command.

```bash
less test_file.txt
```

Press `q` to exit less. Great! We've now learned to navigate directories, make our own directories and files, and read files, all without leaving the shell.

## Manipulating files

Say we want to duplicate a file. To do this, we use the `cp` command. Let's give our copy a creative new name like `test_file2.txt`. 

```bash
cp test_file.txt test_file2.txt
ls
```

You can check using `less` that your important file contents got copied over too.

```bash
less test_file2.txt
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
```

Great! The `mv` command also has another fun trick which is renaming files. To do this, you "move" the file to the same directory, but with a new name. Rename `test_file.txt` to `awesome_file.txt`.

```bash
mv test_file.txt awesome_file.txt
ls
```

What if we want to delete a file or directory? We do this with the `rm` (remove) command.

```bash
rm awesome_file.txt
ls
```

We deleted our file, now let's delete our directory. First navigate up to the parent directory then remove the test directory with `rm`.

```bash
cd ..
rm test/
```

Here, rm is making sure we don't accidentally delete a directory full of files we may need. To proceed with removing a directory we need to add an **option** to the `rm` command. Options are used to modify the behavious of bash commands. To see what options are available, we can use the `info` (information) command.

```bash
info rm
```

Remember to hit `q` to leave most scary dialogs in the shell. Did you notice the `-d` or `--dir` option? It sounded like the one we need. Both `-d` and `--dir` do the same thing, as do other options that you see listed together. The `-d` is just shorter (because programmers are lazy and typing the 3 extra characters is too much work).

Let's give it a shot.

```bash
rm -d test
ls
```

And it's gone! Great, you now know how to move, copy, and delete files and directories. You also know how to get help on any command with `info`. Now let's cover one more important basic shell option.

## Wrapping up
I hope this foray into the basics of bash has helped with your aversion to using the shell. We will build on these basics and apply them to actual scientific coding through the next 5 lessons. 

I think a big source of shell anxiety comes from thinking you'll destroy the computer that you are using if you start typing into the black box. Now that you know about permissions, you know you literally couldn't erase all the data on the machine if you tried. You can inadvertantly delete all of *your* data (never run `rm -rf ~`), which is why it is useful to always have backups and snapshots of your super important files.

How you ask?

Tune in next time when we learn about the power of Git and version control. Don't forget to work through the [Learn Git](https://www.codecademy.com/learn/learn-git) modules before the next class!
