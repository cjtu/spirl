# Comments in Python Code
 
## Why are good comments crucial?

### They make your life easier
 
Suppose you write a program- it reduces data exactly how you need it to, you have your result, but you haven't put a single comment in the code. It seems you're in the clear. But then, a year later, you need to do exaclty the same thing just with a few upgrades. That's easy! You can just use the code you have already written and add a few extra steps. Except you've entirely forgotten how the code works. It takes hours to parse through your code, but it's a mess. You must have been rushed when you'd written it - the variable names don't make any sense, there are no functions and pieces of code have been copy and pasted, and worst of all there's no comments to help you sort the mess out. Having good comments will allow you to look through your code and understand what is happening in a matter of minutes - much less than the hours you might spend trying to figure out what is happening without them. 
 
##### They make other's lives easier

When using someone else's code you want things to be as easy as possible - to understand how the code works and how to use it without having to parse through each and every line of code. Good comments allow you to do this. Aside from making your life easier, commenting your code allow you to share it with other and let them quickly get started using it.
 
## Python Commenting Basics

A comment in Python is ignored by the compiler - you can put whatever you want in a comment and it will be ignored when the code is actually run.

```bash
# Single line comments use the pound symbol
```

You can comment after a line of code

```bash
print ('Hello World') # Everything after the pound is ignored
```

Keep comments short and to the point - this makes them more readable. When following PEP 8, there is a 79 character (per line) cutoff, however for inline comments it is suggested at 72.
If your comment is longer than this, you can make it multiple lines. To do this, you just need to add a '#' to each line

```bash
# I have a long comment
# So I've made it multiple lines
    # You can even indent to make things more clear
```

## Tips for Writing Good Comments

Comments are a good tool to use while developing code, or when writing reusable functions to specify what the expected inputs and outputs should be. They can help you keep track of things even during the development process.

**Here are a few good ways to use comments:**

- Sketch out your code in comments before you start. This can help you figure out the high level flow of the code before you get bogged down in too many details.
- Use comments for debugging. When making changes, comment out the old code so that you can return to it if the new code doesn't fix the issue.
- Use comments to spell out what is happening for any tricky parts of your code. You'll thank yourself later.
- Separate major sections of your code using comments to keep track of the organization.
- If anything complicated is happening (ie: a function who's name doesn't do a great job of expalining what it does), add a comment with this info.


**Things to avoid when writing comments:**

- Avoid WET comments - that is commenting exaclty what the code itself already says. These types of comments are not useful and break the DRY (Do not repeat yourself) rule.

```bash
print(x) #prints x
```

-Don't over comment either. While this is typically less of an issue than undercommenting, you don't need a comment for every line of code. If it is clear what a line does (ie: a print statement), then it doesn't need a comment. Comments should make things more clear, otherwise they serve no purpose.
