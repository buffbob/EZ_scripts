#!/usr/bin/env python3

import argparse
import subprocess
import sys
import os

#############################################
# command line program for storing passwords
#############################################
# allows new installation
# allows viewing all pws
# allows searching (also case_insensitive search)
# allows adding new pw
#############################################


def initialize(name):
    file_location = name
    if not(os.path.isdir(dir1_path)):
        subprocess.Popen(["mkdir", dir1_path])

    file1_path = f"{dir1_path}/{file}"
    file2_path = f"{dir2_path}/{file_location}"
    subprocess.Popen(["touch", file1_path])
    with open(file1_path, "w") as f1:
        f1.write(file_location)
    subprocess.Popen(["touch", file2_path])
    sys.exit(0)


def add_info(aline):
    with open(write_location, "a") as file1:
        file1.write(aline)
        sys.exit(0)


def list_all():
    with open(write_location, "r") as fp:
        for aline in fp.readlines():
            print(aline)
    sys.exit(0)


def search_term_i(term):
    process = subprocess.Popen(['grep', '-i', term, write_location],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    return process.stdout.readlines()


def search_term(term):
    process = subprocess.Popen(['grep', term, write_location],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    return process.stdout.readlines()


dir1_path = "./venv/bin/dude"
dir2_path = "/bin"
file = "secret.txt"
parser = argparse.ArgumentParser()
parser.add_argument("--init",  help="initialize the pw file at location /bin/INIT")
parser.add_argument("--list", "-l", help="list all of the entries", action="store_true")
parser.add_argument("--search", "-s", help="search the file for SEARCH_TERM")
parser.add_argument("--nocase", "-i", help="search the file for case-insensitive SEARCH_TERM", action="store_true")
parser.add_argument("--add", "-a", nargs=3, metavar="ADD", help="add the following information to the file")

args = parser.parse_args()

if args.init:
    print("init")
    initialize(args.init)

path_to_file = f"{dir1_path}/{file}"

with open(path_to_file, "r") as f:
    write_location = f"/bin/{f.readline()}"


if args.add:
    arg_list = args.add
    line = f"{arg_list[0]}:{arg_list[1]}:{arg_list[2]}\n"
    add_info(line)


if args.list:
    list_all()

if args.nocase:
    if args.search:
        res = search_term_i(args.search)
        for line in res:
            print(line)
    else:
        print("need search term defined")
    sys.exit(0)


if args.search:
    res = search_term(args.search)
    for line in res:
        print(line)
    sys.exit(0)

print("done")
