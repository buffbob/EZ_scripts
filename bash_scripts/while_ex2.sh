#!/bin/bash
# init counter
n=1
# 5 iterations
while [ $n -le 5 ]
do
echo "running $n times"
(( n++ ))
done