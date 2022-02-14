#!/bin/bash

# use of while and continue
counterMax=$1
counter=0
echo "$0"
while [ $counter -lt $counterMax ]
do
  if [ $counter -eq 3 ]
  then
  counter=$((counter+1))  
    continue
  fi
  echo "The counter is $counter"
  counter=$((counter+1))
done
printf "done"