#!/bin/bash

# Installing the VIM Stuff
pkg install /root/vimtest/vim-common_8.1.2269-1ubuntu5_all.deb
pkg install /root/vimtest/vim-runtime_8.1.2269-1ubuntu5_all.deb
pkg install /root/vimtest/vim_8.1.2269-1ubuntu5_amd64.deb
pkg install /root/vimtest/xxd_8.1.2269-1ubuntu5_amd64.deb

# Delete the directory
rm -rf /root/vimtest/
