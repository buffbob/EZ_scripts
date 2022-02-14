#! /bin/bash

[ 5 -eq 10 ] && echo true || echo false

[ 5 -le 10  ] && echo true || echo false

file1=$1
echo $file1

## echo will not produce output if .....?
[ -e $file1 ] && echo $?
echo -----------------------
[ -d $file1 ] && echo true || echo false
