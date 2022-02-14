#!/bin/bash

# append 2nd file to 1st file
echo "Before appending"
file1=$1
file2=$2

while read line; do
echo $line >> $file1
done < $file2