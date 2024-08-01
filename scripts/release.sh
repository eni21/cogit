#!/bin/bash

set -e

cogit=dist/cogit.exe

function step {
    LIGHT_BLUE='\033[1;34m'
    NC='\033[0m'
    echo -e "$LIGHT_BLUE### $1 ###$NC"
}

function error {
    RED='\033[0;31m'
    NC='\033[0m'
    ERROR='ERROR'
    echo -e "\n$RED$ERROR: $1$NC\n"
}

# step "Check repository"
# if git status | grep -q 'nothing to commit, working tree clean'
# then
#     echo 'Repository has not changes'
# else
#     error 'Repository has local changes, please commit changes and try again'
#     exit 1
# fi

step "Calculating version"
CURRENT_VERSION=$($cogit current-version)
NEXT_VERSION=$($cogit next-version)
echo "CURRENT_VERSION=$CURRENT_VERSION"
echo "NEXT_VERSION=$NEXT_VERSION"
if [ $CURRENT_VERSION == $NEXT_VERSION ]
then
    error 'Can not generate new version'
    exit 1
fi

step "Switch to main"
git checkout main

step "Pull"
git pull origin $(git rev-parse --abbrev-ref HEAD)

step "Bump version"
$cogit bump $NEXT_VERSION

# step "Add changes"
# git add --all

# step "Commit"
# git commit --step "Bump version to $NEXT_VERSION"

# step "Add tag"
# git tag $NEXT_VERSION

# step "Push changes"
# git push origin $(git rev-parse --abbrev-ref HEAD)

# step "Push tags"
# git push origin $NEXT_VERSION


# git flow release start $VERSION
# git flow release finish -m "version: $VERSION" $VERSION
# git checkout dev
# git push origin $(git rev-parse --abbrev-ref HEAD)
# git checkout master
# git push origin $(git rev-parse --abbrev-ref HEAD)
# git push origin $VERSION
# git checkout dev