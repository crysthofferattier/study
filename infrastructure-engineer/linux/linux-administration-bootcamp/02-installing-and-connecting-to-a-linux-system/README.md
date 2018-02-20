# Installing and Connecting to a Linux System

## Table of Contents
1. [Linux Distributions](#linux-distributions)
	1. [Linux](#linux)
	2. [Linux Kernel](#linux-kernel)
	3. [Linux Distro](#linux-distro)
	4. [Linux isn't just for business](#linux-isnt-just-for-business)
	5. [Linux is Linux](#linux-is-linux)
2. [Getting Connected](#getting-connected)
	1. [What you will learn](#what-you-will-learn)
	2. [Connecting Directly](#connecting-directly)
3. [Connecting Directly VM](#connecting-directly-vm)
	1. [Take it easy](#take-it-easy)

## 1. Linux Distributions

### Linux

* Linux is an Operating System
* Linux OS = Linux Distribution
	* Curated software

### Linux Kernel

* Distro/Flavor = Distribution
* The kernel is the core
* Linux Kernel + Apps = Distro

### Linux Distro

* redhat
	* Banks
	* Airlines
	* Telecoms
	* Healthcare
* Ubuntu
	* Startups
	* SaaS
	* Social Networkers
	* Cloud Based

### Linux isn't just for business

* Linux Mint
* Debian
* Mageia
* Fedora
* openSUSE
* Arch Linux
* Slackware

### Linux is Linux

* linux concepts are universal
* Each distro is slightly different
* You can accomplish the same goals on most Linux distros
* You can't make a "wrong" choice

### Sumary

* Linux Distro = kernel + software
* RHEL and Ubuntu
* CantOS = RHEL - branding/logos

## 2. Getting Connected

### What you will learn

* How to log into Linux
* What SSH is
* Which SSH clients to use

### Connecting Directly

* Using Ubuntu
* Log into the GUI
	* Open up a terminal

* Open terminal: 
	* Menu, type 'Terminal'
	* Ctrl + Alt + T

* Log into the commnd line
	* Type username and password

* SSH command line utility
	* puTTy (Windows)
	* Command line
```
$ ssh [user]@[host addr]
$ ssh root@192.168.0.100
$ ssh user@linuxsvr.yourcompany.com
$ ssh 10.0.0.4
```

### Sumary
* If you have ´physical access or if the Linux system is running in a VM, log in directly
* To log in over the network use SSH
* puTTy is a Windows SSH Client
* The command line utility ssh is used in Mac

## 3. Connecting Directly VM

### Take it easy

* Connect directly to the virtual machine
	* Start virtualbox
	* Start the virtual machine
	* Type into the window to interact directly with the VM