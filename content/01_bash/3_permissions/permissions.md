# 404 Not Found

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

