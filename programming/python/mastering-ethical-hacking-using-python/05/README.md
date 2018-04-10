# Encryption basics with python

## Encryption basics with python

### HASHLIB

```python
>>> import hashlib
>>> dir(hashlib)
['__all__', '__builtins__', '__doc__', '__file__', '__get_builtin_constructor', '__name__', '__package__', '_hashlib', 'algorithms', 'algorithms_available', 'algorithms_guaranteed', 'md5', 'new', 'pbkdf2_hmac', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
```

```python
>>> hashlib.algorithms_available
set(['SHA1', 'SHA224', 'SHA', 'SHA384', 'ecdsa-with-SHA1', 'SHA256', 'SHA512', 'md4', 'md5', 'sha1', 'dsaWithSHA', 'DSA-SHA', 'sha224', 'dsaEncryption', 'DSA', 'ripemd160', 'sha', 'MD5', 'MD4', 'sha384', 'sha256', 'sha512', 'RIPEMD160', 'whirlpool'])
```

```python
>>> hashlib.md5('ferrari').hexdigest()
'0911054d8ad47cc256400031197f3e97'

>>> def md5(string):
...     return  hashlib.md5(string).hexdigest()
... 
>>> md5('ferrari')
'0911054d8ad47cc256400031197f3e97'
>>> md5('ferrari') == ferrari_md5
True
```

```python
>>> hashlib.sha512('ferrari').hexdigest()
'5f5c8cbae2b9561015db0696e389697b64fb880d1b5a895709acdfecb43c081bd0432eb9a973a6d3b44428cb78ab12e41b189df9fdef48eec0cb70433622217f'
```

## 28. Write python script to generate rainbow tables - Part 2 (write the script)

##### rainbow_table.py

## 29. Write python script to generate rainbow tables - Part 3 (save the results)

##### rainbow_table.py

## 30. Write python script to calculate checksum

##### check_sum.py

## 31. Write secure python reverse shell with ssl

##### secure_shell.py