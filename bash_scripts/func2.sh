#! /bin/bash
function areaRect(){
    #bash can't declare function parameter or arguements at the the time of 
    #function declaration. But you can use parameters in function by using 
    #other variable. If two values are passed at the time of function calling
    #then $1 and $2 are used for reading the values.
    area=$(($1 * $2))
    echo "Area = $area"
}

areaRect 10 20