# Conceitos

## O que é dokcer

É uma ferramenta que se apoia em recursos existentes no kernel, inicialmente Linux, para isolar
a execução de processos. As ferramentas que o Docker traz são basicamente uma camada de
administração de containers, baseado originalmente no LXC.

## O que são containers?

Container é o nome dado para a segregação de processos no mesmo kernel, de forma que o processo
seja isolado o máximo possível de todo o resto do ambiente.
Em termos práticos são File Systems, criados a partir de uma "imagem" e que podem possuir
também algumas características próprias.

## O que são imagens Docker ?
Uma imagem Docker é a materialização de um modelo de um sistema de arquivos, modelo este
produzido através de um processo chamado build.
Esta imagem é representada por um ou mais arquivos e pode ser armazenada em um repositório.
Docker File Systems
O Docker utiliza file systems especiais para otimizar o uso, transferência e armazenamento
das imagens, containers e volumes.
O principal é o [AUFS](#https://pt.wikipedia.org/wiki/Aufs), que armazena os dados em camadas sobrepostas, e somente a camada
mais recente é gravável.

[Docker aufs-driver](#https://docs.docker.com/engine/userguide/storagedriver/aufs-driver/)