# Instructions

This section covers all the procedure for managing your `git` project.
The instructions are very specific for the configuration that you will most
likely encounter on your machine in the laboratories of ENSE3.
Specifically, we assume:
- A Windows machine
- Python installed with at least a 3.9 version
- `C:` is your data drive

For the following operations we suggest to use a desktop computer from the 
university to make use of the fast speed connection.
Please operate exclusively on the C drive on Windows not to be limited in 
terms of data size. 

## Creating a new remote repository

- Login, using your Agalan credential on the Gitlab of Gricad:  
  <https://gricad-gitlab.univ-grenoble-alpes.fr/> 
- Click on "New project" and then on "Create blank project"
- Assign a name to your project in the text box, select "Public", unselect 
  "Add README.md" and finally click on "Create project".
- From now you have an assigned git repository with a name such as:
  ```
  https://gricad-gitlab.univ-grenoble-alpes.fr/username/project.git
  ```
  where `username` is your AGALAN username and `project` is the name that you 
  have assigned to your project.


## Initializing a repository

- Install **git for Windows** from <https://gitforwindows.org/>
- Install **git-lfs** from <https://git-lfs.com/> 
- Launch the git CLI (CLI stands for command line interface) from the utility 
  you have just installed. You will see a command terminal.
- From the command line interface, navigate to the root folder of your project:
  ``` 
  cd C:\pathtoproject        
  ```
- If you already have initialized a git project, and you want to delete the previous content type:
  ```bash
  rm -rf .git
  ``` 
- Initialize the project to connect to the remote git  
  ```bash
      git init
      git remote add origin https://gricad-gitlab.univ-grenoble-alpes.fr/username/project.git
      git branch -M main
  ```
  where `username` and `project` are the username and project name you have 
  previously assigned.

## First commit

First, we need to configure your identity on your machine:
```bash
  git config --global user.name "Your Name"
  git config --global user.email "you@grenoble-inp.fr"
```
where `Your Name` are your name and surname and `you@grenoble-inp.fr` is your 
institutional mail.

For a first commit, I suggest to create a `README.md` file to the root folder 
of your project and upload it remotely:  
```bash
    git add README.md
    git commit -m "Initial commit"
    git push origin main
```
It will ask you to type your Grenoble-INP username and password.
Verify that your readme file now shows on the Gricad page of your repository.

## Commits with data content

Identify what are all the extensions that are specific of those large files, 
such as `.pdf`, `.tif`, `.jpg`, etc.
You need to notify your repository that those files are large. For example for 
`tif` files type:  
```bash
    git-lfs track *.tif
    git-lfs track *.TIF
```
and repeat this operation for all extensions of files larger than 5MB.

In the second commit, I suggest to just add the code and the reports to the root folder of your project. If you have any data, please move it away to a temporary external folder outside of the root folder of your project.
Then type:  
```bash
    git status
```
to show all the files that you wanted to add to the online repository.
Then commit and pull once again:  
```bash
    git add .
    git commit -m "Intermediate commit"
    git push origin main
```

Finally, add your data back to the folder and try a final commit:  
```bash
    git add .
    git commit -m "Final commit"
    git push origin main
```

## Failed commits

In the case that Gitlab-Gricad does not allow you to push data, it is most 
ikely the case that you are not properly tracking all the data content that is 
bigger than 5 MB. In that case I suggest to restart from the operation of 
"initializing a repository" and try again, being very careful to track all the 
large files when you type `git-lfs track *.pdf`, etc.


# Legacy instructions

The following procedure describes the instructions to submit your project up to
the academic year 2023/2024. While those instructions do not concern you 
anymore, you may still find some interesting information to use.

## Instructions for the git repository

*git* is a platform form code control, which allows to:
- Track your code modifications
- Share your code online
- Synchronize your work across different people


## Getting started
- If under Windows, download `Git for Windows`, and launch `git bash`
- If under Linux/Mac, `git` is already installed by default on your kernel


## Managing permissions
- On the Gricad website, login and click on `Edit Profile` on the top right icon
- On the left menu, click on `Access Tokens` and generate a new one:
    - Give a token name (eg: `token_name`)
    - Check `api`
    - Select an expiration date (ending after the end of this project)
    - Finally, click on `Create personal access token`
- Copy the token (a 19-characters key) from the box somewhere safe
- This token will be called `token_key` in the rest of the document


## Forking the original project

- Login to your Gricad account
- Go to `https://gricad-gitlab.univ-grenoble-alpes.fr/dallamum/remote-sensing-projects`
- Fork your project on your private account (click on the button `Fork` on top right)

## Initialize the git repository

- Get your project URL:
    - The git project URL is an identifier of your project, with permission rights
    - On your forked project webpage, click on clone and copy the URL in `clone with HTTPS`
    - The project URL will be something like `https://gricad-gitlab.univ-grenoble-alpes.fr/username/remote-sensing-projects/`
    - Rewrite it as: `https://token_name:token_key@gricad-gitlab.univ-grenoble-alpes.fr/username/remote-sensing-projects/`
    - where:
        - `username` is your specific username in the forked project
        - `token_key` is the token obtained in the `Managing permissions`section
    - The obtained URL will be called from now on `project_uri`
- Go on your command line (git bash under Windows, shell under Linux)
- Go to the folder where you save your projects
- Type `git clone project_uri` to have the version of your forked project on your device


## Setting the original repository as upstream
- Add the original repository as remote source of your repository:
    - ```git remote add upstream https://token_name:token_key@kegricad-gitlab.univ-grenoble-alpes.fr/dallamum/remote-sensing-projects```
    - where `token_key` is the token obtained in the `Managing permissions` section


## Updating your forked repository

- Identify a single person on your group to take care of collecting and 
  updating the code to the repository. This will avoid conflicts between 
  different versions of the code
- Whenever the person in charge want to update your code from your local machine online:
  - `git pull origin master` to download the current version online
  - `git status` to show what files you have changed locally with respect to online
  - `git add .` to inform git that you want to track the new files you added
  - `git commit -m "Commentary"` to save your updates, where `"Commentary"` is a specific explanation on the changes
  - `git push origin main` to upload your changes to the forked repository

## At the end of your project

- In your terminal:
  - `git pull upstream master` to get the most up-to-date version of the central repository
- On the Gricad page of your forked repository:
  - Click on `Merge requests` on the menu on the left
  - For the source:
    - Select your own project and your currently active
  - For the destination:
    - Select `https://gricad-gitlab.univ-grenoble-alpes.fr/dallamum/remote-sensing-projects` 
    - Select the branch `main`
  - Click on `Send a merge request`
  - Once approved, your code will be uploaded on the central repository


