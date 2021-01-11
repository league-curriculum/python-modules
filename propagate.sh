#!/bin/sh
#Log
MODULES="/home/ec2-user/python-module-updater-DO_NOT_MOVE/python-modules"
destination="/home/ec2-user/python-module-updater-DO_NOT_MOVE/destination"
cd ${MODULES}
git clean -fd
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>log.out 2>&1
#================================================================
# HEADER
#================================================================
#% DESCRIPTION
#%    This script will pull down any changes from a repo
#%    and progpogate the changes to children repositories.
#%
#% EXAMPLES
#%    ${SCRIPT_NAME} -o DEFAULT arg1 arg2
#================================================================
#- IMPLEMENTATION
#-    version         ${SCRIPT_NAME} 0.0.1
#-    author          Keith Groves
#-    copyright       Copyright (c) The League of Amazing Programmers
#-    script_id       100001
#================================================================
#TODO change to relative path.
date
echo "pulling changes"
git pull

while read in; do 
    if ! git clone "$in" ; then
        echo >&2 this failed
    else
        echo "copy repo over"
        repoName=$(basename "$in" ".${in##*.}")
        echo ${repoName}
        cp -rf "${repoName}" "${destination}/java-modules/"
        rm -rf ./*/.git
        echo "do stuff"
        git add ${repoName}
        git commit -m "add ${repoName}"
        echo "push repo"
        git push
    fi;
done < RepoList.txt





echo "syncing folders"
rsync -av --exclude='.git/' --delete "${MODULES}" "${destination}" 

cd "${destination}/java-modules"
#Save current directory so we can restore it later
cur=$PWD
#Save command line arguments so functions can access it
args=("$@")

#changes color
cecho(){
    RED="\033[0;31m"
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    # ... ADD MORE COLORS
    NC='\033[0m' # No Color

    printf "${!1}${2} ${NC}\n"
}
#function is executed in each sub directory
#To access command line arguments use syntax ${args[1]} etc
function dir_command {
    #This example command implements doing git status for folder
    cd $1
    if [ "${args[0]}" == "gitignore" ]
    then
    cecho "GREEN" "creating gitignore in $1"
    curl https://gitignore.io/api/java -o .gitignore
    fi
    pwd
    echo $1
    git status
    git add .
    cecho "GREEN" "commiting changes"
    git commit -m "update from league central"
    cecho "GREEN" "pushing changes"
    git push
    cd ..
}
echo "moving through directories"
#This loop will go to each immediate child and execute dir_command
#find . -maxdepth 1 -type d \( ! -name . \) -name 'Level[0-9]*' | while read dir; do
#   dir_command "$dir/"
#   
#done

while read in; do 
        echo "copy repo over"
        repoName=$(basename "$in" ".${in##*.}")
        echo ${repoName}
        dir_command "${repoName}/"
done < RepoList.txt

#Restore the folder
cd "$cur"

git push
