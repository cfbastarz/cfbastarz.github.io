---
title: Compilando LAPACK e BLAS com ifort
date: '2013-07-20 14:50:58'
tags:
- BLAS
- C
- Intel
- LAPACK
- Linux
- OS X
- Tudo
- Tutoriais
- Ubuntu
- fortran
- icc
- ifort
categories:
- Tudo
- Tutoriais
wordpress_id: 2138
original_url: https://craftmind.wordpress.com/2013/07/20/compilando-lapack-e-blas-com-ifort/
---

# Compilando LAPACK e BLAS com ifort

Este tutorial é muito simples e mostra como compilar as bibliotecas de Álgebra Linear [BLAS](http://www.netlib.org/blas/) e [LAPACK](http://www.netlib.org/lapack/index.html) do netlib (<http://www.netlib.org>) utilizando os compiladores C e fortran da Intel (icc e ifort).

Tanto para Linux (Ubuntu 11.04) quanto no OS X (Mountain Lion), os procedimentos são os mesmos:


```
$ wget -c http://www.netlib.org/lapack/lapack-3.4.2.tgz
$ tar -zxvf lapack-3.4.2.tgz
$ cd lapack-3.4.2
$ cp INSTALL/make.inc.ifort ./make.inc
$ make lapacklib
$ make blaslib
```


Como resultado da compilação, duas bibliotecas (libs) deverão ser criadas:

- liblapack.a
- librefblas.a

Dependendo da sua aplicação, pode ser necessário atribuir algum valor para a variável "LAPACK_PATH" indicando o caminho das libs que foram geradas. Se a compilação das libs foi feita em /home/user/lapack-3.4.2, então, pode-se fazer:


```
$ export LAPACK_PATH=/home/user/lapack-3.4.2
```


Este comando pode ser incluído no seu ~/.bashrc ou mesmo em /etc/bash.bashrc.

**Referência:**

- <http://idolinux.blogspot.com.br/2012/03/building-scalapack-with-lapack-blas-and.html>
