---
title: 'catastrophic error: cannot open source file "malloc.h"'
date: '2013-01-10 18:18:54'
tags:
- Mac OS X
- Tudo
- Tutoriais
- bacio.v1.3.c
- malloc.h
categories:
- Tudo
- Tutoriais
wordpress_id: 1923
original_url: https://craftmind.wordpress.com/2013/01/10/catastrophic-error-cannot-open-source-file-malloc-h/
---

# catastrophic error: cannot open source file &quot;malloc.h&quot;

Esse erro apareceu quando uma rotina que eu estava tentando compilar não conseguiu abrir o "malloc.h" (uma função para alocamento de memória) no OS X Mountain Lion:


```
bacio.v1.3.c(14): catastrophic error: cannot open source file "malloc.h"
  #include 
                     ^

compilation aborted for bacio.v1.3.c (code 4)
make[1]: *** [bacio.v1.3.o] Error 4
make: *** [linux] Error 2
```


Pesquisando na internet, encontrei que uma solução é modificar a rotina com um condicional, o qual funcionou perfeitamente para o meu caso. Basta fazer o seguinte: abra a rotina que está dando o problema (no meu caso, uma rotina chamada "bacio.v1.3.c"), localize a linha de include do "malloc".h e edite da seguinte forma:

**Forma original:**


```
#include
```


**Forma modificada:**


```
#if !defined(__APPLE__)
#include 
#endif
```


Fazendo isso, o header "malloc.h" poderá ser encontrado no Mac OS, que fica alocado em "/usr/include/sys".

É isso!

**Referências:**

- <http://code.google.com/p/gil-contributions/issues/attachmentText?id=9&aid=90001000&name=patch.diff&token=1K_Hd3RrRHPPTMORjKqmQni0iv8%3A1357837426761>
- <http://hintsforums.macworld.com/showthread.php?t=2023>
- <http://www.idevgames.com/forums/thread-3429.html>
