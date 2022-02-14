#!/bin/bash

file=$1
if [ -f "$file" ]; then
echo "File EXISTs"
else
echo "does no EXISTs"
fi