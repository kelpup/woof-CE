#!/usr/bin/python3

# Import needed classes 
import time
import sys
import os

# Import utilities from other folder
ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.insert(0, os.path.join(ROOT_DIRECTORY, 'utils'))
from utils import timed_print, print_line

# Set the pace of the print statements and line nums
time_var = 0.05
line_num = 150

# Print the introduction text
def print_intro(path):

    print()
    with open(path) as f:
        lines = f.readlines()
    for line in lines:
        timed_print(line.strip(), time_var)


def get_user_choice():
    choice = input('\tENTER (Y/N):')
    if(choice.upper() != 'Y'):
        print('Bold ... I like it!')
        timed_print('Press any key to begin: ', time_var)
        input()
        os.system('clear')
        return(False)
    else:
        timed_print('Right on! Let\'s get into it!', time_var)
        print_line('#', line_num)
        timed_print('Press any key to begin: ', time_var)
        input()
        os.system('clear')
        return(True)



def main():

    os.system('clear')
    directory = os.path.join(ROOT_DIRECTORY, 'introduction/introduction.txt')
    print_intro(directory)   
    choice = get_user_choice()
    if(choice):
        pass
        # do the ls, cd, pwd, etc tutorial
    else:
        pass
        # go into the next time 
        
if __name__ == '__main__':
	main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
