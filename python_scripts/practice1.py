#! /usr/bin/env python3

import argparse
par = argparse.ArgumentParser()

par.add_argument("--echo", help="echo the string you use as an argument")
args = par.parse_args()
if args.echo:
    print('echo')


