#!/bin/bash
valid=true
count=1

while [ true ];
do 
echo $count
if [ $count -eq 5 ];
then
break
fi 
((count++))
done
: 'syntax very impt in bash!!!!!'