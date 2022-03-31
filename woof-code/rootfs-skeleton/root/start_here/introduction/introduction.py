#/usr/bin/python3

# Import needed classes 
import time
import sys
import os

# Import utilities from other folder
#sys.path.insert(0, os.getcwd() + '/utils')
#from utils import timed_print, print_line


# Set the pace of the print statements and line nums
time_var = 0.01
line_num = 150

# Functions copied for now
def timed_print(string, delay):
    for char in string:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Print the introduction text
def print_intro(path):

    #print_line('#', line_num)
    with open('introduction.txt') as f:
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
    print_intro('introduction/introduction.txt')   
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
