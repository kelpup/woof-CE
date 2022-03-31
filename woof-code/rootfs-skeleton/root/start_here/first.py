#/usr/bin/python3

import time
import sys
import os

# Helper function to print slowly 
def timed_print(string, delay):
	for char in string:
		print(char, end='')
		sys.stdout.flush()
		time.sleep(delay)
	print()
		
# Helper function to print a full line
def print_line(string, num):
    for i in range(num):
        print(string, end = '')


# Python pwd function
def pwd_python():
    cwd = os.getcwd()
    return(cwd)

# Python ls function
def ls_python():
    ls = os.listdir('.')
    return(ls)

def main():
	# timed_print("Hello, there :)", 0.08)
    #print_line('#', 50)
    text_time = 0.08
    timed_print('Welcome to your first introduction to Linux!', text_time)
    timed_print('We are so glad you chose Kelpup as your beginning distribution.', text_time)
    


if __name__ == '__main__':
	main()
