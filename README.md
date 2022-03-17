# KelPup - a Puppy Linux distro for beginners

[KelPup](https://kelpup.github.io/kelpup/Home/) is an in-development [woof-built](https://github.com/puppylinux-woof-CE/woof-CE) [Puppy Linux](https://puppylinux.com/) distribution targeted towards those interested in Linux but unsure of where to begin. It's designed to provide the experience of booting a Linux distro off of a USB, getting a taste for how Linux works, and giving the confidence to start exploring other distros. 

Testing: [![Build status](https://github.com/puppylinux-woof-CE/woof-CE/actions/workflows/build.yml/badge.svg)](https://github.com/kelpup/woof-CE/actions/workflows/test.yml)

KelPup is built on top of [FossaPup64](https://blog.puppylinux.com/fossapup64-release)- built by Puppy Linux developer [Phil Broughton](https://github.com/mrfricks). Puppy Linux was created by [Barry Kauler](https://bkhome.org/news/). 

KelPup is built using [woof-CE](https://github.com/puppylinux-woof-CE/woof-CE), a Puppy Linux distribution builder forked from Barry Kauler's woof2 by [the Puppy Linux github organization](https://github.com/puppylinux-woof-CE).

# Contribute

1. Fork this fork of woof-CE
2. Go to the Actions tab and enable actions
3. Make any modifications you want! 
4. Run the test workflow manually, with the branch with your modifications as the input
6. Download the ISO from the build artifacts, install it, and test it out
7. Open a pull request to kelpup/woof-CE!

Installation info for [MacOS](https://kelpup.github.io/kelpup/Instructions/MacDownload.html) and [Windows](https://kelpup.github.io/kelpup/Instructions/WindowsDownload.html)

# Test Workflow

The test workflow builds a x86_64, ubuntu focal64 puppy linux distribution with a 5.4.x-x86_64 kernel from the files in the branch that is input into it. It builds directly on GitHub, and uploads the ISO as a build artifact. 

<img width="1107" alt="Screen Shot 2022-03-16 at 11 55 18 PM" src="https://user-images.githubusercontent.com/65368903/158733917-dd6fb32f-e3c6-4062-a0d5-dc2e3e14aafc.png">
1. Go to GitHub Actions, and select Test
2. Hit Run Workflow, then Run Workflow again
3. Wait for the test to complete (20min-1hr) and a green checkmark appears
4. Click on the test, and scroll down to the build artifacts and download the artifact
5. Unzip the artifact, and the ISO will be in the resulting folder
<img width="1139" alt="Screen Shot 2022-03-16 at 11 59 41 PM" src="https://user-images.githubusercontent.com/65368903/158734402-fc5fe4ea-f7d5-437b-a3d1-562b766f3f79.png">



# Contributing to woof-CE: using Gitpod

To modify woof-CE and push the changes to GitHub without having to set up a local development environment: [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/puppylinux-woof-CE/woof-CE)

Not all of woof-CE can run [without root access](https://github.com/gitpod-io/gitpod/issues/39), but most of woof-CE works on Gitpod and it's possible to [boot Puppy inside QEMU and control it over VNC](https://www.gitpod.io/blog/native-ui-with-vnc/), all through the browser.

To work on woof-CE in a fork, through Gitpod:

1. Fork woof-CE.

2. Browse to `https://gitpod.io/#https://github.com/your-github-username/woof-CE`.

# Directory Structure

Woof-CE has five directories:

- woof-arch   : architecture-dependent (x86_64, x86, ARM) files, mostly binary executables.
- woof-code   : the core of Woof. Mostly scripts.
- woof-distro : distro-configuration (Debian, Slackware, etc.) files.
- kernel-kit  : scripts to download, patch, configure and build the kernel.
- initrd-progs: scripts and files to generate the initial ramdisk

To create a working directory, named `woof-out_*`, you first have to run the `merge2out` script. This merges the 5 directories into a directory named `woof-out_*`. You then `cd` into `woof-out_*` and run the build scripts.

The great thing about this merge operation is that you can choose exactly what you want to go into woof-out. You can choose the host system that you are building on (usually x86_64), the target (exs: x86_64 x86, ARM), the compatible-distro (ex: slackware), and the compat-distro version (ex: 15.0). So, you create woof-out without any confusing inappropriate content.

So, to get going with woof-CE, open a terminal and do this:

    ./merge2out
    cd ../woof-out_*

# Preparation

1. Suitable build environment
  - Linux partition (ext2/3/4)
  - At least 6-10GBs of space

2. Host operating system
  - A recent Woof-CE puppy with the devx (compilers, headers and other development tools) installed. Otherwise use [run_woof](https://github.com/puppylinux-woof-CE/run_woof).
  
3. Choose a compatible-distro.

This is the distro whose packages you are going to 'borrow' to build your Puppy. Open file DISTRO_SPECS in a text editor and change this line:

    DISTRO_BINARY_COMPAT="ubuntu"

to what you want: `slackware`, `devuan`, `ubuntu`, `debian` or `puppy`.

# Building a Puppy: using the commandline scripts

Open a terminal in the `woof-out_*` directory.

0. Download package database files

       ./0setup

OPTIONAL: Tweak common PET package selection. You can edit the variable PKGS_SPECS_TABLE in file `DISTRO_PKGS_SPECS-*` to choose the packages that you want in your build.

1. Download packages

       ./1download

About 500MB drive space is required, but this may vary enormously depending on the package selection.

2. Build the cut-down generic Puppy-packages

       ./2createpackages

3. Build Puppy live-CD

       ./3builddistro

This gets built in a directory named `sandbox3` and as well as the live-CD ISO file you will also find the individual built files and the `devx` file.

# TECHNICAL NOTES

## History

Woof-CE (woof-Community Edition) is  a fork of Barry Kauler's woof2 fossil repository of Nov 11, 2013 commit f6332edbc4a75c262a8fec6e7d39229b0acf32cd.

## packages-templates directory

any directory in the template, the files in the target pkg will be cut down to the same selection (even if empty dir). Exception, file named `PLUSEXTRAFILES` then target will have all files from deb.

- 0-size file, means get file of same name from deb (even if in different dir) to target.
- Non-zero file, means copy this file from template to target.
- Template files with `-FULL` suffix, rename target file also (exs: in coreutils, util-linux).
  
Any dir in template with `PKGVERSION` in name, substitute actual pkg version number in target dir. Except for /dev, /var, all dirs in target are deleted to only those in template, except if file `PLUSEXTRADIRS` is found in template.
  
As a last resort, if target pkg is wrong, a file `FIXUPHACK` is a script that can be at top dir in template. It executes in target, with current-dir set to where `FIXUPHACK` is located. (ex: perl_tiny). Ran into problem slackware post-install scripts messing things up. See near bottom of '2createpackages' how damage is limited. Also `DISABLE_POST_INSTALL_SCRIPT=yes` in `FIXUPHACK` to disable entirely.
  
If a dir in template has files in it then target is cut down (unless `PLUSEXTRAFILES` present), however there are some exceptions (such as .so regular files).

## Packages-puppy-*

Notice that there are `Packages-puppy-noarch-official`, also `Packages-puppy-common-official`

The single-digit `-2-`, `-3-`, `-4-`, `-5-` files reside on ibiblio.org also. These files list the complete contents of each repository.

## Puppy filenames

The main Puppy files are:

    vmlinuz, initrd.gz, puppy.sfs, zdrv.sfs, fdrv.sfs, adrv.sfs, ydrv.sfs

Versioning is put into the last two, for example:

    vmlinuz, initrd.gz, puppy_slacko_7.0.0, zdrv_slacko_7.0.0.sfs fdrv_slacko_7.0.0.sfs, adrv_slacko_7.0.0.sfs, ydrv_slacko_7.0.0.sfs

...those last two names are intended to be unique for that build of Puppy, so they can be found at bootup.

## DISTRO_SPECS file

The filenames are stored in the built Puppy, in /etc/DISTRO_SPECS.
For example:

    DISTRO_PUPPYSFS='puppy_slacko_7.0.0.sfs'
    DISTRO_ZDRVSFS='zdrv_slacko_7.0.0.sfs'
    DISTRO_FDRVSFS='fdrv_slacko_7.0.0.sfs'
    DISTRO_ADRVSFS='adrv_slacko_7.0.0.sfs'
    DISTRO_YDRVSFS='ydrv_slacko_7.0.0.sfs'

So, any script that wants to know what the names are can read these variables.

Woof 3builddistro also copies DISTRO_SPECS into the initrd.gz, so that the `init` script can see what files to search for.

However, in a running Puppy, you can find out the filenames in the way that scripts have done before, by reading `PUPSFS` and `ZDRV` variables in /etc/rc.d/PUPSTATE.

In fact, to clarify the difference between these two sets of variables,
I have put this comment into /etc/DISTRO_SPECS:

    #Note, the .sfs files below are what the `init` script in initrd.gz searches for,
    #for the partition, path and actual files loaded, see `PUPSFS` and `ZDRV` in /etc/rc.d/PUPSTATE

# by 01micko

Woof-CE, a fork of woof2 can build the same as woof2 however a new feature has been added as of today. It now has the ability to build a distro with out modules in the initrd.gz, a feature which had been pioneered by Fatdog  developers kirk and jamesbond. This has a number of advantages over the  legacy kernel builds.
1. No messy copying kernel modules from the initial ram disk to the root system.
2. Ease of changing kernels.

I have named this the 'huge' type kernel, for want of a better term. The rationale for this is that Slackware developers name their default kernel `huge-$some_suffix`. The reason is that the vmlinuz kernel image contains all the necessary filesystem and hardware drivers to get the system to boot and hand over to the real running system. Once that occurs, kernel modules are loaded to bring up the rest of the hardware and extra filesystems if necessary.

"kernel-kit", part of woof-CE, has the ability to produce one of these 'huge' style kernel packages. Please read the relevant  README and the comments in "build.conf" inside the kernel-kit directory.

If you have built a "huge" style kernel with kernel-kit then place the package in the "huge_kernel" directory at the root of your woof installation. If not, one will be downloaded for you after you invoke 3builddistro from the CLI. You do get a choice of which version you want. Be sure you choose the correct architecure. All 32 bit builds are suffixed with either  i486, i686 or x86. All 64 bit builds are suffixed x86_64. At the end you will end up with an ISO image, devx and checksums as usual.

Regards,
Barry Kauler
puppylinux.com
