#!/bin/bash

function greeting(){
    str="Hello, $name"
    echo $str
}

echo "Enter your name:"
read name

val=$(greeting)
echo "returned greeting - $val"