# Jupyter (iPython notebooks)
The **Jupyter Notebook** is an interactive document that combines text and code. By the end of this course, you will be able to write up something to the effect of [this](http://nbviewer.jupyter.org/gist/jhemann/4569783) and post it to GitHub so that anyone can view your data, code, and reproducible results.

For now, we'll use a cool website called [mybinder](https://mybinder.org/) that not only allows you to view Jupyter notebooks, but also allows you to interactively run the code inside them. This is a new and exciting way that scientists can share their analysis in a truly transparent and reproducible way.

The two main parts of this lesson are exercises in interactive Jupyter notebooks. The first part is a quick tutorial on Jupyter notebooks and how to use them. Feel free to play around until you are comfortable. 

[Part 1: Jupyter Tutorial](https://mybinder.org/v2/gh/cjtu/sci_coding/master?filepath=lessons%2Flesson2%2Fdata%2Fjupyter_tutorial.ipynb)

The second part of this lesson is practice with some basic Python. You are given several functions in a Jupyter notebook that deal with **strings**, **booleans**, and **if statements**. You will need to fix and run the code in the notebook until the functions work as intended.

[Part 2: Python Practice](https://mybinder.org/v2/gh/cjtu/sci_coding/master?filepath=lessons%2Flesson2%2Fdata%2Flesson2.ipynb)

The rest of this document involves getting Jupyter running locally and also remotely via ssh. Some of the configuration details are a little technical, but hopefully once you have it set up, you will be able to create, edit, and interact with Jupyter notebooks to start making reproducible scientific code.


## Starting a local Jupyter server
Websites like mybinder.org are great for sharing Jupyter notebooks online, but they are limited by the resources the website will allow you. Luckily, Jupyter comes with an easy way to start a **local server**, so that you can quickly create and test your notebooks on your computer.

### Starting Jupyter locally (no ssh)
Jupyter is installed by default with Anaconda. On any Linux or Mac computer with Anaconda installed, you can type `jupyter notebook` into the shell and wait for it to start running. Your shell should print out info as it configures the local server. When it is ready, you should see a line with a url starting with `http://localhost`. This means that your local server is running, and you can access it by navigating to that link in a web browser (the Jupyter team recommends *Mozilla Firefox* or *Google Chrome*).
```bash
jupyter notebook
# A bunch of setup lines
[I 11:59:16.597 NotebookApp] The Jupyter Notebook is running at:
http://localhost:8888/?token=c8de56fa4deed24899803e93c227592aef6538f93025fe01
```

You should see a plain `Jupyter` splash page. If you do, great! Skip to [Navigating the Jupyter Server](#navigating-the-jupyter-server).

### Starting Jupyter remotely (with ssh)
If you are writing and running code on a remote computer (where Anaconda is installed), the steps above will still work as long as you use the graphical flag `ssh -X` or `ssh -Y` when you connect to the remote machine. The problem you would have is the web browser that opens will be very slow to type in because it needs to send a picture of the whole screen over the internet every time you type a character.

What we want is to start the Jupyter server on the remote machine (so we can edit and run our code there), but to see the server with a web browser on our local computer. This part is a little technical, but at the end of it you will have two simple scripts that:

1) Start the Jupyter server on the remote computer

2) Connect a local *port* on your computer to the remote server so that you can see the Jupyter server in a web browser on your local computer.

#### Starting Jupyter (on the remote computer)
First access your remote computer with **ssh**.

Next, we need to start Jupyter on the remote server with the `Jupyter notebook` command with two extra flags. The `--no-browser` flag stops Jupyter from trying to open a browser on the remote machine, while the `--port` flag starts the server on a specific **port**. 

On the **remote computer**:
```bash
jupyter notebook --no-browser --port=8080
```

**Note**: Leave this shell running! if you close this shell, it will kill the Jupyter server.

#### Connecting to Jupyter (from the local computer)

##### On Linux/Mac:
We will use a second **ssh** to our remote computer to connect a local port to the port we started Jupyter on above. This is called **port forwarding**.
Open a **new** shell/terminal on our **local computer**. 

In a **new shell** on your **local computer**:
```bash
ssh -v -N -L 8080:localhost:8080 <YOUR_SSH_USER>@<REMOTE_HOST>
```

This works the same as your regular ssh and you will need to log in. Once you have, your local port 8080 should be *forwarded* to the remote computer's port 8080. Now you can open a browser and navigate to `localhost:8080` and you should see the `Jupyter` server running on the remote machine.

##### On Windows
If on Windows, you have a couple options for connecting to your remote Jupyter server. 

Using the Windows Subsystem for Linux, the above commands for Linux/Mac should work in your Windows bash shell.

Using PuTTY, we will need to configure port-forwarding before we remote login to the remote server. Assuming you are comfortable with PuTTY and can ssh into the remote machine, below are the additional steps you will need to take:

1) Open PuTTY Settings / Configuration

2) On the left menu, go to **SSH** then **Tunnels**

3) Enter 8080 as your **Source port**

4) Enter 127.0.0.1:8080 as your **Destination**

5) Click **Add**, then **Open** your connection to the remote machine.

Now on the remote machine, start the Jupyter server as above. Finally, you should be able to open Chrome or Firefox on Windows, head to `localhost:8080` and see the remote `Jupyter` server.

If you're having trouble finding the settings, there are pictures and a guide on port forwarding with PuTTY [here](https://www.linode.com/docs/networking/ssh/ssh-connections-using-putty-on-windows/#port-forwarding-ssh-tunnels-with-putty).

### Creating scripts to simplify the above
The above two commands would be a pain to run every time we want to open a Jupyter notebook. Luckily we know from previous lessons how to simplify our lives by making executable bash scripts!

#### startjupyter script (to start Jupyter remotely)
Ssh to your **remote machine**.

Create a directory in your home directory called `bin/`. The **bin** or *binaries* directory is where executable scripts on your computer are saved. We will reserve this `home/bin/` directory to store our own user defined scripts (to keep them separate from operating system scripts).
```bash
mkdir ~/bin
```

Create a file in the  `~/bin` directory called `startjupyter`. Copy the command we used to start the notebook server into the file. Don't forget the shebang (`#!/bin/bash`)!
```bash
#!/bin/bash
jupyter notebook --no-browser --port=8080
```

Make the `startjupyter` script executable with `chmod u+x`.
```bash
chmod u+x ~/bin/startjupyter
```

Add the `~/bin` directory to your `PATH` by adding the following to your `.bash_profile`.
```bash
# Added path to my scripts to system PATH
export PATH=$PATH:/home/<your_username>/bin
```

Source your `.bash_profile` so that the change takes effect.
```bash
source ~/.bash_profile
```

Now you can start a Jupyter server from anywhere on your remote machine by typing `startjupyter`.

#### Mac/Linux: connectjupyter script (to connect local port to remote Jupyter server)
Open a new shell/Terminal on your **local computer**.

Create a directory in your home directory called `bin/`. Again, this is where you can store your local shell scripts.
```bash
mkdir ~/bin
```

Create a file in the  `~/bin` directory called `connectjupyter`. This time we will make a slightly more general script. Copy the following into `connectjupyter`. Make sure to replace `<YOUR_SSH_ID>@<REMOTE_HOST>` with your personal ssh info.
```bash
#!/bin/bash
remoteport=${1:-8080}
localport=${2:-8080}
ssh -v -N -L ${localport}:localhost:${remoteport} <YOUR_SSH_ID>@<REMOTE_HOST>
```

Make `connectjupyter` executable with `chmod +x`.
```bash
chmod +x ~/bin/connectjupyter
```

Add the `~/bin` directory to your `PATH` by adding the following to your `.bashrc` (Linux) or your `.bash_profile` (Mac).
```bash
# Addded path to my scripts to system PATH
export PATH=$PATH:/home/<your_username>/bin
```

Source your `.bashrc` (Linux) or your `.bash_profile` (Mac) so that the change takes effect.
```bash
source ~/.bashrc # or ~/.bash_profile
```

Now you can connect to your remote Jupyter environment from your local shell/Terminal with the `connectjupyter` command! Make sure to run `startjupyter` on the remote machine first!

**Note on ports**: `connectjupyter` will default to connecting the local port 8080 to the remote port 8080. Make sure when you run `startjupyter` on your remote machine that it is directing you to `localhost:8080`. If for some reason this port was taken, your server will be opened on the next available port and you will see something like:
```bash
startjupyter
# A bunch of setup lines
[I 11:59:16.597 NotebookApp] The Jupyter Notebook is running at:
http://localhost:8081/?token=c8de56fa4deed24899803e93c227592aef6538f93025fe01
```

If this is the case, you need to direct your local port to the remote port `8081`. You can specify a remote port in the `connectjupyter` script by adding it as the first option (e.g. `connectjupyter 8081`). Then when you go to `localhost:8080` on your local machine, you will be able to see the Jupyter server.

If you prefer to make both ports the same for simplicity, you can also use the second option to `connect jupyter`, (e.g. `connectjupyter 8081 8081`). Now you need to go to `localhost:8081` to see the remote Jupyter server.

#### Windows
On Windows, your PuTTY tunneling configuration should be saved and will execute each time, no need for a `connectjupyter` script. One hiccup is if you are sharing a machine among several people who may be opening servers on ports, you may not be guaranteed `8080`. In this case, I suggest picking a new port number somewhere in the range of `8070-8079` that nobody else uses. You will need to update your `startjupyter` script to open on your chosen port `--port=807X`, and then update your `Destination=127.0.0.1:807X` accordingly in PuTTY.


## Navigating the Jupyter Server
Now that you were able to start the local Jupyter server, you can start creating and editing Jupyter notebooks! If the splash page prompts you to log in, return to the shell where you started the server and find the `token`, a random string of characters after `?token=`. Copy and paste this into the password field.

Now you should see the directory where you started the notebook. From here you can navigate your file-system. When you are in the folder you want, you can click `New -> Python 3` to start a new Jupyter notebook. You can also click on an `.ipynb` file to open it for editing.

You can stop a Jupyter server at any time by returning to the shell where it is running and typing `ctrl+c`. Make sure to save your work first!

## That's it!
Once you have completed the two Jupyter tutorials and got a Jupyter server running, you are finished for today! The Jupyter server configuration can be a bit tough, if you need a hand please let me know!

Next class, we will be learning how to work with lists and dictionaries as well as how to write functions.
