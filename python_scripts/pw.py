#! /usr/bin/env python3
'''
a command line program to raise arg1 to power of arg2
> ./pw.py 3 4
> 80

'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", help="the base number", type=int)
parser.add_argument("y", help="the power to raise the base to", type=int)
args = parser.parse_args()

z = args.x**args.y

print(f"{args.x} to the {args.y} = {z}")
