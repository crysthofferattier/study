# Uso basico do Docker

## 1. Introdução ao Docker Client

## 2. Hello World Meu Docker funciona!

* Command:

```
ubt-docker@ubuntu-vm:~$ sudo docker container run hello-world
```

* Output:
```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete
Digest: sha256:083de497cff944f969d8499ab94f07134c50bcf5e6b9559b27182d3fa
80ce3f7
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub. (amd64)
 3. The Docker daemon created a new container from that image which runs the executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

### Meu querido amigo run

```
ubt-docker@ubuntu-vm:~$ sudo docker container run hello-world
```

### Ferramentas diferentes

* Verificando diferença entre ferramentas

	* Teste da versão do **bash**:
		Verificando a versão do **bash** e comparar com uma imagem Debian, apra ter a certeza de que o docker esta executando a imagem.

		```
		ubt-docker@ubuntu-vm:~$ bash --version

		GNU bash, version 4.3.48(1)-release (x86_64-pc-linux-gnu)
		Copyright (C) 2013 Free Software Foundation, Inc.
		License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
		This is free software; you are free to change and redistribute it.
		There is NO WARRANTY, to the extent permitted by law.
		```

		* Run Debian:

		```
		ubt-docker@ubuntu-vm:~$ sudo docker container run debian bash --version

		GNU bash, version 4.3.48(1)-release (x86_64-pc-linux-gnu)
		Copyright (C) 2013 Free Software Foundation, Inc.
		License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
		This is free software; you are free to change and redistribute it.
		There is NO WARRANTY, to the extent permitted by law.
		```

* Verificando container executados:

	* **docker container ps**: Lista container em execução
	```
	ubt-docker@ubuntu-vm:~$ sudo docker container ps
	CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
	```


	* **docker container ps -a**: Log de execução
	```
	ubt-docker@ubuntu-vm:~$ sudo docker container ps -a
	CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
	9f5f54aa5c78        debian              "bash --version"    5 minutes ago       Exited (0) 5 minutes ago                        serene_colden
	dd50302f2b02        debian              "bash --version"    5 minutes ago       Exited (0) 5 minutes ago                        silly_wilson
	8d184725b9e0        debian              "bash --version"    7 minutes ago       Exited (0) 7 minutes ago                        pensive_euler
	a7c63b1d4957        debian              "bash --version"    7 minutes ago       Exited (0) 7 minutes ago                        kind_pare
	9759e1d96822        hello-world         "/hello"            25 minutes ago      Exited (0) 25 minutes ago                       gallant_beaver
	274bc519bbdf        hello-world         "/hello"            32 minutes ago      Exited (0) 32 minutes ago                       fervent_mcnulty
	```

	* **docker container run --rm [args]**: Remove container da lista (mencionada acima), após a execução
	```
	ubt-docker@ubuntu-vm:~$ sudo docker container run --rm debian bash --version
	CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
	9f5f54aa5c78        debian              "bash --version"    5 minutes ago       Exited (0) 5 minutes ago                        serene_colden
	dd50302f2b02        debian              "bash --version"    5 minutes ago       Exited (0) 5 minutes ago                        silly_wilson
	8d184725b9e0        debian              "bash --version"    7 minutes ago       Exited (0) 7 minutes ago                        pensive_euler
	a7c63b1d4957        debian              "bash --version"    7 minutes ago       Exited (0) 7 minutes ago                        kind_pare
	9759e1d96822        hello-world         "/hello"            25 minutes ago      Exited (0) 25 minutes ago                       gallant_beaver
	274bc519bbdf        hello-world         "/hello"            32 minutes ago      Exited (0) 32 minutes ago                       fervent_mcnulty
	```

### **Run** cria sempre novos containers

### Containers devem ter nomes únicos