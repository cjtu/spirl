# Bash Basics

If you have access to a Mac Terminal or Bash shell, open it up to practice these basic commands. If not, you can use an online *emulator* like [this one](https://www.masswerk.at/jsuix/index.html), but your capabilities may be slightly limited. There is also a [bash cheat sheet](https://www.cheatography.com/gregcheater/cheat-sheets/bash/) which you may find helpful to have up while working in the shell.

## Hello World

Type the following code into your shell and press enter:

```bash
echo "Hello World"
```

Did you type it out? Seriously try it!

## Navigating the shell

You can navigate your operating system's files using a few simple commands in the shell.

### Working directory

For starters, we can always check where we are, our *working directory*, with the `pwd` (print working directory) command.

```bash
pwd
```

The *path* that you see tells you where you are. Each `/` denotes a *directory* (or folder). For example, if your working directory is `/home/username`, it means you are in the `username` folder in the `home` folder.

### Root directory

On a UNIX system (MacOS or Linux), the initial `/` is called the *root directory*. It is the very top level of your file system and contains all of your system's files and folders,

Your computer's hierarchy of files are like a branching tree. Starting from the root directory, we will learn to navigate up and down directories (branches) and make new files (leaves).

![file_tree, CSE 124 Fall 2017. (c) George Porter 2017](../../images/file_tree.png)

Note: The Windows file system is a little different. Windows separates your files and folders from the system-reserved files with different *drives* (e.g. `C://` or `D://`).

### Changing directories

When you open a new shell, you typically start in your *home directory*. Each user on a Linux computer has their own home directory, typically at the path `/home/<username>`. The symbol `~` (tilde) is shorthand for your home directory.

Let's use the `cd` (change directory) command to navigate to the root directory, `/`.

```bash
cd /
pwd
```

Now we're in `/`, let's see what files and folders are here.

### Listing files

Make sure you're in the root (`/`) directory with `pwd`. If you are not, `cd /`.

Now use the `ls` (list) command to see what's here.

```bash
ls
```

Here are the files and folders that are in root. Many of them are directories maintained by the operating system that you don't need to worry about.

Recall the path to your home directory `/home/<your_username>`. Let's see if we can get there from the root directory. First we want to change directory to `/home/`.

```bash
cd home
pwd
```

If we use `ls` here, we can see all of the users with a home directory on this machine. If this is your personal computer, you should just see your username.

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
cd ~
ls
```

### Make directory

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

### Making am empty file

Now let's make a new file. The easiest way to make a file is with the `touch` command.

```bash
touch myfile.txt
```

Touch makes an empty file with the name that you gave it. Let's see if it's there:

```bash
ls
```

### Making a file with text

Great! Now let's say we want to quickly make a file with a line of text in it. Bash has a handy trick for this which combines two parts. This first is the `echo` command.

```bash
echo 'Hello World!'
```

Echo simply prints out the string of characters that you pass to it. The second part is the `>` (redirection) command. Redirection takes the output of the command on the left and puts it into the command or file on the right.

Using `echo` and `>` together allows us to make a simple text file quickly! Let's make a new file called `test_file.txt` containing one line with the words `Hello World`.

```bash
echo 'Hello World!' > test_file.txt
```

Use the list command to see if the file was created:

```bash
ls
```

### Viewing text in files - less is more

Now that we have a text file, we can quickly check its contents with the `less` command. Press `q` to exit `less` (and most command line dialogs you get trapped in).

```bash
less test_file.txt
```

Less allows us to view text interactively on the command line, but what if we just want to print out the contents of a file? Try the `more` command.

```bash
more test_file.txt
```

Although `less` is a new and improved version of `more` (confusingly), `more` can be used to quickly dump files to the shell or even to redirect output into a new file.

```bash
more test_file.txt > test_file2.txt
ls
```

And to see the contents of our new file:

```bash
more test_file2.txt
```

This is a simple way we can copy files with what we already know, but bash make it even easier for us.

## Manipulating files

Let's learn some commands for manipulating files.

### Copy

To copy a file, we use the `cp` command. Let's give our copy a creative new name like `copy_file.txt`.

```bash
cp test_file.txt copy_file.txt
ls
```

Check the contents of the copied file with `more`.

```bash
more copy_file.txt
```

### Move

We can move files using the `mv` (move) command. The move command takes a file or directory and moves it to a new path like so: `mv file_or_dir /new/path`.

If you've been following along this tutorial, move your `test_file.txt` to the home directory.

```bash
mv test_file2.txt ~
```

To see if we were successful, we can use `ls` without changing directories. Just give the path to the directory you want to list, in this case the home directory:

```bash
ls ~
```

### Rename

Great! The `mv` command also has another fun trick which is renaming files. To do this, you "move" the file to the same directory, but with a new name. Rename `test_file2.txt` to `awesome_file.txt`.

```bash
mv test_file2.txt awesome_file.txt
ls
```

### Remove

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

Got an error? Here, `rm` is making sure we don't accidentally delete a directory full of files we may need. To proceed with removing a directory we need to add an **option** to the `rm` command. 

### Info

Options are used to modify the behavior of bash commands. To see what options are available, we can use the `info` (information) command - you can also use the unnecessarily gendered `man` (manual page) command.

```bash
info rm
```

Remember to hit `q` to leave most scary dialogs in the shell. Did you notice the `-d` or `--dir` option for removing directories?

Adding `-d` or `--dir` to `rm` do the same thing, the `-d` is just shorter for us lazy folks who can't bear to type 3 extra characters.

```bash
rm -d test
ls
```

Looks like `rm` is looking out for us again because the directory is not yet empty. Let's see what is still in there.

```bash
ls
```

### Wildcard

Inserting a wildcard into a path will match any path with any number of characters replaced by the `*`.

For example, if a directory called `data/` has `a.txt b.png c.txt` in it, the path `/data/*.txt` will match only `a.txt` and `c.txt`. Alternatively, the path `data/*` will match all three files.

Let's use the wildcard to delete all files in the `test/` directory:

```bash
rm test/*
ls test
```

Now test should be empty. Finally, let's remove `test/` with the `rm -d` command.

```bash
rm -d test
```

And it's gone! Like most things in bash that take a few steps, they can be shortened with **options**.

Remove has a `-f` (force) option and a `-r` (recursive) option. Combining these will remove all file and folders at the given path. The equivalent to clearing the directory and deleting it would have been:

```bash
rm -f test
```

And if test had sub-directories, we would have needed to use:

```bash
rm -rf test
```

*Caution*: You can delete a lot of files very quickly using `rm -rf`. Make sure you know what is at the path you are deleting before you use this command. That being said, everyone makes mistakes, which is why we encourage everyone to backup their files with [version control](../../02_git/why-git), but more on that later.

## Learning more

Bookmark this [cheat sheet](https://www.cheatography.com/gregcheater/cheat-sheets/bash/) for all of the basics we covered here and more. The next section covers **permissions**, which determines who can read, write and run the different files on your computer.
