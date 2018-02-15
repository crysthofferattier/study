# Code of conduct

## Caesar cipher

* [caesar-cipher.py](https://github.com/crysthofferattier/study/blob/master/security/criptografy/criptografia-0x65/code/caesar-cipher.py)

* Params
	- File: file containing the text to encode or decode
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

## Caesar cipher (brute force)

* [caesar-cipher-brute-force.py](https://github.com/crysthofferattier/study/blob/master/security/criptografy/criptografia-0x65/code/caesar-cipher-brute-force.py)

* Params
	- File: file containing the text to decode

* Usage
```
$ python caesar-cipher-brute-force.py [encode-text-file] > [result-file]
$ python caesar-cipher-brute-force.py files/encode-text > files/decode-text-brute-force
```

## Vigenère cipher

* [vigenere.py](https://github.com/crysthofferattier/study/blob/master/security/criptografy/criptografia-0x65/code/vigenere.py)

* Params
	- File: file containing the text to decode
	- Key: integer number
	- Mode:
		- enc: encode mode
		- dec: decode mode

* Usage
```
$ python vigenere.py [plain-text-file] [key] [function] > [result-file]
```

* Encode example:
```
$ python vigenere.py files/plain-text mypasswd enc > files/vig-encode-text
```

* Encode example:
```
$ python vigenere.py files/encode-text mypasswd dec > files/vig-decode-text
```