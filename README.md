# KelPup - a Puppy Linux distro for beginners

[KelPup](https://kelpup.github.io/kelpup/Home/) is an in-development [woof-built](https://github.com/puppylinux-woof-CE/woof-CE) [Puppy Linux](https://puppylinux.com/) distribution targeted towards those interested in Linux but unsure of where to begin. It's designed to provide easy (ish!) instructions for booting a Linux distro off of a USB, getting a taste for how Linux works and is different from Windows or MacOS, and giving the confidence to start exploring other distros. 

Testing: [![Build status](https://github.com/puppylinux-woof-CE/woof-CE/actions/workflows/build.yml/badge.svg)](https://github.com/kelpup/woof-CE/actions/workflows/test.yml)

KelPup is built on top of [FossaPup64](https://blog.puppylinux.com/fossapup64-release)- built by Puppy Linux developer [Phil Broughton](https://github.com/mrfricks). Puppy Linux was created by [Barry Kauler](https://bkhome.org/news/). 

KelPup is built using [woof-CE](https://github.com/puppylinux-woof-CE/woof-CE), a Puppy Linux distribution builder forked from Barry Kauler's woof2 by [the Puppy Linux github organization](https://github.com/puppylinux-woof-CE).

## Contribute

1. Fork this fork of woof-CE to your own GitHub account
2. Open your fork, go to the Actions tab and enable actions
3. Make any modifications you want, either on lastbuild or your own branch! See the wiki or read below about the directory structure for guidance
4. Run the test workflow manually (instructions below), with the branch with your modifications as the input
6. Download the ISO from the build artifacts, install it, and test it out
7. When you're happy with it, open a pull request and select kelpup/woof-CE!

Installation info for [MacOS](https://kelpup.github.io/kelpup/Instructions/MacDownload.html) and [Windows](https://kelpup.github.io/kelpup/Instructions/WindowsDownload.html).

### We need help with...

* Bug reports - test out our latest ISO release out yourself and let us know what didn't go right 
* Learning games - we'd like to include simple python learning games, if you'd like to make them ([Issue #27](https://github.com/kelpup/woof-CE/issues/27))
* pTheme development - check out the pTheme page on the wiki for instructions and make some modifications to KelPup's "Pink Moon" pTheme ([Issue #24](https://github.com/kelpup/woof-CE/issues/24))
* Ideas - a feature you think should be added, an idea that should be explained better, let us know!

## Test Workflow

We're building our distro by modifying the distro specifications in `woof-CE/woof-distro/x86_64/ubuntu/focal64/` to decide what to include and not include in the distro and the root filesystem of the distro in `woof-CE/woof-code/rootfs-skeleton/`.

The test workflow builds a x86_64, ubuntu focal64 puppy linux distribution with a 5.4.x-x86_64 kernel from the files in the branch that is input into it. It builds directly on GitHub, and uploads the ISO as a build artifact. 

<img width="1107" alt="Screen Shot 2022-03-16 at 11 55 18 PM" src="https://user-images.githubusercontent.com/65368903/158733917-dd6fb32f-e3c6-4062-a0d5-dc2e3e14aafc.png">

1. Go to GitHub Actions, and select Test
2. Hit Run Workflow, then Run Workflow again
3. Wait for the test to complete (20min-1hr) and a green checkmark appears
4. Click on the test, and scroll down to the build artifacts and download the artifact
5. Unzip the artifact, and the ISO will be in the resulting folder

<img width="1139" alt="Screen Shot 2022-03-16 at 11 59 41 PM" src="https://user-images.githubusercontent.com/65368903/158734402-fc5fe4ea-f7d5-437b-a3d1-562b766f3f79.png">

## Directory Structure

Woof-CE has five directories:

- woof-arch   : architecture-dependent (x86_64, x86, ARM) files, mostly binary executables.
- woof-code   : the core of Woof. Mostly scripts.
- woof-distro : distro-configuration (Debian, Slackware, etc.) files.
- kernel-kit  : scripts to download, patch, configure and build the kernel.
- initrd-progs: scripts and files to generate the initial ramdisk

The majority of the code we modified was as follows:

- woof-code   : modified the base filesystem, added things to the packages
- woof-distro : modified the distro specification files  

### Where is...?

woof-code
* root filesystem in rootfs-skeleton
* build scripts
* packages with applications

woof-distro
* files that specify the pet packages you want for different distro builds
* distro specification files seperated by folders (ex: focal is in ``woof-CE/woof-distro/x86_64/ubuntu/focal64/`)

init-progs
* init script (spooky!)

## Build Scripts

The GitHub workflows wrap around four main scripts that were originally designed to run via the commandline. 
0. 0setup           - download package database files as specified in the puppy pet package files under woof-distro
1. 1download        - download actual pet packages
2. 2createpackages  - build the puppy packages
3. 3builddistro     - build the ISO

All these are in woof-code. 

## Technical notes

Check out the technical notes from the [original readme](https://github.com/kelpup/woof-CE/blob/lastbuild/PUPPY_README.md) by [the Puppy Linux github organization](https://github.com/puppylinux-woof-CE).
