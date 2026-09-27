# Module 1 — Git & GitHub

**Student:** Viar, Paolaine Esther M.
**Date:** 09/27/2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is a tool that automatically record your projects. It uses different commands. These commands allow you to save a snapshot of your progress to avoid duplicate files. It is also a version control, meaning you can look back to your yesterday’s work or past work to see your mistakes and updates in your project. 

The difference between the Git and Github, Git is like a camera that takes a photo or screenshot of your work. It also run locally in your computer. While Github is a platform that allows you to collaborate with your friends, workmate, and team. This also run in a web-based where you upload your Git history.

---

## Key vocabulary (in your own words)

- repository: The main project folder that contains all the code files and the full history of every change ever made to them.
- commit: A saved snapshot of our project's files. Every commit comes with a description message explaining what changes have done.
- branch: It is a different workspace from the main branch. This allows us to work in a collaborative manner.
- push / pull:
Push: Sending/uploading your local commits from your computer to a remote repository on GitHub.
Pull: Downloading the latest changes from the remote GitHub repository to your local computer.
- pull request: A request on GitHub asking the repository maintainers to review and merge your branch's changes into the main branch.
- merge conflict: An issue that occurs when two people edit the same line of code in the same file differently, requiring a manual decision on which change to keep before merging

---

## Walking through what I did

I started by linking my local project to my GitHub repository and checking if the remote was connected properly. After that, I checked the branches and created a separate branch where I could work on my changes. Once I finished my files, I added and committed the changes, then pushed the branch to GitHub. I then created a pull request on GitHub to submit the changes.

git remote add origin "url of repo" 
git remote -v git branch 
git switch -c paopao 
git push -u origin paopao 
git add . 
git commit -m "message" 
git push

---

## A mistake I made (or one I want to avoid)

[What tripped you up? A confusing error message, committing to the wrong branch, a merge conflict — explain it so a classmate reading this avoids the same mistake.]

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
