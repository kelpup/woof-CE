#!/bin/bash

# Installing the VIM Stuff
pkg install /root/vim-common_8.1.2269-1ubuntu5_all.deb
sleep(5)
pkg install /root/vim-runtime_8.1.2269-1ubuntu5_all.deb
sleep(5)
pkg install /root/vim_8.1.2269-1ubuntu5_amd64.deb
sleep(5)
pkg install /root/xxd_8.1.2269-1ubuntu5_amd64.deb
sleep(5)

touch scriptran.txt

# Delete the directory
#rm -rf /root/vimtest/
