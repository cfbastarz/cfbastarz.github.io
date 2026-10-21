---
title: svn merge (jeito simples)
date: '2012-01-17 17:54:07'
tags:
- Internet
- SVN
- Subversion
- Tudo
- Tutoriais
- merge
categories:
- Internet
- Tudo
- Tutoriais
wordpress_id: 1453
original_url: https://craftmind.wordpress.com/2012/01/17/svn-merge-jeito-simples/
---

# svn merge (jeito simples)

Fazer um merge pode ser um pouco tenso para algumas pessoas, principalmente quando não se entende bem a lógica do merge no SVN. Na verdade, esse procedimento pode ser bem simples (pare, respire, tome um cafezinho e volte a fazer) ou bem complicado (se você não parar, respirar um pouco e sair para tomar um cafezinho). Sem mais enrolação, aqui vai um jeito bem simples e objetivo de fazer um merge entre dois ramos SVN. Primeiro, vamos desenhar uma situação: temos um ramo trunk (o principal) e um ramo branch (em que estamos trabalhando). Vamos trazer os últimos desenvolvimentos do ramo trunk para dentro do ramo branch, sem perder as nossas implementações (no ramo branch). Queremos que o svn merge apenas traga as atualizações que recebem para dentro do nosso branch.

Para isso, siga os passos seguintes:

**1. Checkout do seu branch para a sua área de trabalho:**


```
$ svn co https://endereco.alguma.coisa/projeto/branch/pasta pasta.branch
```


No comando acima, iremos criar uma nova pasta de nome "pasta" que contém todo o código que queremos atualizar a partir do trunk, utilizando o comando merge.

**2. Entre na "pasta" criada e execute o comando svn merge como indicado:**


```
$ cd pasta.branch/
$ svn merge https://endereco.alguma.coisa/projeto/trunk/pasta .
```


Observe bem que no final do comando svn merge, foi colocado um ponto ".", que representa a pasta atual (pasta.branch) onde está o código do nosso branch, para o qual queremos trazer as atualizações contidas no ramo trunk do projeto.

Depois de algumas tentativas mais complicadas, essa foi a mais simples e que deu certo.

Pode ser que no seu caso essa solução não funcione como esperado, porque tudo depende de como você está trabalhando com o seu projeto no svn. É importante também ressaltar que, no exemplo dado acima, o ramos trunk contém o código mais atualizado e que, apenas alguma parte do código do ramo branch não existe no ramo trunk, ou seja, nossas criações no branch ainda não foram adicionadas ao trunk e tudo o queríamos eram apenas as últimas alterações do trunk, da parte do código em que não alteramos.
