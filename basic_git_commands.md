# Git Basics

## Setting up a Git Repository ...

1. Creating README.md file for github.
The README.md is special file which adds description to your git repo.

2. git init
This command initializes a git Repository. It Local in nature.

3. git add <file_path, multiple>
This command helps in addition of files into the git VCS.

4. git commit -m "<Commit_Message, String>"
This creates a Check Point.
__*Note:__ All the files added are placed into the same commit.

5. git branch -M <master|main|trunk|developement>
This is a one time command.
Defines the name of the master branch in the Repository.

6. git push -u origin master
Current commit is mushed to the master branch .
You Don't Generally mention the Branch name during Pushing of Code into Repo.
For the first commit to be pushed we need to determine the Branch it has to be pushed into.

## Types of Repositories ..

1. Public
This repository will store code that is accessible to all the users. Genererally shared for teaching purposes.

2. Private
This is a Repo with controlled access management. Users having access to such repos can only view or commit to the repository as per permission defined.
For defining permissions you use the collaboration present in the Git Settings.  
