# Installing Anaconda

Anaconda is available for Windows, Mac and Linux. Head to the following link and follow the prompts to the appropriate *Python 3* installer for your system:

[https://www.anaconda.com/distribution/#download-section](https://www.anaconda.com/distribution/#download-section)

**Note for Windows users**: If you use the Windows Subsystem for Linux (Bash on Windows), don't use the Windows install link for Anaconda. Instead, I recommend checking out the following tutorial: [link](https://gist.github.com/kauffmanes/5e74916617f9993bc3479f401dfec7da)


## Install Anaconda via command line is better!
Go to [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual), and scroll down to find **Anaconda Installers**. If you are using Windows or Mac, feel free to install via the **graphical installer**, however, installation via the command line installer is much elegant and clean (default for Linux user)!

Right-click to copy the link for **command line installer**, then use `wget` or `curl -o` in the terminal to download the installation file, e.g.,
```bash
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-MacOSX-x86_64.sh
or
curl -o https://repo.anaconda.com/archive/Anaconda3-2020.07-MacOSX-x86_64.sh
```
(make sure to copy the url from Anaconda web page to get the latest python version).\
After the download is finished, type `bash`, follow by a space, and then type the file name you just downloaded to start the installation, e.g.,
```bash
bash Anaconda3-2020.07-MacOSX-x86_64.sh
```

After the installation is done, type `python` and press Enter to see if you have something like this:
```python
Python 3.7.7 (default, Mar 26 2020, 10:32:53)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
```
Make sure that your python version matchs that shown on the download page, and with **Anaconda, Inc.**.
Type `exit()` to leave.

The benefit of installing via the command line is that you can get rid of the bulky UI (Anaconda-Navigator), and open the ipython, jupyter lab/notebook IDE from the terminal faster. This effect can be more severe when you have a small RAM (<16GB), and less powerful CPUs.



## Note on IDEs

Anaconda comes with a code editor called **Spyder** which can be helpful for working with data (and feels very similar to MATLAB, if you've used that before). Recently, Anaconda began offering [Visual Studio Code](https://code.visualstudio.com/) as an optional download. VS Code is a powerful code editor (often called an IDE, or Integrated Development Environment in programming-speak) which has quickly gained popularity in the software developer and scientific programming communities.

Most IDEs have some useful tools in common:

- auto-completion of functions as you type
- help hints on functions (so you don't need to type `help(function)` every time)
- *linters* which analyze the style of your code to help you make it more readable and get into good style habits
- fast search across many files and directories (ever needed to dig into 15 files to find where a variable is defined?)

If you plan to write code, it is a good idea to install and learn use an IDE. A guide to Python IDEs can be found [here](https://realpython.com/python-ides-code-editors-guide/), and a guide to getting started with Visual Studio Code, my current IDE of choice, can be found [here](https://realpython.com/python-development-visual-studio-code/).

> The downside of the **Spyder** IDE is that it is bulky. You might need to wait for more than a min for it to initialize lots of things every time you open it! Especially for people with not enough RAM!
