# Endpoint security with python

## 16. Introduction to python shells

* Executing commands on the remote machine
* Controlling systems
* Escalate privileges

### Shell types

* Reverse Shell
* Bind Shell

#### Reverse Shell

![reverse-shell](https://preview.ibb.co/mdLcZn/image.png)

#### Bind Shell

![bind-shell](https://preview.ibb.co/kTOLn7/image.png)

## 17. Write python reverse shell (Linux platform)

##### example8.py

## 18. Write python rootkit for Linux to invoke hidden reverse shell

##### rootkit.py

## 19. Write python reverse shell (Windows platform)

##### example8_2.py

## 20. Write python bind shell

##### example9.py

##### [socket.bind(address)](https://docs.python.org/2/library/socket.html#socket.socket.bind)

##### [socket.listen(backlog)](https://docs.python.org/2/library/socket.html#socket.socket.listen)

##### [sock.accept()](https://docs.python.org/2/library/socket.html#socket.socket.accept)

![bind-shell](https://preview.ibb.co/kTOLn7/image.png)

## 21. Protect your shell with password

##### example9_2.py

## 22. Using pyinstaller to create win32 executable file

##### [pyinstaller.org](http://www.pyinstaller.org/)

### PyInstaller Quickstart

Install PyInstaller from PyPI:
```
pip install pyinstaller
```

Go to your program’s directory and run:
```
pyinstaller yourprogram.py
```

This will generate the bundle in a subdirectory called dist.
For a more detailed walkthrough, see the [manual](https://pyinstaller.readthedocs.io/).

#### Arguments

* --onefile: generate exec file (dll, dependencies, manifest, etc) in one file
* --windowed: generate very simple exe whithout popup.
```
pyinstaller.exe reverseshell-windows.py --onefile --windowed
```

## 23. Using pyinstaller to create ELF executable file (Linux)

```
pyinstaller reverseshell.py --onefile --windowed
```

## 24. Using py2exe to create win32 executable file

##### [py2exe.org](http://py2exe.org/)

### Downlaod

##### [py2exe Versions](https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/)
##### [py2exe-0.6.9.win32-py2.7.exe](https://ufpr.dl.sourceforge.net/project/py2exe/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe)

### Usage

* Configuration file: convert.py

```python
from distutils.core import setup
import py2exe

setup (
	options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
	windows = [ReverseShell.py],
	zipfile = None)
```

* Convert

```
convert.py py2exe
```

## 25. Bypass Anti­Virus using Pyinstaller and py2exe (demo)

##### [virustotal.com](https://www.virustotal.com/#/home/upload)

## 26. Write python script to execute commands without saving the commands

