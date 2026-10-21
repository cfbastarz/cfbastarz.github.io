---
title: 'Erro: cannot open source file “asm/errno.h”'
date: '2011-01-25 17:18:40'
tags:
- C
- Ciência
- Compilação
- GCC
- Header
- Tudo
- Tutoriais
- fortran
- ifort
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 1120
original_url: https://craftmind.wordpress.com/2011/01/25/erro-cannot-open-source-file-%e2%80%9casmerrno-h%e2%80%9d/
---

# Erro: cannot open source file “asm/errno.h”

Se você está tentando compilar algum programa em linguagem C ou que precisa ler algum reader do sistema escrito em linguagem C e o compilador fortran da Intel (ifort) não consegue encontrar o header correto (no caso errno.h) e recebe o seguinte erro:


```
catastrophic error: cannot open source file "asm/errno.h"
```


Pode ser que você não tenha as bibliotecas extras do GCC instaladas por completo no seu sistema. Para resolver, basta instalar o pacote gcc-multilib:


```
$ sudo apt-get install gcc-multilib
```


Referência: <http://secure-software.intel.com/en-us/forums/showpost.php?p=149314>
