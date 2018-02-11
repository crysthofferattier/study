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

## Conhecendo as cifras clássicas

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
* [caesar-cipher.py](https://github.com/crysthofferattier/study/blob/master/security/criptografy/criptografia-0x65/code/caesar-cipher.py)