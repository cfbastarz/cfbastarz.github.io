---
title: Executando comandos remotamente dentro de uma rede linux com o SSH
date: '2011-02-25 17:44:34'
tags:
- Internet
- SSH
- Tudo
- Tutoriais
- comandos via SSH
categories:
- Internet
- Tudo
- Tutoriais
wordpress_id: 1135
original_url: https://craftmind.wordpress.com/2011/02/25/executando-comandos-remotamente-dentro-de-uma-rede-linux-com-o-ssh/
---

# Executando comandos remotamente dentro de uma rede linux com o SSH

Às vezes queremos executar um comando em uma máquina remota sem ter que logarmos nela. Isso é possível utilizando o SSH. O diferencial neste caso é que, ao invés de logarmos na máquina com o SSH, o utilizamos apenas para executar o comando desejado. Por exemplo:

Um login comum utilizando o SSH e dispondo de compressão (modificador C) e a parte gráfica (modificador X) e executando um comando em seguida:


```
ssh usuario@maquina -XC
$ comando
```


Agora o mesmo procedimento, mas sem a necessidade de login:


```
$ comando usuario@maquina:/pasta/desejada
```


Agora um exemplo real: Suponha que queiramos copiar um arquivo que está em na máquina local de um local para um outro local na maquina remota.


```
$ cd /pasta/local/desejada
$ scp arquivo usuario@maquina:/pasta/desejada
```


Uma outra situação seria aquela em que se deseja executar um programa gráfico em uma máquina que está dentro de uma rede diferente da sua e que por algum motivo, não se consegue obter display. Por exemplo, vamos partir da máquina 1 e executar o programa na máquina 3, sendo que as redes das máquinas 1 e 3 são diferentes (em outras palavras, as máquinas não se enxergam). Para isto, vamos precisar de uma segunda máquina, que nos sirva de ponte entre as máquinas 1 e 3:

SSH na máquina 1:


```
$ ssh usuario@maquina1 -XC
```


SSH na máquina 2:


```
$ ssh usuario@maquina2 -XC
```


SSH na máquina 3:


```
$ ssh usuario@maquina3 -XC
```


Execução do comando X (um comando qualquer que abra a parte gráfica, por exemplo o editor de textos nedit):


```
usuario@maquina3 $ nedit
Cannot open display.
```


Isso pode acontecer ou porque a variável DISPLAY não está ajustada corretamente. A variável DISPLAY permitirá, por exemplo, exportar o display da máquina 3 para a máquina 2 ou qualquer outra máquina que se tenha acesso e que consiga enxergar a máquina 3. Em outro caso em que o export do display da máquina 3 não funcionar (por algum motivo…), pode-se tentar executar o comando “nedit” (ou qualquer outro que abra a parte gráfica), via SSH:

SSH na máquina 1:


```
$ ssh usuario@maquina1 -XC
```


SSH na máquina 2:


```
$ ssh usuario@maquina2 -XC
```


Execução do comando “X” (que pode ser, por exemplo, o nedit) via SSH:


```
usuario@maquina2 $ ssh maquina3 "nedit"
```


Pimba, e de repente tudo funciona! O que acontece é que, quando se executa o comando “X” através do SSH, o display é automaticamente exportando para a máquina em que se executa o comando, no caso a máquina 2. Não é garantido que irá funcionar, mas para uma necessidade que tive funcionou. Tudo pode depender da topologia das redes e das permissões de acesso.
