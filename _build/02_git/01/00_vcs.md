---
redirect_from:
  - "/02-git/01/00-vcs"
title: 'Version Control'
prev_page:
  url: /02_git/00_why-git.html
  title: 'Version Control in Git'
next_page:
  url: /02_git/01/01_git-overview.html
  title: 'Git overview'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Version Control Systems (VCS)

Version control systems (VCS) were developed to solve the challenges of collaborating on code with others, a common task in both industry and academia.

There are many version control systems that approach code collaboration slightly differently. Some VCS you may (or may not) have heard of are  [Subversion (SVN)](https://subversion.apache.org/), [Mercurial](https://www.mercurial-scm.org/) and [Git](https://git-scm.com/). 

In this book, we focus on Git because of it's recent rise in popularity with the advent of popular code-hosting websites like [GitHub](https://github.com), [GitLab](https://about.gitlab.com) and [BitBucket](https://bitbucket.org).

### I fly solo, why bother?

If you mostly work on your scientific code by yourself, you might wonder why you would ever need version control. Hopefully this chapter will convince you that version control has many benefits to your day-to-day work aside from sharing code.

Until then, here are some reasons you may want to use version control if you fly solo:

1. You always have time-stamped snapshots of your code that you can revert to if you accidentally break or delete something.

2. Version control makes it really easy to host a private backup of your code. Nobody wants to be the person that loses a whole paper or dissertation worth of work because of a faulty hard drive or spilled coffee...

3. You can easily keep your code up to date on multiple machines, say, if you have to run code on a cluster or in the cloud.

4. Free hosting sites (like GitHub) provide a well-established way to share your beautiful science analysis and/or code that won't fit in the footnotes of a paper.

Finally, you'll see how few steps it takes to post code to GitHub later in the chapter; if you get in the habit of using Git day-to-day, it'll be even simpler to share your science with the world when it's ready!
