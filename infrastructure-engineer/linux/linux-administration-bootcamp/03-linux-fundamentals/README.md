# Linux Fundamentals

## Table of Contents
1. [Linux Directory Structure](#linux-directory-structure)
	1. [What you will learn](#what-you-will-learn)
	2. [Common Directories](#common-directories)
	3. [Comprehensive Directory Listing](#comprehensive-directory-listing)
2. [The Shell](#the-shell)

## Linux Directory Structure
The filesystem hierarchy

### What you will learn

* Linux directory structure
* Location of operating system components
* Application directory structures

### Common Directories

* **/**: "Root", the top of the file system hiearchy
* **/bin**: Binaries and other executable programs
* **/etc**: System configuration files
* **/home**: User home directories (Documents, Music, Video, etc)
* **/opt**: optional or third party software
* **/tmp**: Temporary space, typically cleared in reboot
* **/usr**: User related programs
* **/var**: Variable data, most notably log files

![linux-folders-hierarchy](https://www.linuxtrainingacademy.com/wp-content/uploads/2014/03/linux-folders.jpg)

![linux-forlders](http://www.linuxtrainingacademy.com/wp-content/uploads/2014/03/linux-directory-tree.jpg)

### Comprehensive Directory Listing

* **/**: "Root", the top of the file system hiearchy
* **/bin**: Binaries and other executable programs
* **/boot**: Files needed to boot the operating system
* **/cdrom**: Mount point for CD-ROMs
* **/cdgroup**: Control Groups hierarchy
* **/dev**: Divice files, typically controlled by the operating system and the system administrators
* **/etc**: System configuration files
* **/export**: Shared file systems
* **/**: Home directories
* **/**: System libraries
* **/**: System libraries, 64 bit
* **/lost+found**: Used by the file system to store recovered files after a file system check has been performed
* **/media**: Used to mount removable media like CD-ROMs
* **/mnt**: Used to mount external file systems
* **/opt**: Optional or third party software
* **/proc**: Provides info aboute running processes
* **/root**: The home directory for the root account
* **/sbin**: System administration binaries
* **/selinux**: Used to display information about SELinux
* **/srv**: Contains data with is served by the system
* **/srv/www**: Web server files
* **/srv/ftp**: FTP files
* **/sys**: Used to display and sometimes configure the devices known to the Linux kernel
* **/tmp**: Temporary space, typically cleared on reboot
* **/usr**: user related programs, libraries, and docs
* **/usr/bin**: Binaries and other executable programs
* **/usr/lib**: Libraries
* **/usr/local**: Locally installed software that is not part of the base operating system
* **/usr/sbin**: System administration binaries
* **/var**: Variable data, most notably log files
* **/var/log**: Log files

### Application Directory Structures

* **/user/local**:
	* **/usr/local/crashplan/bin**
		* Application binaries
	* **/usr/local/crashplan/etc**
		* Application config behavior in runtime
	* **/usr/local/crashplan/lib**
		* Application libraries
	* **/usr/local/crashplan/log**
		* Log files

* **/opt**:
	* **/opt/local/crashplan/bin**
	* **/opt/local/crashplan/etc**
	* **/opt/local/crashplan/lib**
	* **/opt/local/crashplan/log**

* **Variation**:
	* **/etc/ope/myapp**
	* **/opt/myapp/bun**
	* **/opt/local/myapp/lib**
	* **/var/opt/myapp**

	* **/user/local/bin/myapp**
	* **/user/local/etc/myapp.conf**
	* **/user/local/lib/libmyapp.so**

	* **/opt/google**
	* **/opt/google/chrome**
	* **/opt/google/earth**

### Summary

* The most common directories to know are?:
	* **/**
	* **/bin**
	* **/etc**
	* **/home**
	* **/opt**
	* **/tmp**
	* **/usr**
	* **/var**

## The Shell

### What you will learn

* What the shell is
* How to access the shell
* What the superuser account is

### 1. What the shell is
* The default interface to Linux
* A program that accepts your commands and executes those commands
* Also called a command line interpreter

### Command Line Interface vs a GUI
CLI x GUI

* The command line is more powerful
* The will always be a command line
* Server distributions do not includ GUIs
* Desktop distributions have a GUIs and CLIs

### 