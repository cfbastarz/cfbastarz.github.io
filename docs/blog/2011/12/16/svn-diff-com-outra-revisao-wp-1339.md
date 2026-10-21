---
title: svn diff com outra revisão
date: '2011-12-16 12:36:47'
tags:
- Internet
- SVN
- Tudo
- Tutoriais
- diff
- patch
- revisão
- svn diff
categories:
- Internet
- Tudo
- Tutoriais
wordpress_id: 1339
original_url: https://craftmind.wordpress.com/2011/12/16/svn-diff-com-outra-revisao/
---

# svn diff com outra revisão

Esta é uma dica rápida:

Se você quiser criar um patch das modificações da sua cópia local em relação à uma revisão anterior qualquer, basta utilizar o modificador "-r#", sendo que # representa um número de revisão.

Exemplo:


```
$ svn info
...
Revision: 247
...
$ svn diff -r220 > $HOME/teste.patch
```


Depois, caso queira aplicar um patch na revisão 220, basta fazer um checkout e aplicar da seguinte forma:


```
$ svn co -r220 http://... TESTE
$ cd TESTE
$ svn info
...
Revision: 220
...
$ patch -p0 -i $HOME/teste.patch
```


É isso!
