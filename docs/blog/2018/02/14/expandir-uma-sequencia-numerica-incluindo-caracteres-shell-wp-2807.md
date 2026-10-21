---
title: Expandir uma sequência numérica incluindo caracteres (Shell)
date: '2018-02-14 10:27:43'
tags:
- BASH
- Brace Expansion
- Shell
- Tudo
categories:
- Tudo
wordpress_id: 2807
original_url: https://craftmind.wordpress.com/2018/02/14/expandir-uma-sequencia-numerica-incluindo-caracteres-shell/
---

# Expandir uma sequência numérica incluindo caracteres (Shell)

Escrever sequências numéricas no Shell é fácil. Você pode utilizar o comando "seq" para escrever sequências numéricas, inclusive formatando a quantidade de dígitos. Por exemplo:

**1) Sequência de 1 a 5, com passo igual a 1:**


```
$ seq 1 5
 1
 2
 3
 4
 5
```


**2) Sequência de 1 a 5, com passo igual a 2:**


```
$ seq 1 2 5
 1
 3
 5
```


**3) Sequência de 1 a 5, com passo igual a 1, com dois dígitos:**


```
$ seq -f %02g 1 5
 01
 02
 03
 04
 05
```


E assim por diante. Neste último exemplo, se quiséssemos escrever o resultado da sequência com três dígitos, bastaria fazer "seq -f %03g 1 5", ou seja, basta alterar o modificador.

Mas, e se quiséssemos escrever uma sequência formatada com caracteres, como em "01N 02N 03N"? Neste caso, é mais fácil utilizar o comando de expansão "{..}". Por exemplo:

**4) Sequência de 1 a 5, com passo igual a 1:**


```
$ echo {1..5}
1 2 3 4 5
```


**5) Sequência de 1 a 5, com passo igual a 2:**


```
$ echo {1..5..2}
1 3 5
```


**6) Sequência de 1 a 5, compasso igual a 1, com dois dígitos:**


```
$ echo 0{1..5}
01 02 03 04 05
```


**7) Sequência de 1 a 5, com passo igual a 2, com três dígitos sendo o último, um carácter:**


```
$ echo 0{1..5..2}A
01A 03A 05A
```


Muito fácil, não é? Este tipo de estrutura de expansão faz parte do Bash e ele pode ser utilizado apenas com caracteres também. Em inglês, o termo é "Bash Brace Expansion". Experimente também o comando: "echo {a..z}".

É isso!

**Referências (e muito mais exemplos):**

- <http://www.linuxjournal.com/content/bash-brace-expansion>
- <http://wiki.bash-hackers.org/syntax/expansion/brace#increment>
