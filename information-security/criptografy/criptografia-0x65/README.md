# Criptografia 0x65

## 01. Introduction to criptografy
 
### Introduction to Information Security

* NIST - National Institute Standards and Technology
	- Computer security: The protection offorded to an automated information system in order to attain the applicable objectives of preserving the intregrity, availability and confidentiality of information system resources (includes hardware, software, firmware, information/data and telecomunications).

* CIA
	- Intregrity
		- Data integrety: is a requirement that information and programs are changed only in a specified and authorized manner;
		- System integraty: is a requirement that a system performs its intended function in an unimpaired manner, free from deliberate or inadvertent unauthorized manipulation of the system.

	- Availability
		- The requirement intended to assure that system work promptly and service is not denied to authorized users.

	- Confidentiality
		- The requirement that private or confidential information not be disclosed to unauthorized individuals.

	- Extras
		- Authenticity and non-repudiation: guarantee that the information came from a reliable source; and guarantee that neither the sender nor the recipient denies sending/receiving a message.

### Criptografy

* Criptologia
	- Estudo de toda forma de escrita codificada
	- Cifras
	- Chaves
	- Algorítmos
	- Análise de cifras existentes
	- Formas de quebra de cifras

* Criptografy
	- Escrita codificada
	- Cifras
	- Chaves
	- Algoritmos
	- Cifrar x Decifrar

* Criptoanálise
	- Estudo das formas de se quebrar cifras
	- Força bruta
	- Análise de frequencia
	- Algortimos defeituosos

### Criptografia na antiguidade
* As necessidades
	- Conflitos
	- Alianças
	- Informações sigilosas

* Esteganografia
	- Mensagens ocultas
	- Esteganografia x Criptografia

* Criptografia
	- Mensagens visiveis
	- Mensagens incompreensíveis
	- Esteganografia x Criptografia

### As primeiras técnicas

* Substituição
	- Troca de caracteres
	- Uso de diversos símbolos
	- Uso de caracteres combinados

* Transposição
	- Embaralhamento dos caracteres
	- Uso dos mesmos símbolos

* Cifras monoalfabéticas
	- Cifra de César
		- Cifra de substituição
		- Deslocamento do alfabeto
		- Uso de chave para definir o deslocamento
		- ROT13
		- Análise de frequência x Cifra de César

![caesar-cipher](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Caesar3.svg/856px-Caesar3.svg.png)

* Scytale
	- Cifra de transposição
	- Cilindro criptográfico
	- A chave é o diâmetro do cilindro

![scytale](https://upload.wikimedia.org/wikipedia/commons/5/51/Skytale.png)

* Cifras polialfabéticas
	- Cifra de Vigenere
		- Uso de mais de um afalbeto no algoritmo
		- Uso de uma palavra secreta
		- rias cifras de César em uma mensagem
		- Tamanho da palavra secreta
		- Análise de frequência x Cfras polialfabeticas

![vigenere-square-shading](https://upload.wikimedia.org/wikipedia/commons/9/9a/Vigen%C3%A8re_square_shading.svg)

* Top Websites
	- [Cifra de César](https://cryptii.com/caesar-cipher)
	- [ROT13](http://www.rot13.com)
	- [Vigenere](https://cryptii.com/vigenere-cipher)

## 02. Conhecendo as cifras clássicas

### Entendendo a cifra de César

|  A |  B |  C |  D |  E |  F |  G |  H |  I |  J |  K |  L |  M | N  | O  | P  |  Q |  R |  S |  T |  U |  V |  W |  X | Y  |  Z |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |


* Key: 5
* Plaintext: CRIPTOGRAFIA

| - |    ENCODE   | - |
| - | ----------- | - |
| C | (02+5 = 07) | H |
| R | (17+5 = 22) | W |
| I | (08+5 = 13) | N |
| P | (15+5 = 20) | U |
| T | (19+5 = 24) | Y |
| O | (14+5 = 19) | T |
| G | (06+5 = 11) | L |
| R | (17+5 = 22) | W |
| A | (00+5 = 05) | F |
| F | (05+5 = 10) | K |
| I | (08+5 = 13) | N |
| A | (00+5 = 05) | F |

- Result: HWNUYTLWFKNF

| - |    DECODE   | - |
| - | ----------- | - |
| H | (07-5 = 02) | C |
| W | (22-5 = 17) | R |
| N | (13-5 = 08) | I |
| U | (20-5 = 05) | P |
| Y | (24-5 = 19) | T |
| T | (19-5 = 14) | O |

- Result: CRIPTO...

### Implementando a cifra de César usando Python
* [caesar-cipher.py](https://github.com/crysthofferattier/study/blob/master/security/criptografy/criptografia-0x65/code-of-conduct/caesar-cipher.py)

### Quebrando a cifra de César (brute force)
* [caesar-cipher-brute-force.py](https://github.com/crysthofferattier/study/blob/master/security/criptografy/criptografia-0x65/code-of-conduct/caesar-cipher-brute-force.py)

### Entendendo a cifra de Vigenère

|  A |  B |  C |  D |  E |  F |  G |  H |  I |  J |  K |  L |  M |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 |

| N  | O  | P  |  Q |  R |  S |  T |  U |  V |  W |  X | Y  |  Z |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

![vigenere-table](http://3.bp.blogspot.com/-I8bpzYFclxE/VkyfkPgFW5I/AAAAAAAAC6U/_t-wQVWLzfc/s1600/vigenere-table1.png)

* Key: senha
* Plaintext: CRIPTOGRAFIA

* Key and positions:

|  S |  E |  N |  H |  A |
| -- | -- | -- | -- | -- |
| 18 | 04 | 13 | 07 | 00 |


* Plaintext and positions:

|  C |  R |  I |  P |  T |  O |  G |  R |  A |  F |  I |  A |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| 02 | 17 | 08 | 15 | 19 | 14 | 06 | 17 | 00 | 05 | 08 | 00 |

* Application

|  S |  E |  N |  H |  A |  S |  E |  N |  H |  A |  S |  E |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
|  C |  R |  I |  P |  T |  O |  G |  R |  A |  F |  I |  A |


| C/S | 02+18=20 | U |
| - | --- | -  |
| R/E | 17+04=21 | V |
| I/N | 08+13=21 | V |
| P/H | 15+07=22 | W |
| T/A | 19+00=19 | T |
| O/S | 14+18=32 | G |
| G/E | 06+04=10 | K |
| R/N | 17+13=30 | E |
| A/H | 00+07=07 | H |
| F/A | 05+00=05 | F |
| I/S | 08+18=26 | A |
| A/E | 00+04=04 | E |

* Ciphertext: UVVWTGKEHFAE

### Implementando a cifra de Vigenère em Python

* [vigenere.py](https://github.com/crysthofferattier/study/blob/master/security/criptografy/criptografia-0x65/code-of-conduct/vigenere.py)

### Implementando uma análise de frequência

* [frequency-analysis.py](https://github.com/crysthofferattier/study/blob/master/security/criptografy/criptografia-0x65/code-of-conduct/frequency-analysis.py)

### Esquemas incondicionalmente e computacionalmente seguros

* XOR/OU Exclusivo
	- 0 + 0 = 0
	- 1 + 1 = 0
	- 1 + 0 = 1
	- 0 + 1 = 1

* Crifra de VERNAM
	- Chave secreta do mesmo tamanho do texto claro.
	- ci = pi XOR ki
	
	- |M|E|U|T|E|X|T|O|U|L|T|R|A|S|E|C|E|T|O| < Plaintext
	- |C|H|A|V|E|S|E|C|R|E|T|A|C|H|A|V|E|S|E| < Secret Key

* Esquema incondicionalmente seguro
	- Informação insuficiente no texto cifrado
	- O tempo disponível não importa

* ONE TIME PAD
	- Chave secreta aleatória
	- Chave secreta do mesmo tamanho do texto claro
	- Uso único da chave secreta
	- Nova mensagem, nova chave secreta
	- Esquema inquebrável, único que apresenta o *perfect secrecy*
	- Chave verdadeiramente aleatória
	- ci = pi XOR ki
	- Segurança totalmente dependente da aleatoriedade da chave secreta
	- Se a chave é verdadeiramente aleatória, então o texto cifrado também o será
	- O que impede qualquer tipo de análise, pois não há padrões ou regularidades
	- Criação de grandes quantidades de chaves aleatórias é um problema prático
	- Inviável em sistemas muito utilizados
	- Distribuição e proteção das chaves é um grande problema, pois para cada mensagem uma nova chave é utilizada

* Esquemas computacionalmente seguros
	- Custo para quebrar a cifra ultrapassa o valor da informação
	- O tempo exigido para a quebra ultrapassa o tempo de vida útil da informação

### Entendendo o XOR
	
|  XOR	| - |
| ----- | - |
| 1 + 1 | 0 |
| 0 + 0 | 0 |
| 1 + 0 | 1 |
| 0 + 1 | 1 |

* Example:
	- Lines:
		- Text (message)
		- Key (key)
		- Result (1+0=1; 0+1=1; 0+0=0, ...)

| ORGINAL | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 1 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| KEY | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| RESULT | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |

### XOR - Implementando a crifra de Vernam

* [vernam-cipher.py](https://github.com/crysthofferattier/study/blob/master/security/criptografy/criptografia-0x65/code-of-conduct/vernam-cipher.py)

##  03. Cifras modernas

### Criptografia simétrica

![public-key](http://nakamotoinstitute.org/static/img/mempool/crypto-anarchy-and-libertarian-entrepreneurship-2/public-key.jpg)

* Como funciona
	- Chave unica para cifrar e decifrar
	- Cifras de bloco
	- Cifras de fluxo

* Pontos fortes
	- Desempenho
	- Simplicidade

* Pontos fracos
	- Problema do compartilhamento de chave
	- Gerenciamento de grande quantidade de chaves
	- Inicio de comunicaçã segura entre desconhecidos

### Tipos de criptografia simétrica

* Cifras de bloco
	- Mensagem dividida em blocos de n bits
	- Cada bloco é tratado como um todo
	- Um bloco de texto cifrado do mesmo tamamnho é produzido para cada bloco de texto
	- Chaves normalmente de 64 ou 128 bits
	- Adequam-se a uma gama muito maior de aplicações
	- Aplicações de criptografia simetrica baseadas em rede
	- DES, 3DES, AES

* Cifras de fluxo
	- Opera em um bit por vez, continuamente
	- Chave inserida em um gerador de bits pseudoaleatorios
	- Produz um fluxo de numeros de 8 bits, fluxo de chaves
	- Operação XOR
	- Semelhante ao *one-time pad*
	- Aleatório x pseudoaleatório
	- Não se sabe o tamanho da informação
	- RC4 (SSL/TSL, WEP. WPA)