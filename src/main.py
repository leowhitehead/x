import sys
import os
from parser import parse, error
from data import *
from base64 import b64encode

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        error("invalid flags/options, use -h for help")
    flags = {'-'+x: None for x in ['o','s','c']}
    args = sys.argv[1:]
    if '-h' in args:
        help()
    compiler = defaultCompiler
    outfile = "a.out"
    if '-s' in args:
        flags['-s'] = True
        args.remove('-s')
        outfile = "a.c"
    for i in range(len(args)-1):
        if args[i] == '-o':
            outfile = args[i+1]
            del args[i+1]
            del args[i]
            break
    for i in range(len(args)-1):
        if args[i] == '-c':
            compiler = args[i+1]
            del args[i+1]
            del args[i]
            break
    if len(args) != 1:
        error("Invalid flags/options, use -h for help")
    sourceName = args[0]
    with open(sourceName, 'r') as f:
        source = f.read()
    output = parse(source)
    if not flags['-s']:
        os.system(f"echo {output} | base64 -d | {compiler} -w -x c - -o {outfile}")
    else:
        os.system(f"echo {output} | base64 -d > {outfile}")

def help():
    print("Usage: x program.x [-o output] [-c compiler] [-s]\n")
    sys.exit(0)

if __name__ == "__main__":
    main()