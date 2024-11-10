# Introduction To GitHub

## What is Git?
- Git is a version control system that runs locally on your computer.
- It allows you to track changes to your code, create snapshots of your project at different points in time, and manage branches for different versions or features of your project.
- Offline and Local: Git doesn’t require an internet connection and works independently of any online services. You can commit, branch, and revert changes entirely on your local machine.
- Command-Line Tool: Git is primarily used through the command line, though there are GUI tools that simplify its use.

## What is GitHub?
- GitHub is a cloud-based platform for hosting Git repositories.
- It provides a remote place to store your code online so that it’s accessible from anywhere and by anyone (if you choose to make it public).
- Collaboration Features: GitHub includes additional tools for collaboration, such as pull requests, issues, code reviews, and project boards. These features make it easier for teams to work together on codebases.
- GitHub Account Needed: To access GitHub’s features, you create an account and can then create, share, and contribute to repositories stored on GitHub.

## Downloading Git
To be able to use Git on your machine you will need to install it onto laptop/desktop using the following methods:

### Windows
You can install Git for your Windows machine using the [installer](https://gitforwindows.org/). 
You will just need to download the installer and follow the instructions; once successfully downloaded you can check 
the version of your Git in your terminal by running:
```
git --version
```

### MacOS
If you have **Homebrew** insatlled you can install Git with the following commad:
```
brew insatll git
```

Or you can download Git from [https://git-scm.com/downloads/mac](https://git-scm.com/downloads/mac) and run the insatller.
Once its downloaded successfully, you can check the version:
```
git --version
```
### Linux
If you have a **Debian/Ubuntu** operating system, you can install Git using the following commands:
```
sudo apt update
sudo apt install git
```

If your operating system is **Fedora** you can install Git using the commands below:
```
sudo dnf install git
```

Once installed, you can check the version of your Git by running the command below:
```
git --version
```

## Create An Account
Navigate to [GitHub](https://github.com/) website to create an account. You will need to sign up with your email and a password tro craete an account.
You will also need to create a **Profile Username** which will be linked to your account.  This will enable you to share your repositories, 
projects, code etc with others and across any multiple devices you may have.

## What is a repository?
A repository **(often called a repo)** is a space where you store and manage all the files, folders, and documentation related to a 
project on GitHub or another version control platform. It’s essentially a project folder, but with some added features specifically 
for coding and collaboration.

### Files & Folders
- You can keep all your project files here: code files, images, documents, etc.
- This organization makes it easy to access and update your work in one place.

### Version Control
- A repository tracks every change you make to files over time.
- You can view, revert, or compare versions, making it easier to manage and track the history of your project.

### Branches
- You can create branches within a repository, which are separate lines of development.
- Branches allow you to work on different features or fixes without affecting the main project files until you’re ready to merge them.

### Collaboration
- Repositories are central to collaboration on platforms like GitHub.
- Multiple people can work on the same project, suggest changes, review each other’s code, and contribute without overwriting each other's work.

### Documentation
- Repositories usually have a `README` file, which describes the project, instructions, and anything a contributor or user needs to know.
- Additional documentation, like contributing guidelines or code of conduct, can also be included.

## Why Use a Repository?
Repositories make it easier to:

- Keep your code organized and accessible.
- Track changes and understand the evolution of your project.
- Work with others by sharing code and merging changes seamlessly.
- Experiment with new features in branches without disrupting the main project.

In short, a repository is like a “home” for your project on GitHub, where everything related to your project is organized, versioned, and accessible for you or collaborators to work on!

## GitHub Commands and How To Use Them
Here’s a list of basic Git and GitHub commands to help you manage repositories. These commands are usually typed in a terminal or command-line interface, such as Git Bash or Terminal:

`git init`
- Initializes a new Git repository in your project folder.
- Run this command in a folder to make it a Git repository, enabling version control for that project.
```
git init
```

`git clone`
- Copies an existing repository (usually from GitHub) to your local machine.
- This downloads all files, commits, and branches from the specified GitHub repository.
```
git clone https://github.com/user/repository.git
```

`git status` 
- Shows the current status of your files in the repository.
- This command tells you if there are any modified, untracked, or staged files in your project.
```
git status
```

`git add`
- Stages changes (modified files) to prepare them for a commit.
- Adding files stages them for commit, meaning you’re telling Git you want these changes saved.
```
git add file1.txt
git add .
```

`git commit`
- Saves the staged changes to the repository history with a message describing the changes.
- This creates a snapshot of your project at its current state. The message helps you track what changes were made.
```
git commit -m "Initial commit"
```

`git push`
- Uploads your commits from your local repository to a remote repository, like GitHub.
- Pushing syncs your changes on GitHub so they’re available for others or for your future access from anywhere.
```
git push origin main
```

`git pull`
- Fetches and merges changes from the remote repository to your local repository.
- This updates your local files with any new changes from GitHub, keeping your repository up-to-date.
```
git pull origin main
```

`git branch`
- Lists branches, creates a new branch, or deletes a branch.
- Branches allow you to work on features separately from the main project until they’re ready to be merged.
```
git branch new-branch           # create new branch
git branch -d old-branch        # delete branch
git checkout branch-name        # switch to other branch
git checkout -b branch-name     # create new branch and switch to it
```

`git merge`
- Combines changes from one branch into another.
- Merging applies changes from a different branch into your current branch, allowing you to combine completed features or updates.
```
git merge feature-branch
```

`git remote`
- loads changes from the remote repository without merging them.
- Fetching retrieves changes from GitHub without merging them, allowing you to review before merging.
```
git remote add origin https://github.com/user/repository.git
git remote -v
```

`git fetch`
- Downloads changes from the remote repository without merging them.
- Fetching retrieves changes from GitHub without merging them, allowing you to review before merging.
```
git fetch origin
```

You can find [more commands here](https://github.com/joshnh/Git-Commands) for an in depth analysis.


## Cloning Your First Repo!
This will be a quick example on how to clone an exsiting repository onto your machine.  We will clone a **Dino Run** game, which will run locally on your machine.
```
# create empty folder/directory
new-item dino-run -type directory           # Windows
mkdir dino-run                              # MacOS / Linux


# clone the repo
https://github.com/CrapTheCoder/PynoRunner.git


# create Python virtual environment
python -m venv venv


# Activate Python virtual environment
venv\Script\activate                                # Windows
source venv/bin/activate                            # MacOS / Linux


# Install required libraries
pip insatll -r requirements.txt


# Run the app
python main.py

```