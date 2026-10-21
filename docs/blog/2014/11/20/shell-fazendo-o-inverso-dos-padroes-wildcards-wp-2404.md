---
title: 'Shell: fazendo o inverso dos padrões (wildcards)'
date: '2014-11-20 01:57:24'
tags:
- Shell
- Tudo
- Tutoriais
- wildcars
categories:
- Tudo
- Tutoriais
wordpress_id: 2404
original_url: https://craftmind.wordpress.com/2014/11/20/shell-fazendo-o-inverso-dos-padroes-wildcards/
---

# Shell: fazendo o inverso dos padrões (wildcards)

Essa dica é simples, mas é aquela que você sempre quis saber. Se você sempre soube dela, parabéns, você aprendeu o Shell direito. Ou não :)

Suponha que você queira listar (ou copiar, mover, apagar etc) todos os arquivos de uma pasta, cujos nomes NÃO contenham um determinado padrão.



Fazer isto considerando o padrão, é trivial. Por exemplo:


```
$ ls *2014*
```


O comando acima, lista todos os arquivos que possuam o padrão “2014” no nome. Pela lógica, para fazer o inverso - ou melhor, o contrário disso, poderíamos utilizar um comando como o seguinte, de forma a recuperar todos os arquivos que NÃO contenham o padrão “2014” no nome:


```
$ ls !(*2014*)
```


E o resultado desse comando, deveria ser uma lista com todos os arquivos que não contenham o padrão “2014” no nome. Mas isso, a princípio, não funciona no Shell padrão. Eu disse a princípio, porque na verdade, ele funciona!

Para que esta função do Shell seja habilitada, você deve executar o seguinte comando para poder usar o operador lógico “!” (negação) e então inverter a lógica dos wildcards:


```
$ shopt -s extglob
```


Com isso, o comando "ls !(*2014*)” deve funcionar e você será capaz de listar todos os arquivos que não contenham o padrão "2014" no nome!

O comando "shopt" permite que algumas extensões do Shell sejam habilitadas e, neste caso em específico, o modificador "-s" indica a habilitação da função "extglob" estendendo as o funções de busca através de padrões (wildcards). Mas conhecer as outras opções do comando "shopt", basta digitar "man shopt" ou simplesmente "shopt" para saber quais opções estão habilitadas no seu Shell.

**Referência:**

- <http://stackoverflow.com/questions/216995/how-can-i-use-inverse-or-negative-wildcards-when-pattern-matching-in-a-unix-linu>
