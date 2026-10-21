---
title: Um pouco sobre o comando xargs
date: '2011-03-25 17:25:45'
tags:
- Tudo
- Tutoriais
- xargs
categories:
- Tudo
- Tutoriais
wordpress_id: 1128
original_url: https://craftmind.wordpress.com/2011/03/25/um-pouco-sobre-o-comando-xargs/
---

# Um pouco sobre o comando xargs

O comando xargs é bastante útil quando se quer repetir um comando várias vezes. Por exemplo, suponha que se queira encontrar todos os links simbólicos a partir de uma determinada pasta e apagá-los. O comando “find . -type l” procura pelos links (em bash) e os retorna toda na tela. Para apagar todos de uma vez, à medida em que eles são encontrados, basta digitar:


```
$ find . -type l | xargs rm -rf
```


Neste caso, o xargs recebe como entrada a saída do comando find e replica o comando rm para cada item encontrado. Fácil, mas tome cuidade com ele!
