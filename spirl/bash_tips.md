# Extra tips and tricks

Here are a collection of other topics in bash that are useful.

## Cheat sheet

See this [cheat sheet](https://www.cheatography.com/gregcheater/cheat-sheets/bash/) for a summary of useful commands, options, and other cool things you can do in bash.

## Tab is king

Bash has a built-in completion feature which can be easily accessed with the `Tab` key. When writing a long file path, it can be convenient to type a few characters and press `Tab`. If you wrote enough characters to give you a unique path, it will fill in the characters for you. If not, you can hit `Tab` twice to see all of paths that do match.

Try typing the following, but only type `cd /home/` and then the first couple letters of your username then press `Tab`:

```bash
cd /home/<user>
```

I recommend practicing using `Tab` anytime you are navigating the shell or typing in paths. It can make getting around a lot easier.

## Aliases

An alias is a helpful way to make a shortcut for a command we want to use in bash.

Say you want a shortcut to your `~/Documents` directory. We could define an alias like so:

```bash
alias cdd='cd ~/Documents'
```

Now if you type `cdd`, you should find yourself in the Documents directory.

```bash
cdd
pwd
```

Any alias or variable you set in a shell are particular to that shell windows that is open. If you open a new shell and try to use the `cdd` alias, it will not know that you've defined it here. To keep these aliases, we can make a **profile** for our bash shell.

## Profiles

Go to your home directory if you are not already there.

```bash
cd ~
```

Now list the files, but add the `-a` option, which lists all *hidden files*, sometimes called *dotfiles* because they begin with a `.`.

```bash
ls -a
```

My home directory has a `.bashrc` and a `.bash_profile` in it (it is ok if you do not have these, especially on a new system). Profiles special bash scripts that are located in your home directory and are run every time you start up a shell.

On Linux:

- The commands in the `.bashrc` are run every time you start a new shell locally (i.e. on your computer).

- The `.bash_profile` commands are run every time you start a remote bash shell (i.e. one that you ssh to).

On MacOS:

- The `.profile` (or `.bash_profile`) takes the role of `.bashrc` and is run every time you open a new terminal

It can be helpful to add helpful commands to your `.bash_rc` or `.profile`. For instance if we add the alias `alias cdd='cd ~/Documents'` to the `.bashrc` (or `.profile` if you are using a Mac), then the `cdd` alias will be available for every new shell we open. Try it out!

## Editing files

Interactive editing of files is a contentious topic and programmers and scientists alike are known to go to battle over their favored command line file editors.

We won't advocate for one specific tool here, all have strengths and weaknesses. Generally the best one is the *one you can use*. So pick one, learn the basics, and it'll make your all of your future file-editing endeavors easier.

Some command-line editors you may have heard of are:

- [vi](https://www.guru99.com/the-vi-editor.html)
- [vim](https://www.linux.com/tutorials/vim-101-beginners-guide-vim/), the upgraded version of vi
- [emacs](https://www.gnu.org/software/emacs/)
- [nano](https://www.tecmint.com/learn-nano-text-editor-in-linux/)
- [gedit](https://www.lifewire.com/gedit-linux-command-unix-command-4097153)

Many basic shells (including the emulator suggested for this chapter) only come loaded with `vi`, so it can be a useful, although challenging, interface to learn. Before the next lecture, it would be useful to pick one, install it on your machine, and learn to open a file with it, edit and save the file, and then quit the editor (yes quitting is something you need to learn to do, especially in `vi`). The links above should be good starting points.
