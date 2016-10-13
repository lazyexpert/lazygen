#!/usr/bin/python

import sys
import itertools

DEFAULT_SYMBOLS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

# Simple help output
def printHelp():
    print "\nLAZY PASSWORD GENERATOR"
    print "\nUsage:"
    print "./main.py [-l number] || [--length number] [-s string] || [--symbols string]"
    
    print "\nOptions:"
    print "\t-l NUMBER or --length NUMBER - required, the max length of the password, integer"
    print "\t-s STRING or --symbols STRING - optional, symbols set, default(ascii) might be used"

    # TODO: think of pipe here ...
    print "\nPro usage :D :"
    print "./start -l NUMBER > dict.txt"

# Find target argument and return its value
def findValue(arg, arg2):
    for i, val in enumerate(sys.argv):
        if val == arg or val == arg2:
            return sys.argv[i+1]
    return ""

# Parse arguments
def parseArgs():
    length = int (findValue('-l', '--length'))
    symbols = findValue('-s', '--symbols')
    if len(symbols) == 0:
        symbols = DEFAULT_SYMBOLS
    while length != 3:
        generate(symbols, length)
        length = length -1

# Generate password list
def generate(symbols, length):    
    res = itertools.product(symbols, repeat=length)
    for i in res: 
        print ''.join(i)    

# Main function
def main():
    if '-h' in sys.argv or '--help' in sys.argv:
        printHelp()

    if len(sys.argv) == 1 or (not "-l" in sys.argv or "--length" in sys.argv) or len(sys.argv)%2 != 1:
        printHelp() 
    else: 
        parseArgs()

# Start app execution
main()