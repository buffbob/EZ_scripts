#!/bin/bash

# my first useful command line program in bash
# keeps all pws in file denoted below
# allows the adding of pw info
# allows the searching for pw info


Help()
{
  #Display Help
  echo "A password manager"
  echo
  echo "Syntax: pw [-v|h|i]"
  echo "options:"
  echo "  v   Print software version"
  echo "  h   Print this Help"
  echo "  i   Case-Insensitive Search"
}

########################
# Version
########################
Version()
{
  #Display version information
  echo "Version 1.0.0.beta"
}


#############
# Main Program
#############
file=/bin/pw.pw
res=""

while getopts "hiv" option; do
    case ${option} in
        h) # display Help
           Help
           exit;;
        v) # display Version
           Version
           exit;;
        i) # Case Insensitive Search
           sn=$2
           res=`grep -i $sn $file`
           echo "___________results___________" 
           echo "$res"
           echo "_____________________________"
           exit;; 
       \?) # Invalid option
           echo "Error: Invalid option!"
           exit;;
    esac
done
echo "$res"


if [ $# -eq 1 ] 
then
  sn=$1
  # search
  res=`grep $sn $file`
  echo "___________results___________" 
  echo "$res"
  echo "_____________________________"
  exit 0
fi

if [ $# -eq 3 ]
then
  sn=$1
  un=$2
  pw=$3
  res="$sn:$un:$pw"
  if [ -f $file ] 
    then
    echo $res | tee -a $file
    echo added
    else
    # make a new file and add
    # is order logical
    `touch /bin/pw.pw`
    echo $res | tee -a $file
    echo "shit it"
  fi
fi
