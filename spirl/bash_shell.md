# Meet the shell

Terminal? Command line? Shell? Bash? You may have heard different names for that window with the blinky cursor so let's take a quick step back to understand what the shell is.

## Command-line Interface

Your computer has an *operating system*, or **OS**, that takes care of the thousands of operations per second that your computer does so that you can browse cat pictures online without a hitch. Most operating systems have a *graphical use interface*, or **GUI**, that you can navigate with your mouse and get nice visual feedback in return. If you are brand new to programming, you may have only ever used a GUI and didn't even realize it!

![mac gui](images/mac_gui.jpg)

All operating systems also come with a text-based *command-line interface*, or **shell**, to interact with the OS directly. The shell has a different name depending on your OS. On Windows it's called **Command Prompt**, on MacOS it's the **Terminal**, and on Linux it can vary (e.g., **sh**, **fish**, **csh**) but the most common is **bash** which comes with Ubuntu.

The purpose of every shell is to send commands directly to the operating system, but each one speaks a different language. This text works with **bash** for a few reasons:

1. It is used commonly by scientists and is the default shell on many servers and clusters.

2. Since it is now easy to get bash on Windows (see below), we don't need a separate section for the Windows command prompt.

> Starting from macOS Catalina (macOS 10.15), the default login shell for all Mac became **zsh** (before was **bash**). Although **zsh** is similar to **bash** in some ways, not all **zsh** things will work in **bash**, and vice versa. Therefore, please make sure to switch back to **bash** shell via `chsh -s /bin/bash`. You will see the below message every time you open a new terminal window if you are using the bash shell.
```bash
The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
```


## Windows users

Lament not, ye weary and burdened Windows users! There are many ways to get access to a bash shell on Windows.

*Note*: None of these are needed for this course, but they are mentioned here for future reference.

| Option | Pros   | Cons |
| ------ | ------ | ---- |
| [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about) | Official Microsoft-supported method, setup is easy and free, can run any Linux OS without complicated dual-booting or slow virtual machines, full access to all of your Windows files. | Requires Windows 10. |
| [Virtual Machine (VM)](https://lifehacker.com/how-to-set-up-a-virtual-machine-for-free-1828969527) | Self-contained virtual Linux program that will run in a window and can be started, stopped or completely reset at will. | Adds overhead (can be slow) and often limited in terms of CPU power and memory usage. |
| [Dual-boot](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/) | Full version of Linux separate but on the same machine as Windows. Full CPU power and memory use. | Requires you to reserve space for another full OS on your hard drive. Requires partitioning your hard drive (can accidentally delete all your files: advanced users only!). |
| [Google Cloud](https://cloud.google.com), [AWS](https://aws.amazon.com/), [Azure](https://azure.microsoft.com) | Accessible from anywhere, can request more resources as you need them. | High initial overhead (requires advanced / technical background to setup). Charges by resources use / by the hour which can get costly. |

Of these options, I would recommend the Windows Subsystem for Linux (specifically WSL2 if you have an updated version of Windows 10. Setup intructions [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10)). It gives a seamless shell experience while still being able to use your Windows PC and programs as usual. I would also recommend getting a shell emulator ([ConEmu](https://conemu.github.io/) is a good option) and an "X-server" which allows graphical programs to run (e.g. [VcXsrv](https://seanthegeek.net/234/graphical-linux-applications-bash-ubuntu-windows/)).
