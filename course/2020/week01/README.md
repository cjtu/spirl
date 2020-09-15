# Class 1: Sep 11, 2020

In this lesson we will practice bash and Git by learning to contribute to the SPIRL textbook!

## Pre-class homework

SPIRL Chapter 1 (Bash) and Chapter 2: (Git) were assigned.

## Itinerary

**(5 mins)** Wait for people to join / Zoom poll:

1. Did you do the pre-class homework? A: Yes, B: Ch1 only, C: Ch2 only, D: No, I didn't know about it, E: No, I didn't get a chance
2. Had you used Bash before the homework? A: A little, B: A lot, C: Nope
3. Had you used Git before the homework? A: A little, B: A lot, C: Nope

**(15 minutes)** Live demo

Step through how to contribute to a GitHub repository in two ways! First:

- Find the 2020 class folder on the repo (if you're reading this, you found it!)
- Fork the repo

Method 1: Command line

First we set up the textbook locally (see instructions in [CONTRIBUTING.md](https://github.com/cjtu/spirl/blob/master/CONTRIBUTING.md)). Generally the first step of contributing to a repository is to read through the contributing guidelines and get a build set up on your computer. This way you can test your changes before contributing them to the repository.

- Clone the repo
- Create conda env
- Activate conda env
- Build the textbook locally
- Check out the local textbook in browser

Now we make our first contribution:

- Make a branch
- Add a file to the `spirl/course/2020/week01` folder called `myinitials.md`
- Commit file
- Push change to GitHub
- Make pull request on the main repository on GitHub

Part 2: GitHub Desktop

GitHub offers a graphical user interface (GUI) to help users contribute changes without ever having to use the command line. You may still need the command line to set up a build (as is the case for this example), but GitHub Desktop allows you to do everything from cloning the repository, branching, adding, committing and pushing it to GitHub - so all the Git stuff.

- Show how to use GitHub desktop to clone, branch, add, commit, and push a new file to GitHub
- Make a pull request with the commit we made with GitHub Desktop

**(25 minutes)** Breakout room practice

- Work through the above steps to get a clone of SPIRL on you computer, then make a pull request!
- Feel free to use the command line or try GitHub Desktop!
- Ask each other questions and make sure everyone is keeping up!
- Your goal is to make a pull request to add a new file, `myinitials.md`, to the main repository

**(15 minutes)** Debrief and Q&A

- How did it go?
- Did you use the command line or GitHub Desktop?
- What questions do you have about Git, Bash, misc?
- Would you feel comfortable using this for your own work? Why or why not?

## Minutes / Notes

Q: Do I need to build the SPIRL website to contribute the file on GitHub?
A: Technically, no. Once you fork a repository on GitHub and clone it to your local PC, you can make any changes you'd like, add and commit them, and push them back to your fork. At that point you can open a pull request - no local textbook build needed. The reason to make a local build is to **test your changes** before you contribute them. Many code repositories will have a set of tests that you will need to run locally before you open a pull request, ensuring that any new code that you write does not break any existing code. Making a local build of the SPIRL textbook is good practice for this process - and let's you preview the textbook on your own computer if you ever want to fix typos, make a tutorial, or contribute to it in some other way!

Q: Why do we need branches? Why do we need forks? Whats the difference?
A: The branch system is done in **Git**. It is used to separate changes you make to your files into their own self-contained units. Branches can help keep your code organized and allow you to have a main, always working version if you make sure to only develop new features / changes on dedicated branches. When the changes on those branches are ready, you can merge them into the main branch, but in the meantime you know the main branch works and can switch between them at any time.

Forks are a **GitHub** system which allows you to make your own copy of a GitHub repository that you can clone and contribute to at will. Since only the owner (and designated maintainers) can push directly to a GitHub repository, you would have no way to propose changes if you clone the main repository directly. By making a fork, you have a complete copy of the repository under your account which you can push to at will. When you think your changes are ready to be added to the main repository, you can push them to your fork and open a **pull request**, asking the main repository maintainers to bring in the changes from your fork. The maintainers can see all of the changes made since you forked the repository and get the final say on if your commit(s) are added to the main repository.
