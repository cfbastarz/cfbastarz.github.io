---
title: 'Erro: no such instruction: `vzeroupper'' do PGF90 12.8-1'
date: '2012-08-24 03:15:41'
tags:
- AVX
- Ciência
- Intel
- IvyBridge
- PGI
- SandyBridge
- Tudo
- Tutoriais
- fortran
- pgf90
- vzeroupper
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 1766
original_url: https://craftmind.wordpress.com/2012/08/24/erro-no-such-instruction-vzeroupper-do-pgf90-12-8-1/
---

# Erro: no such instruction: `vzeroupper&#x27; do PGF90 12.8-1

Recentemente instalei a versão trial do compilador fortran do Portland Group (PGI) para compilar um pacote. No primeiro teste (com um programa Hello World), ocorreu o seguinte erro:


```
$ pgf90 teste.f90
NOTE: your trial license will expire in 14 days, 0.939 hours.
NOTE: your trial license will expire in 14 days, 0.939 hours.
teste.f90:74:no such instruction: `vzeroupper'
teste.f90:83:no such instruction: `vzeroupper'
teste.f90:90:no such instruction: `vzeroupper'
teste.f90:97:no such instruction: `vzeroupper'
teste.f90:101:no such instruction: `vzeroupper'
teste.f90:107:no such instruction: `vzeroupper'
teste.f90:234:no such instruction: `vzeroupper'
```


O que é muito estranho, pois o programa hello world contém apenas uma instrução para imprimir uma linha na tela. Dando uma olhada aqui e alí, encontrei a solução [aqui](http://www.pgroup.com/userforum/viewtopic.php?t=2794&sid=3fb09a8305d263e7694c5c20887035b8), e a sugestão foi acrescentar a opção  "-tp=nehalem-64" na compilação:


```
$ pgf90 -tp=nehalem-64 teste.f90
NOTE: your trial license will expire in 14 days, 0.901 hours.
NOTE: your trial license will expire in 14 days, 0.901 hours.
```


Ou seja, o "a.out" (programa compilado) foi criado e funciona sem problemas. Este problema pode afetar máquinas Linux ou Mac OS X com processador Intel, especialmente com o chip SandyBridge. Meu Macbook Pro é de 2011 e tem processador Intel com chip Sandybridge e a Apple não atualizou (ainda...) o Xcode (que fornece acesso a algumas instruções básicas do processador) para suportar as instruções AVX presentes a partir dos chips SandyBridge (o que é ridículo, pois já temos os novos chips IvyBridge...). Então, esta solução força o compilador a interpretar o chip como um modelo mais antigo, ou mais ou menos isso :)

**Referência:**
<http://www.pgroup.com/userforum/viewtopic.php?t=2794&sid=3fb09a8305d263e7694c5c20887035b8>
