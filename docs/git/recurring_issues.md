There are the most common problems you may face when dealing with git.
1. No git configuration setup:
   Use the classic:
   ```bash
   git config --global user.name "Name Surname"
   git config --global user.email "example@mail.com"
   ```
2. You do not have the permissions to push to the repository:  
   This is usually solved by ensuring that ALL THE MEMBERS are registered as at least
   `Mantainers` role on your repository.  
   On the project page, on the left bar, click `Members` -> `Invite members` (blue button on top right)
   The `Invite members button appears only for the owner/mantainer of the project.
3. You cannot push your code since the remote version is some commits ahead:
   This can be fixed by doing in order commit -> pull -> push
   ```bash
   git commit -m "Local version"
   git pull
   git push
   ```
   and eventually merge conflicts that arise.
4. Merge conflicts
   To show what are the problematic files, use:
   ```bash
   git status
   ```
   Then fix the code until the files are in good shape. 
   Look for lines that look like `HEAD...` and `=========`
5. `gricad-gitlab` will deny pushing large files.
   For large files, students have to download `git-lfs`, available at:
   <https://git-lfs.com/>
   Once installed check the version:
   ```bash
   git-lfs --version
   ```
   then check which are the extensions of the large files and track them, e.g. for `tif` files:
   ```bash
   git-lfs track *.tif
   ```
   You my need to undo the last commit in these cases:
   ```bash
   git reset HEAD~1
   ```

