---
title: Valor Máximo e Mínimo em um arquivo
date: '2011-12-16 12:22:02'
tags:
- Ciência
- Korn Shell
- Shell
- Tudo
- Tutoriais
- máximo e mínimo
- valor máximo
- valor mínimo
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 1333
original_url: https://craftmind.wordpress.com/2011/12/16/valor-maximo-e-minimo-em-um-arquivo/
---

# Valor Máximo e Mínimo em um arquivo

Esses dias estava precisando saber qual era o valor máximo e o mínimo dentro de um arquivo com centenas de números. Em Korn Shell, não há uma função reservada para fazer este tipo de verificação, então tive que procurar algum script que o fizesse. Acabei encontrando um por aí que não fazia exatamente o que eu queria, mas que comparava dois números inteiros. Dei uma modificada e acabei com isso aqui:

```bash
#! /bin/sh

#set -o xtrace

max=0

while read valor

do

val="$(echo ${valor})"

if [ ${val} -gt ${max} ]

then

max=${val}

fi

done < teste

min=${max}

while read valor

do

val="$(echo ${valor})"

if [ ${val} -lt ${min} ]

then

min=${val}

fi

done < teste

echo "valor maximo e ${max}" echo "valor minimo e ${min}"
```

Para testar, basta escrever alguns valores (um por linha) em um arquivo texto chamado teste e executar o script na mesma pasta ;)
