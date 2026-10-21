---
title: 'Erro: cannot open source file "asm/param.h"'
date: '2011-09-06 10:46:53'
tags:
- Ciência
- Compilação
- Header
- MPICH2
- Tudo
- Tutoriais
- ifort
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 1252
original_url: https://craftmind.wordpress.com/2011/09/06/catastrophic-error-cannot-open-source-file-asmparam-h/
---

# Erro: cannot open source file &quot;asm/param.h&quot;

Quando fui compilar o MPICH2 no meu notebook, ao rodar o comando make, me deparei com a seguinte mensagem de erro:


```
/usr/include/linux/param.h(4): catastrophic error: cannot open source file "asm/param.h"
  #include <asm/param.h>
                        ^
```


Isso aconteceu porque a versão da **asm*** instalada no meu Ubuntu 11.04 não era a mesma que o MPICH2 estava procurando. Para resolver este problema, basta criar um link simbólico do **asm-generic** para o **asm**:


```
sudo ln -s /usr/include/asm-generic /usr/include/asm
```


Depois, basta rodar o cmando make novamente para recompilar o MPICH2.

***ASM:**

Procurando sobre o ASM, decobri que ele é um conjunto de funções geralmente escrito em linguagem Assembly (no linux utilizado em linguagem C) para facilitar a portabilidade do kernel para outros tipos de sistemas/plataformas.

Referências:

- <https://bugs.launchpad.net/ubuntu/+source/linux/+bug/778047>
- <http://stackoverflow.com/questions/3247770/what-is-the-linux-2-6-3x-x-include-asm-generic-for>
