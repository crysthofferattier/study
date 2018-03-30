# Web application security with python

## 12. Handling URLs using python - Part1 (Introduction to URL handling)

* Send HTTP requests to the target
* Parsing HTTP response
* Extract requests headers

```python
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import urllib2
>>> req = urllib2.urlopen("http://192.168.0.104/index.html")
>>> req.code
200
>>> req
<addinfourl at 139825605305552 whose fp = <socket._fileobject object at 0x7f2baf8ecb50>>
>>> req.read()
'<!DOCTYPE html>\n<html>\n<head>\n<title>Metasploitable</title>\n<head>\n<body>\n<h1>Hello World!<h1>\n<body>\n</html>\n'
>>>
```

## 13. Handling URLs using python - Part2 (Write a script to test php authentication)

#### auth.php

```php
<?php

$username = $_POST['username'];
$password = $_POST['password'];

if ($username == "askar" && $password == '123456') {
	echo "Login Success!"
} else {
	echo "Login Failed!"
}

?>
```

#### example5.py

## 14. Write python script to control a web shell