#!/usr/bin/python3

import time
import sys
import os

# Helper function to print slowly 
def timed_print(string, delay):
	for char in string:
		print(char, end ='')
		sys.stdout.flush()
		time.sleep(delay)
	print()
		
# Helper function to print a full line
def print_line(string, num):
    for i in range(num):
        print(string, end ='')
    print()


# Python pwd function
def pwd_python():
    cwd = os.getcwd()
    return(cwd)

# Python ls function
def ls_python():
    ls = os.listdir('.')
    return(ls)

# Python cd function
def cd_python(path):
    if(path == '..'):
        curr = os.getcwd()
        os.chdir(curr + '/..')
    elif (path == ''):
        os.chdir('~')
    else:
        os.chdir(path)

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
