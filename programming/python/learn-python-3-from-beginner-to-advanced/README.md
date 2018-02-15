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

print('# We are now working with comments')
```