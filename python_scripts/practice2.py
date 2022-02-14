#! /usr/bin/env python3

import argparse
par = argparse.ArgumentParser()

par.add_argument("square", help="display square of argument", type=int)
args = par.parse_args()

print(args.square**2)
