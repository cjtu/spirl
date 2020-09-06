# Installing Anaconda

Anaconda is available for Windows, Mac and Linux. Head to the following link and follow the prompts to the appropriate *Python 3* installer for your system:

[https://www.anaconda.com/distribution/#download-section](https://www.anaconda.com/distribution/#download-section)

**Note for Windows users**: If you use the Windows Subsystem for Linux (Bash on Windows), don't use the Windows install link for Anaconda. Instead, I recommend checking out the following tutorial: [link](https://gist.github.com/kauffmanes/5e74916617f9993bc3479f401dfec7da)

## Install Anaconda via command line

Anaconda comes packed with many packages and tools that most users will never use. To get a more lightweight version, consider installing it via the command line. THis is the default for Linux users, but also works in the Windows Subsystem for Linux and Mac Terminal. Go to [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual), and scroll down to find **Anaconda Installers**. Look for your distribution (on Linux or WSL, look for the **Linux** installer. On Mac, look for the Mac command line installer).

Right-click to copy the link for **command line installer**, then use `wget` or `curl -o` in the terminal to download the installation file.

```bash
wget https://repo.anaconda.com/archive/Anaconda3-XXXX.YY-MyOS-x86_64.sh
or
curl -o https://repo.anaconda.com/archive/Anaconda3-XXXX.YY-MyOS-x86_64.sh
```

The links above are examples, make sure to copy the url from Anaconda web page [here](https://www.anaconda.com/products/individual) for the latest version.

After the download is finished, run the script by typing `bash` followed by a space, and then the name of the file you downloaded.

```bash
bash Anaconda3-XXXX.YY-MyOS-x86_64.sh
```

After the installation is done, type `conda -V` to test if it installed successfully.

```bash
conda -V
# conda 4.8.3
```

If you see a version number, you should be all set.

## Installing the graphical installer

If you are working on Mac of Windows and are less comfortable with the command line, you can also get all of Anaconda's features with the graphical installers at the same link. These take up more disk space and may run a little slower. These rest of this chapter assumes you are interacting with Anaconda from the command line.

## Note on IDEs

Anaconda comes with a code editor called **Spyder** which can be helpful for working with data (and feels very similar to MATLAB, if you've used that before). Recently, Anaconda began offering [Visual Studio Code](https://code.visualstudio.com/) as an optional download. VS Code is a powerful code editor (often called an IDE, or Integrated Development Environment in programming-speak) which has quickly gained popularity in the software developer and scientific programming communities.

Most IDEs have some useful tools in common:

- auto-completion of functions as you type
- help hints on functions (so you don't need to type `help(function)` every time)
- *linters* which analyze the style of your code to help you make it more readable and get into good style habits
- fast search across many files and directories (ever needed to dig into 15 files to find where a variable is defined?)

If you plan to write code, it is a good idea to install and learn use an IDE. A guide to Python IDEs can be found [here](https://realpython.com/python-ides-code-editors-guide/), and a guide to getting started with Visual Studio Code, my current IDE of choice, can be found [here](https://realpython.com/python-development-visual-studio-code/).

