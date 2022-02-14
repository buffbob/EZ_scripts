#! /usr/bin/env python3

import argparse
import sys
import os
import subprocess

# a program to test the abilities to init the location for
# base file for the password manager cli app in this directory


print("dude")
# os.environ["DEB"] = "FREd"
# print(os.environ.get("DEB"))

parser = argparse.ArgumentParser()
parser.add_argument("--init",  help="set a hidden path")
args = parser.parse_args()

if args.init:
    file_location = args.init
    dir1_path = "./venv/bin/dude"
    dir2_path = "/bin"

    if not(os.path.isdir(dir1_path)):
        process = subprocess.Popen(['mkdir', dir1_path])

    file = "secret.txt"
    file1_path = f"{dir1_path}/{file}"
    file2_path = f"{dir2_path}/{file_location}"
    process = subprocess.Popen(['sudo', 'touch', file1_path])
    with open(file1_path, "w") as f:
        f.write(file_location) # this file will be in /bin/
    process = subprocess.Popen(['touch', file2_path])
else:
    print("not")
