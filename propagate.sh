#!/bin/sh
#%author: Colby Schexnayder

# This script makes the following assumptions:
#
# 1. The local files have not been changed from Central,
#   ANY CHANGES MUST BE COMMITTED AND PUSHED IMMEDIATELY
#
# 2. Once a Repository is added to the RepoList it will
#    only be updated by this script push changes
#    from central to the Repo
#############################################
#BEGIN SCRIPT


#Step 1: pull from Central
echo "Pulling from Central"
git pull

#Step 2: Search through RepoList
while read in; do
    repoName=$(basename "$in" ".${in##*.}")
    #If the Repo doesn't exist check github
    if [ ! -d "$repoName" ]
    then
	echo "$repoName is not in Central"
	echo "Checking github"
	git clone $in
#	git add ${repoName}
    else
	#If the repo does exist generate .git
	echo "$repoName exists"
	echo "Generating .git"
	cd $repoName
	git clone --no-checkout $in
	cd $repoName
	mv ./.git ..
	cd ..
	rm -rf $repoName
	echo "Updating $repoName from Central"
	git add -A
	git commit -m "Updated from Central"
	git push
	cd ..
    fi

    if [ -d "$repoName" ]
    then
	echo "Removing .git"
	cd $repoName
	rm -rf .git
	cd ..
    fi
done < RepoList.txt

#Step 3: Update Central
echo "Updating Central"
git add -A
git commit -m "Automatic Update"
git push
echo "Finished"
