#/usr/bin/python3

# Import needed classes 
import time
import sys
import os

# Import utilities from other folder
#sys.path.insert(0, os.getcwd() + '/utils')
#from utils import timed_print, print_line, pwd_python

# Set the pace of the print statements and line nums
time_var = 0.01
line_num = 150

def timed_print(string, delay):
    for char in string:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Print the introduction text
def print_pwd(path):

#    print_line('#', line_num)
    with open(path) as f:
        lines = f.readlines()
    for line in lines:
        timed_print(line.strip(), time_var)


def get_user_choice():

    timed_print('\tENTER THE PATH:', time_var)
    choice = input('\t\t')
    correct = False
    string = ''
    if(choice == pwd_python()):
        string = 'Correct!'
        correct = True; 
    else:
        string = 'So close ... try again!'
        timed_print(string, time_var)
        return(get_user_choice())
    timed_print(string, time_var)
    print_line('#', line_num)
    return(correct)

def main():

    os.system('clear')
    print_pwd('pwd_intro.txt')
    timed_print('Press any key when you\'ve ran the command: ', time_var)
    input()
    print_pwd('pwd_quiz.txt')
    choice = get_user_choice()
        
if __name__ == '__main__':
	main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
