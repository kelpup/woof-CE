. /etc/profile
[ -f /etc/bash_completion ] && . /etc/bash_completion


# Modifying Prompt
export PS1="\[\e[33m\][\[\e[m\]\[\e[31m\]kelpup\[\e[m\] running \[\e[35m\]bash\[\e[m\]\[\e[33m\]]\[\e[m\] \[\e[36m\]\w\[\e[m\] \[\e[34m\]\\$\[\e[m\] "


# Adding VIM - NOTE: Didn't work :(

# Installing the VIM Stuff if not already installed
#if ! command -v vim &> /dev/null; then
#	pkg install /root/Startup/vim-common_8.1.2269-1ubuntu5_all.deb
#	pkg install /root/Startup/vim-runtime_8.1.2269-1ubuntu5_all.deb
#	pkg install /root/Startup/vim_8.1.2269-1ubuntu5_amd64.deb
#	pkg install /root/Startup/xxd_8.1.2269-1ubuntu5_amd64.deb
#	clear
#fi

# Trying to add tip everytime user opens command line

# Getting number of lines (tips) in text file
NUM_LINES=$(cat /root/.tips.txt | wc -l)

# Randomizing that number
TIP_NUM=$(($RANDOM % $NUM_LINES+1))

# Actually printing it
echo "Welcome back! :) Here's a little Linux Command Line tip" 
echo "Did you know that:";
FLAG="${TIP_NUM}p"

# Once/If we get cowsay to work, add the commented line instead
#sed -n $FLAG .tips.txt | cowsay
sed -n $FLAG .tips.txt
