#!/bin/bash

# files in dir

searchDir=$1
cd "$1"
for [ z in `echo *` ]
do
  echo "$z"
done