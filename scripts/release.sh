#!/bin/bash

set -e

function error {
    RED='\033[0;31m'
    NC='\033[0m'
    echo -e "\n$RED ERROR: $1$NC\n"
}

if git status | grep -q 'nothing to commit, working tree clean'
then
    echo 'Repository has not changes'
else
    error 'Repository has local changes, please commit changes and try again'
    exit 1
fi

CURRENT_VERSION=$(scripts/tools/cogit.exe current-version)
NEXT_VERSION=$(scripts/tools/cogit.exe next-version)
echo "CURRENT_VERSION=$CURRENT_VERSION NEXT_VERSION=$NEXT_VERSION"
if [ $CURRENT_VERSION == $NEXT_VERSION ]
then
    error 'Can not generate new version'
    exit 1
fi

