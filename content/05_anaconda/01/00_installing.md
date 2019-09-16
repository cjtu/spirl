# Downloading and Installing Anaconda
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