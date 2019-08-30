# Scripts and Permissions
Each file and folder in a UNIX filesystem has specific permissions defined for who on the system can read, write or execute that file.

## Bash scripts
To show this, let's make a special type of text file called a **bash script**. A bash script is a text file with bash commands (like `cp`, `mv`, `mkdir`, etc) that can be run in order just by running the file. This can be a way to organize many commands rather than inputting them one by one into the shell, or a way to save commands that we want to use again and again.

### The whole shebang

Since a bash script can be any old text file, we need to add a **shebang** (yes that's what it is called) to the top of the file so that bash knows to run the lines of this file as commands. Bash scripts also end in `.sh` by convention, but the shebang is what really tells your computer it is a bash script.

Print the shebang (`#!/bin/bash`) to a new file called `test_script.sh` with a redirect. Make sure to use single quotes.

```bash
echo '#!/bin/bash' > test_script.sh
```

We added the shebang, but we haven't added any commands yet. The plain redirect command will make a new file everytime we try to add more text to the file this way. Luckily, we can use the `>>` command which will add new text to the end of the file.

Let's add a basic `touch` command to our bash script.

```bash
echo 'touch test_script_file.txt' >> 'test_script.sh
```

Let's see our fancy new bash script!

```bash
more test_script.sh
```

We generally run a bash script by typing in its path. We expect this script to make a new file called `test_script_file.txt`. Recall that `.` simply means the directory we are currently in. Let's try it.

```bash
./test_script.sh
```

When I run this I get an error saying `Permission denied`. What happened? To understand, we will need to take a quick detour into **permissions**

## Permissions

So you ran into a permission issue. To diagnose what is going on, let's list the permissions of the files in our directory with `ls -l`.

```bash
ls -l
# -rw-r--r-- 1 ctaiudovicic users  31 Dec 99 23:59 test_script.sh
```

### The permission string

The first 10 characters of gibberish tell you the permissions of your files and folders, as long as you know how to decode it.

- **Char 1** has 2 options: `d` means directory, `-` means file.

- **Chars 2-10**: These 9 characters follow a particular order:
  - User: `rwx` (chars 2, 3, and 4)
  - Group: `rwx` (chars 5, 6, and 7)
  - Others: `rwx` (chars 8, 9, and 10)
  - When the character is shown (e.g. `r` or `w` or `x`), it means yes this person or people have this permission (either `read`, `write` or `execute`, respectively)
  - When there is a `-` in place of the character, it means no they cannot do that action

This figure summarizes this more visually:

![File Permissions in Linux (c) 2017 Clofus innovations](../../images/permissions.jpg)

Let's break down the permissions for our new bash script:

My `test_script.sh`, had the permission `-rw-r--r--`. Recall when the first character is `-`, we know it is a file, not a directory.

Breaking the permission part down into a table:

| Who | Read | Write | Execute |
| --- | ---- | ----- | ------- |
| User | r | w | - |
| Group | r | - | - |
| Others | r | - | - |

So who are these mysterious people?

- **User**: you, because you made and own the file.

- **Group**: you and other users on this machine can be lumped into a group to share files and permissions. If this is your personal computer, this is probably the least relevant.

- **Others**: everyone else that can access this machine that isn't you and doesn't belong to your group.

So in plain English, I, the *User* can *read* and *write* `test_script.sh`, but not *execute* it. All others can only *read* it. This is typically what we want for new files. It is nice to let others see our files, but we don't want Kevin from HR to log in and start messing with them.

### Changing permissions

Now let's give ourselves permission to execute our bash script. We do this with the `chmod` (change mode) command. To specify who to change permissions for (user / group / others / all) we will use `u/g/o/a`, and to specify which permission to change, we will use `r/w/x`. To add a permission, we use `+`, and to remove a permission, we use `-`.

For example if we wanted to hide the contents of a file, we could say `chmod o-r filename`, meaning others no longer have permission to read that file.

Let's give (`+`) ourselves (user or `u`) permission to execute (`x`) the file `test_script.sh`.

```bash
chmod u+x test_script.sh
ls -l
#-rwxr--r-- 1 ctaiudovicic users  12 Oct 29 13:09 test_script.sh
```

Notice the `x` in the user oart of the permission string? Now try to run the script.

```bash
./test_script.sh
ls
```

Did it make `test_script_file.txt` like we expected?

### Summary

Permissions are a rabbit hole, but for our purposes, the key takeaways are:

- when you make a new file, nobody else can change it unless you give them permission
- nobody can execute a file on your computer until you give explicit permission
- make bash scripts executable with `chmod u+x file.sh`
- don't worry about breaking your system by deleting system files - you probably don't have *permission* to
