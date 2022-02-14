#! /usr/bin/env python3

import argparse
import sys
import os
import subprocess

# a program to test the abilities to init the location for
# base file for the password manager cli app in this directory

dir1_path = "./venv/bin/dude"
dir2_path = "/bin"


def initialize(name):
    file_location = name
    file = "secret.txt"
    if not(os.path.isdir(dir1_path)):
        subprocess.Popen(["mkdir", dir1_path])

    file1_path = f"{dir1_path}/{file}"
    file2_path = f"{dir2_path}/{file_location}"
    subprocess.Popen(["touch", file1_path])
    with open(file1_path, "w") as f:
        f.write(file_location)
    subprocess.Popen(["touch", file2_path])


print("dude")

parser = argparse.ArgumentParser()
parser.add_argument("--init",  help="set a hidden path")
args = parser.parse_args()

if args.init:
    initialize(args.init)
