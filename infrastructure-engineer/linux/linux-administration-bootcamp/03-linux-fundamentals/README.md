# Linux Fundamentals

## Table of Contents
1. [Linux Directory Structure](#1-linux-directory-structure)
	1. [Common Directories](#common-directories)
	2. [Comprehensive Directory Listing](#comprehensive-directory-listing)
	3. [Application Directory Structures](#application-directory-structures)

2. [The Shell](#2-the-shell)
	1. [What the shell is](#what-the-shell-is)
	2. [Command Line Interface vs a GUI](#command-line-interface-vs-a-gui)
	3. [The Prompt](#the-prompt)
	4. [Root, the Superuser](#root-the-superuser)
	5. [Shorcut](#shorcut)
	6. [Multi-Line Prompts](#multi-line-prompts)

3. [Basic Linux Commands](#3-basic-linux-commands)
	1. [Basic Commands](#basic-commands)

4. [Getting Help at the Command Line](#4-getting-help-at-the-command-line)
	1. [Navigating Man Pages](#navigating-man-pages)
	2. [Environmental Variables](#environmental-variables)
	3. [PATH](#path)
	4. [Which Command Exactly?](#which-command-exactly)
	5. [Starting to Fish](#starting-to-fish)	
	6. [Get Help with --help or -h](#get-help-with-help-or-h)
	7. [Searching Man Pages](#searching-man-pages)

## 1. Linux Directory Structure
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

## 2. The Shell

### What you will learn

* What the shell is
* How to access the shell
* What the superuser account is

### What the shell is
* The default interface to Linux
* A program that accepts your commands and executes those commands
* Also called a command line interpreter

### Command Line Interface vs a GUI
CLI x GUI

* The command line is more powerful
* The will always be a command line
* Server distributions do not includ GUIs
* Desktop distributions have a GUIs and CLIs

### The Prompt

* Shell prompt
```
[user]@[linux-system]:[indicate-user]
ubuntu@ubuntu-vm:~$ [command]
```

* Superuser:
```
[user]@[linux-system]:[indicate-user]
root@ubuntu-vm:~# [command]
```

*
```
ubuntu@ubuntu-vm:~$
root@ubuntu-vm:~#
root:/home/ubuntu
ubuntu@ubuntu-vm:~>
16:45:51 ubuntu-vm ~$
$
%
>
```

### Root, the Superuser

* Root is all powerfull
* Normal accounts can only do a subset of the things root can do
* Root access is typically restricted to system adminitrators
* Root access may be required to install, atart, or stop an application
* Day to day activities will be performed using a normal account
* 

### Shorcut

* Tilda Expansion: shorcut for home directory
	* ~jason: /home/jason
	* ~pat: /home/pat
	* ~root: /root
	* ~ftp: /srv/ftp

### Multi-Line Prompts
```
linuxsvr:[/home/jason]
$
```

```
[Mon 14/02/18 12:22 EST][pts/0]
<json@linuxsvr:~>
zsh 14 %
```

### Summary

* The shell is the default user interface
* Use the terminal application to get to the CLI
* Shell prompts can vary greatly in appearance
* Root is the superuser

## 3. Basic Linux Commands
Case sensitive

### Basic Commands

* ls: List directories contents
	* ls
```
ubuntu@ubuntu-vm:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
```
	* ls [arguments]
		* ls -l
		* ls -a
		* ls -la

* cd: Changes the currenty directory
	* cd [directory-name]

```
ubuntu@ubuntu-vm:~$ cd Desktop/
ubuntu@ubuntu-vm:~/Desktop$
```

* pwd: Display the present working directory
```
ubuntu@ubuntu-vm:~/Desktop$ pwd
/home/ubuntu/Desktop
```

* cat: Concatenates and display files
```
ubuntu@ubuntu-vm:~/Desktop$ cat file.txt
Hello World
```

* echo: Display arguments to the screen
```
ubuntu@ubuntu-vm:~/Desktop$ echo $PATH
/home/ubuntu/bin:/home/ubuntu/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

* man: Display the online manual
```
ubuntu@ubuntu-vm:~/Desktop$ man ls
```

* clear: CLear the screen
```
ubuntu@ubuntu-vm:~/Desktop$ clear
```

* exit: Exits the shell or your current session
```
ubuntu@ubuntu-vm:~/Desktop$ exit
```

## 4. Getting Help at the Command Line

### Navigating Man Pages

* Enter: Move down one line
* Sapce: Move down one page
* g: Move to the top of the page
* G: Move to the bottom of the page
* q: Quit

### Environmental Variables
* Storage location that has a name and value
* Typically uppercase
* Access the contents by executing:
	* echo $[var-name]

### PATH

* An environment variable
* Controls the command search path
* Contains a list of directories

### Which Command Exactly?
* which: locate a command

```
ubuntu@ubuntu-vm:~$ which cat
/bin/cat

ubuntu@ubuntu-vm:~$ which tac
/usr/bin/tac
```

### Starting to Fish

* Look at the directories in $PATH
* Look at the files in each directory
* Use man to learn what the command does

### Get Help with --help or -h

* Add --help to a command to get help
* Try -h if --help doesn't work

```
ubuntu@ubuntu-vm:~$ ls -h
ubuntu@ubuntu-vm:~$ ls --help
```

### Searching Man Pages

* man -k [search-term]

```
ubuntu@ubuntu-vm:~$ man -k calendar
cal (1)              - displays a calendar and the date of Easter
calendar (1)         - reminder service
ncal (1)             - displays a calendar and the date of Easter
```

### Sumary

* **man** is used to display documentation
* $PATH controls your search path
* Learn the full path to commands with which
* Ask commands for help with --help or -h
* Search man pages by using man -k