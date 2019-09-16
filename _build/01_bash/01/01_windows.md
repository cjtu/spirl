---
redirect_from:
  - "/01-bash/01/01-windows"
title: 'Windows Users'
prev_page:
  url: /01_bash/01/00_shell.html
  title: 'Introduction'
next_page:
  url: /01_bash/02/00_basics.html
  title: 'Bash Basics'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Getting Bash on Windows

Lament not, ye weary and burdened Windows users! There are many ways to get access to a bash shell on Windows.

*Note*: None of these are needed for this course, but they are mentioned here for future reference.

| Option | Pros   | Cons |
| ------ | ------ | ---- |
| [Virtual Machine (VM)](https://lifehacker.com/how-to-set-up-a-virtual-machine-for-free-1828969527) | Run Linux as a program in Windows. | Can be slow |
| [Dual-boot](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/) | Install Linux alongside Windows | Requires you to reserve space for another OS on your hard drive. Also, partitioning your hard drive could be risky. |
| Cloud ([Google Cloud](https://cloud.google.com), [Amazon AWS](https://aws.amazon.com/), [Microsoft Azure](https://azure.microsoft.com)) | Accessible from anywhere, can request more resources as you need them. | More technical to setup. Generally charges by the hour which can get costly. |
| *Windows 10 only*: [Windows Subsystem for Linux](https://itsfoss.com/install-bash-on-windows/) | Setup is easy and free. Integrated with Windows for easy access to your files | Still in development |

Of these options, I would recommend the Windows Subsystem for Linux. It allows you to install Ubuntu from the Windows store and gives you an almost seamless Bash experience while still logged in and able to use your Windows PC and programs as usual. I would also recommend getting an X server which will allow graphical programs started from Bash to run in Windows ([installing VcXsrv](https://seanthegeek.net/234/graphical-linux-applications-bash-ubuntu-windows/)).
