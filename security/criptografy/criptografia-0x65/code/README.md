# Code of conduct

## Caesar cipher

* [caesar-cipher.py](https://github.com/crysthofferattier/study/blob/master/security/criptografy/criptografia-0x65/code/caesar-cipher.py)

* Params
	- Key: integer number
	- Function:
		- enc: encode mode
		- dec: decode mode

* Usage
```
$ python caesar-cipher.py [plain-text-file] [key] [function] > [result-file]
```

* Encode example:
```
$ python caesar-cipher.py files/plain-text 7 enc > files/encode-text
```

* Encode example:
```
$ python caesar-cipher.py files/encode-text 7 dec > files/decode-text
```