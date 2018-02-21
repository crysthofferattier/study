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

5. [Working with Directories](#5-working-with-directories)
	1. [Directory shorcuts](#directory-shorcuts)
	2. [Directory Separator](#directory-separator)
	3. [Executing Commands](#executing-commands)
	4. [Creatting and Removing Directories](#creatting-and-removing-directories)

6. [Listing Files and Understanding LS Output](#6-listing-files-and-understanding-ls-output)
	1. [Decoding **ls -l** Output](#decoding-ls--l-output)
	2. [Listing All Files, Including Hidden Files](#listing-all-files-including-hidden-files)
	3. [Listing Files by Type](#listing-files-by-type)
	4. [Symbolic Links](#symbolic-links)
	5. [Listing Files by Time and in Reverse](#listing-files-by-time-and-in-reverse)
	6. [The **tree** command](#the-tree-command)
	7. [List Directories, Not Contents](#list-directories-not-contents)
	8. [Listing Files with Color](#listing-files-with-color)
	9. [Working with Spaces in Names](#working-with-spaces-in-names)

7. [File and Directory Permissions Explained - Part One](#7-file-and-directory-permissions-explained---part-one)
	1. [Permissions](#permissions)
	2. [Permissions - Files vc Directories](#permissions---files-vc-directories)
	3. [Permission Categories](#permission-categories)
	4. [Groups](#groups)
	5. [Secret Decoder Ring](#secret-decoder-ring)
	6. [Changing Permissions](#changing-permissions)
	7. [Numeric Based Permissions](#numeric-based-permissions)
	8. [Order Has Meaning](#order-has-meaning)
	9. [Commonly Used Permissions](#commonly-used-permissions)

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

### 5. Working with Directories

## Directory shorcuts

* **.** : This directory
* **..** : The parent directory
* **cd -**: Change to the previous directory

## Directory Separator

* **/** : Directory separator (forward slash)

```
ubuntu@ubuntu-vm:~$
ubuntu@ubuntu-vm:~$ cd Desktop/
ubuntu@ubuntu-vm:~/Desktop$ cd -
/home/ubuntu
ubuntu@ubuntu-vm:~$
ubuntu@ubuntu-vm:~$ pwd
/home/ubuntu
ubuntu@ubuntu-vm:~$ cd Desktop/
ubuntu@ubuntu-vm:~/Desktop$ pwd
/home/ubuntu/Desktop
ubuntu@ubuntu-vm:~/Desktop$ cd ..
ubuntu@ubuntu-vm:~$ pwd
/home/ubuntu
ubuntu@ubuntu-vm:~$ cd ..
ubuntu@ubuntu-vm:/home$ pwd
/home
ubuntu@ubuntu-vm:/home$ cd ubuntu/
ubuntu@ubuntu-vm:~$ pwd
/home/ubuntu
ubuntu@ubuntu-vm:~$ cd .
ubuntu@ubuntu-vm:~$ pwd
/home/ubuntu
ubuntu@ubuntu-vm:~$ cd ..
ubuntu@ubuntu-vm:/home$ pwd
/home
ubuntu@ubuntu-vm:/home$ cd /home/ubuntu/
ubuntu@ubuntu-vm:~$ pwd
/home/ubuntu
ubuntu@ubuntu-vm:~$ cd /var/tmp/
ubuntu@ubuntu-vm:/var/tmp$ pwd
/var/tmp
ubuntu@ubuntu-vm:/var/tmp$ echo $OLDPWD
/home/ubuntu
ubuntu@ubuntu-vm:/var/tmp$ cd -
/home/ubuntu
```

## Executing Commands

* $PATH determines command search path
* You can specify a command with a full path
* You can execute command not in $PATH
* **./command** execute command in the current directory

## Creatting and Removing Directories
* **mkdir [args] [direcory-name]**: create/remove a directory
```
ubuntu@ubuntu-vm:~/Documents$ mkdir my-directory
ubuntu@ubuntu-vm:~/Documents$ mkdir -p 1/2/3
```

* **rmdir [directory-name]**: remove a empty directory
```
ubuntu@ubuntu-vm:~/Documents$ rmdir my-directory
```

* **rm -rf [directory-name]**: recursively removes directory
```
ubuntu@ubuntu-vm:~/Documents$ rm -rf 1/
```

## Summary

* Directories shorcuts
	* **.**
	* **..**
	* **cd -**

* How to execute commands outside of $PATH
	* **/full/path/to/command**
	* **./command-in-this-dir**

* How to create and remove directories
	* **mkdir**
	* **rmdir**
	* **rm**

## 6. Listing Files and Understanding LS Output

### Decoding **ls -l** Output
```
ubuntu@ubuntu-vm:~/Desktop$ ls -l
total 4
-rw-rw-r-- 1 ubuntu ubuntu 12 Fev 19 16:51 file.txt
```

* Permissions: -rw-rw-r--
* Number of links: 1
* Owner name: ubuntu
* Group name: ubuntu
* Number of bytes in the file: 12
* Last modification time: Fev 19 16:51
* File name: file.txt

### Listing All Files, Including Hidden Files
* Hidden files begin with a period.
	* Sometimes called "dot files"
* Hidden files are not displayed by default
* To show hidden files with **ls**, use **ls -a**
* Command options can be combined
	* **ls -l -a** is the same as **ls -la** and **ls -al**
```
ubuntu@ubuntu-vm:~$ ls                                                            
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos         
ubuntu@ubuntu-vm:~$ ls -l                                                         
total 32                                                                          
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 20:16 Desktop                              
drwxr-xr-x 3 ubuntu ubuntu 4096 Fev 19 20:07 Documents                            
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Downloads                            
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Music                                
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Pictures                             
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Public                               
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Templates                            
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Videos                               
ubuntu@ubuntu-vm:~$ ls -a                                                         
.              Desktop        .local                     Videos                   
..             .dmrc          Music                      .Xauthority              
.bash_history  Documents      Pictures                   .xsession-errors         
.bash_logout   Downloads      .profile                   .xsession-errors.old     
.bashrc        .gconf         Public                                              
.cache         .gnupg         .sudo_as_admin_successful                           
.config        .ICEauthority  Templates                                           
ubuntu@ubuntu-vm:~$ ls -la                                                        
total 96                                                                          
drwxr-xr-x 15 ubuntu ubuntu 4096 Fev 19 15:06 .                                   
drwxr-xr-x  3 root   root   4096 Fev 19 11:43 ..                                  
-rw-------  1 ubuntu ubuntu  701 Fev 19 18:22 .bash_history                       
-rw-r--r--  1 ubuntu ubuntu  220 Fev 19 11:43 .bash_logout                        
-rw-r--r--  1 ubuntu ubuntu 3771 Fev 19 11:43 .bashrc                             
drwx------ 11 ubuntu ubuntu 4096 Fev 19 13:55 .cache                              
drwx------ 14 ubuntu ubuntu 4096 Fev 19 12:43 .config                             
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 20:16 Desktop                             
-rw-r--r--  1 ubuntu ubuntu   25 Fev 19 11:48 .dmrc                               
drwxr-xr-x  3 ubuntu ubuntu 4096 Fev 19 20:07 Documents                           
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Downloads                           
drwx------  2 ubuntu ubuntu 4096 Fev 19 11:47 .gconf                              
drwx------  3 ubuntu ubuntu 4096 Fev 19 13:44 .gnupg                              
-rw-------  1 ubuntu ubuntu 1320 Fev 19 13:44 .ICEauthority                       
drwx------  3 ubuntu ubuntu 4096 Fev 19 11:48 .local                              
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Music                               
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Pictures                            
-rw-r--r--  1 ubuntu ubuntu  655 Fev 19 11:43 .profile                            
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Public                              
-rw-r--r--  1 root   root      0 Fev 19 11:45 .sudo_as_admin_successful           
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Templates                           
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Videos                              
-rw-------  1 ubuntu ubuntu   54 Fev 19 13:44 .Xauthority                         
-rw-------  1 ubuntu ubuntu  268 Fev 19 13:46 .xsession-errors                    
-rw-------  1 ubuntu ubuntu 1734 Fev 19 13:24 .xsession-errors.old                
```

### Listing Files by Type

* Use **ls -F** to reveal file types
	* **/**: directory
	* **@**: Link
	* *****: Executable

```
ubuntu@ubuntu-vm:/usr/local/my-company$ ls
my-app  mylink  README

ubuntu@ubuntu-vm:/usr/local/my-company$ ls -F
my-app/  mylink@  README

ubuntu@ubuntu-vm:/usr/local/my-company$ ls -lF
total 4
drwxr-xr-x 2 root root 4096 Fev 19 20:29 my-app/
lrwxrwxrwx 1 root root   29 Fev 19 20:31 mylink -> /home/ubuntu/Desktop/file.txt
-rw-r--r-- 1 root root    0 Fev 19 20:29 README

ubuntu@ubuntu-vm:/usr/local/my-company/my-app$ ls -F
hello-world*
```

### Symbolic Links

* A link is a points to the actual file or directory
* Use the link as if it were the file
* A link can be used to create a shorcut
	* Use for long file or directory name
	* Use to indicate the current version of software

```
ubuntu@ubuntu-vm:/usr/local/my-company$ sudo ln -s ~/Desktop/file.txt mylink
```

### Listing Files by Time and in Reverse

* **ls -t**: List files by time
* **ls -r**: Reverse order
* **ls -latr**: long listing including all files reverse sorted by time

```
ubuntu@ubuntu-vm:~$ ls -l                                                         
total 32                                                                          
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 20:16 Desktop                              
drwxr-xr-x 3 ubuntu ubuntu 4096 Fev 19 20:07 Documents                            
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Downloads                            
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Music                                
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Pictures                             
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Public                               
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Templates                            
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Videos                               
ubuntu@ubuntu-vm:~$                                                               
ubuntu@ubuntu-vm:~$ ls -lr                                                        
total 32                                                                          
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Videos                               
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Templates                            
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Public                               
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Pictures                             
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Music                                
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 11:48 Downloads                            
drwxr-xr-x 3 ubuntu ubuntu 4096 Fev 19 20:07 Documents                            
drwxr-xr-x 2 ubuntu ubuntu 4096 Fev 19 20:16 Desktop                              
ubuntu@ubuntu-vm:~$ ls -lat                                                       
total 96                                                                          
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 20:16 Desktop                             
drwxr-xr-x  3 ubuntu ubuntu 4096 Fev 19 20:07 Documents                           
-rw-------  1 ubuntu ubuntu  701 Fev 19 18:22 .bash_history                       
drwxr-xr-x 15 ubuntu ubuntu 4096 Fev 19 15:06 .                                   
drwx------ 11 ubuntu ubuntu 4096 Fev 19 13:55 .cache                              
-rw-------  1 ubuntu ubuntu  268 Fev 19 13:46 .xsession-errors                    
-rw-------  1 ubuntu ubuntu 1320 Fev 19 13:44 .ICEauthority                       
drwx------  3 ubuntu ubuntu 4096 Fev 19 13:44 .gnupg                              
-rw-------  1 ubuntu ubuntu   54 Fev 19 13:44 .Xauthority                         
-rw-------  1 ubuntu ubuntu 1734 Fev 19 13:24 .xsession-errors.old                
drwx------ 14 ubuntu ubuntu 4096 Fev 19 12:43 .config                             
drwx------  3 ubuntu ubuntu 4096 Fev 19 11:48 .local                              
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Downloads                           
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Music                               
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Pictures                            
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Public                              
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Templates                           
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Videos                              
-rw-r--r--  1 ubuntu ubuntu   25 Fev 19 11:48 .dmrc                               
drwx------  2 ubuntu ubuntu 4096 Fev 19 11:47 .gconf                              
-rw-r--r--  1 root   root      0 Fev 19 11:45 .sudo_as_admin_successful           
-rw-r--r--  1 ubuntu ubuntu  220 Fev 19 11:43 .bash_logout                        
-rw-r--r--  1 ubuntu ubuntu 3771 Fev 19 11:43 .bashrc                             
-rw-r--r--  1 ubuntu ubuntu  655 Fev 19 11:43 .profile                            
drwxr-xr-x  3 root   root   4096 Fev 19 11:43 ..                                  
ubuntu@ubuntu-vm:~$ ls -latr                                                      
total 96                                                                          
drwxr-xr-x  3 root   root   4096 Fev 19 11:43 ..                                  
-rw-r--r--  1 ubuntu ubuntu  655 Fev 19 11:43 .profile                            
-rw-r--r--  1 ubuntu ubuntu 3771 Fev 19 11:43 .bashrc                             
-rw-r--r--  1 ubuntu ubuntu  220 Fev 19 11:43 .bash_logout                        
-rw-r--r--  1 root   root      0 Fev 19 11:45 .sudo_as_admin_successful           
drwx------  2 ubuntu ubuntu 4096 Fev 19 11:47 .gconf                              
-rw-r--r--  1 ubuntu ubuntu   25 Fev 19 11:48 .dmrc                               
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Videos                              
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Templates                           
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Public                              
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Pictures                            
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Music                               
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 11:48 Downloads                           
drwx------  3 ubuntu ubuntu 4096 Fev 19 11:48 .local                              
drwx------ 14 ubuntu ubuntu 4096 Fev 19 12:43 .config                             
-rw-------  1 ubuntu ubuntu 1734 Fev 19 13:24 .xsession-errors.old                
-rw-------  1 ubuntu ubuntu   54 Fev 19 13:44 .Xauthority                         
drwx------  3 ubuntu ubuntu 4096 Fev 19 13:44 .gnupg                              
-rw-------  1 ubuntu ubuntu 1320 Fev 19 13:44 .ICEauthority                       
-rw-------  1 ubuntu ubuntu  268 Fev 19 13:46 .xsession-errors                    
drwx------ 11 ubuntu ubuntu 4096 Fev 19 13:55 .cache                              
drwxr-xr-x 15 ubuntu ubuntu 4096 Fev 19 15:06 .                                   
-rw-------  1 ubuntu ubuntu  701 Fev 19 18:22 .bash_history                       
drwxr-xr-x  3 ubuntu ubuntu 4096 Fev 19 20:07 Documents                           
drwxr-xr-x  2 ubuntu ubuntu 4096 Fev 19 20:16 Desktop                             
```

### The **tree** command

* **ls -R**: Recursive **ls**
```
ubuntu@ubuntu-vm:~$ ls -R                                                 
.:                                                                        
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos 
                                                                          
./Desktop:                                                                
file.txt                                                                  
                                                                          
./Documents:                                                              
my-directory                                                              
                                                                          
./Documents/my-directory:                                                 
my-file.txt                                                               
                                                                          
./Downloads:                                                              
                                                                          
./Music:                                                                  
                                                                          
./Pictures:                                                               
                                                                          
./Public:                                                                 
                                                                          
./Templates:                                                              
                                                                          
./Videos:                                                                 
```

* Similar to **ls -R** but creates visual output
	* **tree -d**: List directories only
	* **tree -C**: Colorize output

```
ubuntu@ubuntu-vm:~$ tree
.
├── Desktop
│   └── file.txt
├── Documents
│   └── my-directory
│       └── my-file.txt
├── Downloads
├── Music
├── Pictures
├── Public
├── Templates
└── Videos

9 directories, 2 files

ubuntu@ubuntu-vm:~$ tree -d
.
├── Desktop
├── Documents
│   └── my-directory
├── Downloads
├── Music
├── Pictures
├── Public
├── Templates
└── Videos

9 directories

ubuntu@ubuntu-vm:~$ tree -C
.
├── Desktop
│   └── file.txt
├── Documents
│   └── my-directory
│       └── my-file.txt
├── Downloads
├── Music
├── Pictures
├── Public
├── Templates
└── Videos

9 directories, 2 files
```

### List Directories, Not Contents

* **ls -d**: List directory name, not contents

```
ubuntu@ubuntu-vm:~$ ls -d Music/
Music/
```

### Listing Files with Color

* **ls --color**: Colorizr the output
	* Directories are blue

```
ubuntu@ubuntu-vm:~$ ls --color -F
Desktop/    Downloads/  my-data.data  Public/     Videos/
Documents/  Music/      Pictures/     Templates/
```

## Working with Spaces in Names

* Just say no to spaces!
* Alternatives:
	* **-**: Hyphens
	* **_**: Underscores
	* CamelCase

```
ubuntu@ubuntu-vm:~$ mkdir my-directory
ubuntu@ubuntu-vm:~$ cd my-directory
```

* Encapsulate the entire file name in quotes
* Use a backslash **(\\)** to escape spaces

### Summary

* Useful **ls** options
	* **-a**: List all files, including hidden files
	* **- -color**: List files with colorized output
	* **-d**: List directory names, not contents
	* **-l**: Use the long listing format
	* **-r**: Reverse the order
	* **-R**: List files recursively
	* **-t**: Sort by time, most recent first

* Symbolic links
* Hidden files and directories
* Spaces in file names

## 7. File and Directory Permissions Explained - Part One

### Permissions

```
ubuntu@ubuntu-vm:~/Documents/my-directory$ ls -ls
total 0
0 -rw-rw-r-- 1 ubuntu ubuntu 0 Fev 19 20:23 my-file.txt
```

| Symbol | Type |
| ------ | ---- |
| -      | Regular file|
| d      | Directory |
| &#124; | Symbolic link |
| r | read |
| w | write |
| x | execute |

### Permissions - Files vc Directories

| Permission | File | Directory |
| ---------- | ---- | --------- |
| Read (r) | Allows a file to be read| Allow a file names in the directory to be read|
|Write (w) | Allows a file to modified | Allows entries to be modified within the directory|
| Execute (x) | Allows the execution of a file | Allows access to contents and metadata for entries|

### Permission Categories

| Symbol | Category |
| ------ | -------- |
| u | User |
| g | Group |
| o | Other |
| a | All |

### Groups

* Every user is in at least on group
* User can belong to many groups
* Groups are used to organize users
* The **groups** command display a user's groups
* you can also use **id -Gn**

```
ubuntu@ubuntu-vm:~$ groups
ubuntu adm cdrom sudo dip plugdev lpadmin sambashare
ubuntu@ubuntu-vm:~$ id -Gn
ubuntu adm cdrom sudo dip plugdev lpadmin sambashare
```

### Secret Decoder Ring

* **-rw-rw-r-- 1 ubuntu ubuntu 0 Fev 19 20:23 my-file.txt**
	* **-**: File type
	* **rw-**: User permission
	* **r--**: Group permission
	* **r--**: Other Users permission

### Changing Permissions

| Item | Meaning |
| ---- | ------- |
| chmod | Change mode command |
| ugoa | User category user, group, toher, all |
| **+** **-** **+** | Add, subtract, or set permissions
| rwx | Read, Write, Execute |

```
ubuntu@ubuntu-vm:~$ ls -l my-data.data
-rw-r--r-- 1 ubuntu ubuntu 0 Fev 19 20:45 my-data.data

ubuntu@ubuntu-vm:~$ chmod g+w my-data.data
ubuntu@ubuntu-vm:~$ ls -l my-data.data
-rw-rw-r-- 1 ubuntu ubuntu 0 Fev 19 20:45 my-data.data

ubuntu@ubuntu-vm:~$ chmod g+wx my-data.data
ubuntu@ubuntu-vm:~$ ls -l my-data.data
-rw-rwxr-- 1 ubuntu ubuntu 0 Fev 19 20:45 my-data.data

ubuntu@ubuntu-vm:~$ chmod u+rwx,g-x my-data.data
ubuntu@ubuntu-vm:~$ ls -l my-data.data
-rwxrw-r-- 1 ubuntu ubuntu 0 Fev 19 20:45 my-data.data

ubuntu@ubuntu-vm:~$ chmod a=r my-data.data
ubuntu@ubuntu-vm:~$ ls -l my-data.data
-r--r--r-- 1 ubuntu ubuntu 0 Fev 19 20:45 my-data.data

ubuntu@ubuntu-vm:~$ chmod u=rwx,g=rx,o= my-data.data
ubuntu@ubuntu-vm:~$ ls -l my-data.data
-rwxr-x--- 1 ubuntu ubuntu 0 Fev 19 20:45 my-data.data
```

### Numeric Based Permissions

| r | w | x | - |
| - | - | - | - |
| 0 | 0 | 0 | Value for off |
| 1 | 1 | 1 | Binary value for on |
| 4 | 2 | 1 | base 10 value for on |

* Options:

| Octal | Binary | String | Description |
| ----- | ------ | ------ | ----------- |
| 0 | 0 | --- | No permissions |
| 1 | 1 | --x | Execute only |
| 2 | 10 | -w- | Write only |
| 3 | 11 | -wx- | Write and execute (2+1) |
| 4 | 100 | r-- | Read only |
| 5 | 101 | r-x | Read and execute (4+1) |
| 6 | 110 | rw- | Read and write (4+2) |
| 7 | 111 | rwx | Read, write, and execute (4+2+1) | 

### Order Has Meaning

| - | U | G | O |
| - | - | - | - |
| Symbolic | rwx | r-x | r-- |
| Binary | 111 | 101 | 100 |
| Decimal | 7 | 5 | 4 | 

### Commonly Used Permissions

| Symbolic | Octal |
| -------- | ----- |
| -rwx------| 700 |
| -rwxr-xr-x | 755 |
| -rw-rw-r-- | 664 |
| -rw-rw---- | 660 |
| -rw-r--r-- | 644 |

### 8 File and Directory Permissions Explained - Part Two

### Working with groups

* New files belong to your primary group
* The **chgrp** command changes the group

```
ubuntu@ubuntu-vm:~$ chgrp adm my-data.data
ubuntu@ubuntu-vm:~$ ls -l my-data.data
-rw-r--r-- 1 ubuntu adm 0 Fev 19 20:45 my-data.data

ubuntu@ubuntu-vm:~$ chmod g+w my-data.data
ubuntu@ubuntu-vm:~$ ls -l my-data.data
-rw-rw-r-- 1 ubuntu adm 0 Fev 19 20:45 my-data.data
```

### Directory Permissions Revisited

* Permissions on a directory can effect the files in the directory
* If the file permissions look correct, start checking directory permissions
* Work your way up to the root

### File Creation Mask
### The **umask** command
### Octal Substraction is an Estimation
### Common umask modes
Special Modes

* File creation mask determines default permissions
* If no mask were used permissions would be:
	* 777 for directories
	* 666 for files

### The **umask** command

```
$ umask [-S] [mode]
```

* Sets the file creation mask to mode, if given
* Use -S to for symbolic notation

| - | Directory | File |
| - | - | - |
| Base Permission | 777 | 666 |
| Subtract Umask | -022 | -022 |
| Creations Permission | 755 | 644 |

### Octal Substraction is an Estimation

| - | Directory | File |
| - | - | - |
| Base Permission | 777 | 666 |
| Subtract Umask | -007 | -007 |
| Creations Permission | 770 | 660* |

### Common umask modes

* 022
* 002
* 077
* 007

### Special Modes

* **umask 0022** is the same as **umask 022**
* **chmod 0644** is the same as **chmod 644**
* The special mode are:
	* setuid
	* setgid
	* sticky

```
ubuntu@ubuntu-vm:~/Documents/my-directory/testumask$ umask
0002

ubuntu@ubuntu-vm:~/Documents/my-directory/testumask$ umask -S
u=rwx,g=rwx,o=rx

ubuntu@ubuntu-vm:~/Documents/my-directory/testumask$ ls -l
total 4
drwxrwxr-x 2 ubuntu ubuntu 4096 Fev 19 22:29 a-dir
-rw-rw-r-- 1 ubuntu ubuntu    0 Fev 19 22:29 a-file

ubuntu@ubuntu-vm:~/Documents/my-directory/testumask$ umask 007
ubuntu@ubuntu-vm:~/Documents/my-directory/testumask$ umask -S
u=rwx,g=rwx,o=

ubuntu@ubuntu-vm:~/Documents/my-directory/testumask$ ls -l
total 4
drwxrwx--- 2 ubuntu ubuntu 4096 Fev 19 22:31 a-dir
-rw-rw---- 1 ubuntu ubuntu    0 Fev 19 22:31 a-file
```

### Summary

* Symbolic permission
* Numeric/octal permissions
* File versus directory permissions
* Changing permissions
* Working with groups
* File creation mask