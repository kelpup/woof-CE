. /etc/profile
[ -f /etc/bash_completion ] && . /etc/bash_completion


# Modifying Prompt
export PS1="\[\e[36m\]kelpup\[\e[m\] running \[\e[35m\]\V\[\e[m\] \[\e[31m\]\\$\[\e[m\]  "


# Trying to add tip everytime user opens command line

# Getting number of lines (tips) in text file
NUM_LINES=$(cat /root/.tips.txt | wc -l)

# Randomizing that number
TIP_NUM=$(($RANDOM % $NUM_LINES+1))

# Actually printing it
echo "Welcome back! :) Here's a little Linux Command Line tip" 
echo "Did you know that:";
FLAG="${TIP_NUM}p"
sed -n $FLAG .test.txt | echo


