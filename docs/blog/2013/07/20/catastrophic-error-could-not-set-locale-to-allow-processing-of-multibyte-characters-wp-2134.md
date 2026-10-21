---
title: 'Catastrophic error: could not set locale "" to allow processing of multibyte
  characters'
date: '2013-07-20 11:18:12'
tags:
- C
- Compilação
- Intel
- LANG=en_US.UTF-8
- LC_ALL=en_US.UTF-8
- Tudo
- Tutoriais
- catastrophic error
- fortran
- icc
- ifort
categories:
- Tudo
- Tutoriais
wordpress_id: 2134
original_url: https://craftmind.wordpress.com/2013/07/20/catastrophic-error-could-not-set-locale-to-allow-processing-of-multibyte-characters/
---

# Catastrophic error: could not set locale &quot;&quot; to allow processing of multibyte characters

As mensagem de erro de compilação dos compiladores da Intel são bastante interessantes: "Catastrophic error...", ou "Erro catastrófico..." :)

Esse erro apareceu quando executei o comando "make" para compilar um código fonte em uma máquina Linux (Ubuntu 11.04) utilizando os compiladores da Intel (ifort/icc). Esse erro apareceu porque o Makefile não conseguiu determinar qual é o "idioma" do terminal, muito embora a variável "LANG" estivesse ajustada para "en_US.UTF-8" (LANG=en_US.UTF-8).

A solução foi ajustar mais uma variável de localização, a "LC_ALL" com o mesmo valor de "LANG", ou seja:


```
$ export LC_ALL=en_US.UTF-8
```


Você pode colocar no seu .bashrc ou ainda em /etc/bash.bashrc, e problema resolvido!

**Referência:**

- <http://software.intel.com/en-us/articles/cdiag912>
