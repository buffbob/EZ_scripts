#! /usr/bin/env python3

import argparse
import subprocess

par = argparse.ArgumentParser()
# -s SEARCH_TERM

process = subprocess.Popen(['grep', '-i', 'gmail', '/bin/pw.pw'],
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

print("dude")
output = process.stdout.readlines()
for o in output:
    print(o)
