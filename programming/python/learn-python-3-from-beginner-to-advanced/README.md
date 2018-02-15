# The Complete Python 3 Course: Go from Beginner to Advance

## Setting Up Python On Your Computer

### Setting up Sublime Text to Build Python

* Python.sublime-build
```
{
   "cmd": ["C:\\Users\\Crysthoffer\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe", "-u", "$file"],
   "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*) ",
   "selector": "source.python"
}
```

## Introduction to your first program with Python, data types and variables

### Key words
```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### First Program in Python

* print()
```python
print('Hello world!')
```

### Data Types

* type()
```python
>>> type(2)
<class 'int'>
>>> type(2.2)
<class 'float'>
>>> type(2000000000)
<class 'int'>
>>> type(2000000000000000)
<class 'int'>
>>> type(2000000000000000000000000000)
<class 'int'>
>>> type(20000000000000000000000000000000000000000000000000000000000000000000000000000000)
<class 'int'>
>>> type(True)
<class 'bool'>
>>> type('a')
<class 'str'>
>>> type('aaaaaa')
<class 'str'>
>>>
```

### Variables

```python
>>> number = 2
>>> real = 2.2
>>> word = 'word'
>>> print(word)
word
>>> type(word)
<class 'str'>
>>> a = b = c = 1.5
>>> print(a)
1.5
>>> print(b)
1.5
>>> print(c)
1.5
>>> one, two, three = 1, 'two', 3.0
>>> print(one)
1
>>> print(two)
two
>>> print(three)
3.0
>>> number = 1
>>> str = 'string'
>>> number = str
>>> number
'string'
```

### Indentation

```python
def test():
	statement1
	statement2
	statement3

def test_2():
	statement1
	statement2
	statement3
```

### How to Clear Screen

```python
# Windows
>>> import os
>>> clear = lambda: os.system('cls')
>>> clear
```

## Comments in Python

### Single-line Comments
```python
print('We are now working with comments') # this is a comment
# comment
# comment

print('# We are now working with comments') # dont work
```

### Multi-line Comments
```python
'''
inside is a bunch od comments
comment1
comment2
comment3
	...
'''
```

## Expressions in Python

### Expressions in Python

```python
>>> print(2+5)
7
>>> print(2.2+5)
7.2
>>> print(2.2-5)
-2.8
>>> print(10-5)
5
>>> print(10.0-5)
5.0
>>> print(40*30)
1200
>>> print(40*30*0.5)
600.0
>>> # ^ = **
>>> print(2**5)
32
```

### Division Characteristics

```python
>>> print(2/4)
0.5
>>> print(23/5)
4.6
>>> print(23.0/5)
4.6
>>> print(23//5)
4
>>> print(23.0//5)
4.0
>>> print(25%4)
1
>>> print(25.0%4)
1.0
>>> a = 2 + 5
>>> b = 3.3 * 3
>>> c = 10.0/25
>>> print(a)
7
>>> print(b)
9.899999999999999
>>> print(c)
0.4
```

### Operator Precedence

* Order:
	- () : parentheses
	- ** : exponent
	- * : multiplication
	- / : division
	- % : modulo
	- +	: addition
	- -	: subtraction'

```python
>>> print(25*15+33/2.0)
391.5
>>> a = 25*15
>>> b = 33/2.0
>>> print(a+b)
391.5
```