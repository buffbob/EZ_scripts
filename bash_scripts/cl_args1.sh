#! /bin/bash

# Named command line args
while getopts n:a:e: OPT
do
    case "${OPT}"
    in
      n) name=${OPTARG};;
      a) address=${OPTARG};;
      e) email=${OPTARG};;
      *) echo "Invalid option"
        exit 1;;
    esac
done

printf "\nName:$name\nAddress:$address\nEmail:$email\n"

      