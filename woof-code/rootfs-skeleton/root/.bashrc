. /etc/profile
[ -f /etc/bash_completion ] && . /etc/bash_completion


# Trying to add tip everytime user opens command line

# Getting number of lines (tips) in text file
NUM_LINES=$(cat ~/Desktop/nd_work/open_source/testing/test.txt | wc -l)

# Randomizing that number
TIP_NUM=$(($RANDOM % $NUM_LINES+1))

# Actually printing it
echo "Welcome back! :) Here's a little Linux Command Line tip" 
echo "Did you know that:";
FLAG="${TIP_NUM}p"
sed -n $FLAG .test.txt | echo
