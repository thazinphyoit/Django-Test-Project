DJANGO & MONGODB
****************
****************
- create(add) data to database using separate python code
- add form create and show form data in another page (no database using)
- read data from database



ENVIRONMENT
############

virtual environment 
-------------------
1. workon DjangoTestVM



GIT PUSH
#########

git (Create Git Repository)
----
1. create git account - https://github.com/
2. create git access token - Settings -> Developer settings -> Personal access tokens ->
                            Tokens (classic) -> Generate new token (classic)
3. create repository (public)


local computer (Add Project to Git Repository)
--------------
1. go to project root folder
2. git init 
3. git status
4. git add .
5. git status 
6. git commit -m "first commit"
7. git branch -M main
8. git remote add origin https://github.com/thazinphyoit/test-repo.git
    *** notice -> https://github.com/<GITHUB_USERNAME>/<REPOSITORY_NAME>.git 
9. git push -u origin main
    (or)
   git push https://thazinphyoit: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@github.com/thazinphyoit/test-repo.git 
    *** notice https://<GITHUB_USERNAME>:<Personal Access Token>@github.com/thazinphyoit/test-repo.git 



GIT CLONE (DOWNLOAD)
##########

local computer (Download Project from Git Repository)
--------------
1. git clone https://github.com/thazinphyoit/test-repo.git
