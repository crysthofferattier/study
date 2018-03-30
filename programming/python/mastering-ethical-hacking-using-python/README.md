# Offensive Python | Mastering Ethical Hacking Using Python

##### Course [link](https://www.udemy.com/offensive-python-mastering-ethical-hacking-using-python/)

## Section 02

### 4. Introduction to python sockets

##### [Python docs. Socket](https://docs.python.org/2/library/socket.html)

* What is python sockets?
* Where we can use it?
* How we can use it as security guys?

```php
root@kali:~# ./example1.py
```

### 5. Write customized port scanner in python

* We will use python sockets to build the scanner
* The scanner will be fully customized
* Perform simple banner grabbing

```php
root@kali:~# ./example2.py
```

### 6. Perform banner grabbing on open ports using netcat

> root@kali:~# nc -vv [host] [port]

```php
root@kali:~# nc -vv 192.168.0.104 22
Connection to 192.168.0.104 22 port [tcp/ssh] succeeded!
SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
```

### 7. Write python script to bypass traffic using SOCKS - TOR network (part 1)

#### The Theory

![traffic](https://preview.ibb.co/gUDSh7/image.png)

### 8. Write python script to bypass traffic using SOCKS - TOR network (part 2)

* Setup TOR on linux machine
* SOCKS library and how we an use it
* Live example about how we can change our identity

##### [http://api.ipify.org/](http://api.ipify.org/?format=text)

#### TOR
```php
root@kali:~# sudo apt install tor
```

#### PySocks

##### [PySocks Docs.](https://pypi.python.org/pypi/PySocks/1.6.7)

##### Install

```php
root@kali:~# pip install PySocks
```

* pip Install at [https://pip.pypa.io](https://pip.pypa.io/en/stable/installing/)

```php
root@kali:~# ./example3.py
```

### 10. Write python Jammer to jam wifi networks - Part1 (find all wifi networks)

* Find all the nearby wifi networks
* Set the wifi adapter to monitor mode
* Send the deauthentication packet to all networks

#### Packages

* wifi
* wireless
* scapy

```php
root@kali:~# sudo apt install python3-pip
root@kali:~# pip3 install wifi wireless scapy
```

```php
root@kali:~# ./example4.py
```