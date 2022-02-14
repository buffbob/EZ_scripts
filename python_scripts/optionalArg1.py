#! /usr/bin/env python3

import argparse

print("start")

par = argparse.ArgumentParser()

par.add_argument("--verbosity", help="increase output verbosity", type=int)
args = par.parse_args()

if args.verbosity:
    print("verbose")
