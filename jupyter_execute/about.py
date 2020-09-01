# Scientific Programming IRL

Welcome to the **Scientific Programming In Real Life** textbook! 

This book explains practical programming concepts for scientists in a hurry.

## Getting started with SPIRL

This textbook can be used in a few ways:

- as a top-to-bottom interactive crash course in scientific programming ([start here](bash_about))
- as a reference for when you can't remember how to do that one thing (trying searching in the left pane)
- to make your own programming course (let me try to convince you to [contribute](https://github.com/cjtu/spirl/CONTRIBUTING.md) to this one instead!)

## Why another learn-to-code resource?

There are many free learn-to-code resources which are great but require 40+ hours to complete. On the other hand, quickly copy and pasting impenetrable code from StackOverflow can lead to confusion and the feeling that coding is some sort of arcane art.

This book was crafted **by scientists, for scientists** with 2 main philosophies:

- _scientists are_ **busy**
- _scientists like to_ **understand** _how things work_

These two philosophies help make this book as **concise** as it can be while giving just **enough depth** to understand why these concepts here are important and how they work.

It is also meant to be a resource that is easy to follow start-to-finish, but also quick to refer back to in a pinch.

## An interactive textbook

SPIRL is powered by [JupyterBook](https://github.com/jupyter/jupyter-book), a fantastic project which makes responsive online textbooks like this one, while allowing readers to execute code without leaving the site!

Don't believe me? Try cliking the rocket icon at the top and choosing the **Live Code** option. This is still an experimental feature so sometimes the kernel is slow to start... But now you should be able to run the cell below!


print("Hello World!")

Each tutorial in this book is intended to be hands-on. Learning scientific programming is like learning a language: you need to practice in order to become fluent! When you see code cells like these throughout the SPIRL text, try editing and running them to see what happens!

import random
def get_lucky(n): 
    return '-'.join([str(random.randint(1, 49)) for i in range(n)])

N = 8  # change me!
print('Your lucky numbers for today are:')
print(lucky)

## Fall 2020 Syllabus

This schedule is for those taking the SPIRL course at Northern Arizona University. It will be updated as the course progresses.

**Last edit: Sep 1, 2020**

| Week   | Date  | Topics | Pre-class homework |
| :--- | :------ | :----- | :----------------- |
| 1 | Sep 11 | Shell navigation, bash scripts | Ch. 1 ([link](bash_about)) |
| 2 | Sep 18 | Git & Version control | Ch. 2 ([link](git_about))|
| 3 | Sep 25 | Python basics & style (bool, int, float, str, list, tuple)  |  Ch. 3.1-3.3 ([link](python_about)) |
| 4 | Oct 2 | Methods, functions, conditionals, loops | Ch. 3.4-3.7 ([link](python_basic-types)) |
| 5 | Oct 9 | Set, dict, modules, numpy, matplotlib  | Ch. 3.8-4.3 ([link](python_adv-types))  |
| 6 | Oct 16 | scipy, pandas | Ch. 4.4-4.5 ([link](sp_about)) |
| 7 | Oct 23 | Managing environments, reproducibility | Ch. 5 ([link](anaconda_about)) |
| 8 | Oct 30 | Hacktoberfest! | Get a GitHub account and review Ch. 2 ([link](git_practice)) |


## Issues

Did you find a glaring typo? Is one of the links broken? Is the whole textbook _broken_?? It would be super helpful if you could report bugs, typos, or glitches over at the GitHub issues page [here](https://github.com/cjtu/spirl/issues). Thanks for helping make this textbook even more useful!

## Contributing

This book is a work in progress! Have ideas for new tutorials? Want to apply your copy-editing skills? Check out the contributing guide on GitHub [here](https://github.com/cjtu/spirl/blob/master/CONTRIBUTING.md). This textbook wouldn't be possible without help from its [contributors](https://github.com/cjtu/spirl/graphs/contributors)!

## Supporting SPIRL

SPIRL will always be **free** and **open source**. If you'd like to support it, consider *sharing SPIRL with friends or peers* who you think would find it useful. If you can spare the time, you can support this project by contributing (see above). If you *use any of the code or concepts in an article / lesson / publication* (please feel free to!), you can **cite SPIRL** [here](). If you'd like to support SPIRL by buying me a coffee, you can also do that [here](https://buymeacoff.ee/cjtu).



```{toctree}
:hidden:
:titlesonly:
:numbered: 

bash_about
git_about
python_about
sp_about
anaconda_about
```
