#!/bin/bash

# get a file if exists
ext=$1
if [ -f "$ext" ];
then
echo "File exists"
else
echo "No File by that name!!!"
fi
