#!/bin/bash

# print names of files in a dir

dirName=$1 # Where to look

for file in `ls $dirName` ;
do
  echo $file
done