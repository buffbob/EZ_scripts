#!/bin/bash

if [ $# -gt 0 ]; then
    filename=$1
    echo "Reading from $filename"
    echo ""
    while read line;
        do
            echo $line
    done < $filename
else
    echo "No filename given, please provide one."
fi