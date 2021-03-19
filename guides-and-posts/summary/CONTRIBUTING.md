# Contributing Guide

## How to Contribute
1. Fork this repo on your local machine.

    * Fork and clone this repo to your local machine, use [this guide](https://help.github.com/articles/fork-a-repo/) if you don't know how to do that
    * Set the upstream remote to keep your copy of the app synced with the original. To do that go to your terminal and `cd` into your cloned directory. Then use one of the following commands:

   If you have ssh set up with Git
   ```
   $ git remote add upstream git@github.com:barrysweeney/1-click-startup.git
   ```
   Otherwise
   ```
   $ git remote add upstream https://github.com/barrysweeney/1-click-startup.git
   ```

2. Before you start working on your issue create a branch and name it like the following examples:

   For a new feature
   ```
   $ git checkout -b feature/feature-name`
   ```
   For a bug fix
   ```
   $ git checkout -b fix/fixed-bug-name
   ```

3. When you have finished and are ready to submit a Pull request:

**Before you submit your pull request ensure your markdown is correctly formatted and rendering properly**

**Push your branch to your fork**
```
$ git push origin <your branch name here>
```
**Create a pull request**
* Go to your fork on Github after you have pushed up your branch. A new button should be visible near the top of the page. It will allow you to create a pull request to the original 1 Click Startup Repo.

* Please link to the issue your pull request resolves in the body of your pull request.

## References
This contribution guide is based on [this guide from The Odin Project](https://github.com/TheOdinProject/curriculum/blob/master/CONTRIBUTING.md)
