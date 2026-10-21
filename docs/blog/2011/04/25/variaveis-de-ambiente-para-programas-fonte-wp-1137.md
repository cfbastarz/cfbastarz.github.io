---
title: Variáveis de ambiente para programas-fonte
date: '2011-04-25 17:46:20'
tags:
- C_INCLUDE_PATH
- LIBRARY_PATH
- MANPATH
- PATH
- PYTHONPATH
- Tudo
- Tutoriais
- Variáveis de ambiente
categories:
- Tudo
- Tutoriais
wordpress_id: 1137
original_url: https://craftmind.wordpress.com/2011/04/25/variaveis-de-ambiente-para-programas-fonte/
---

# Variáveis de ambiente para programas-fonte

Sempre que se instala um programa a partir do código-fonte, o próximo passo é configurar o PATH, ou seja, deve-se dizer ao sistema que há um novo programa disponível e que os seus executáveis estão em determinado local. Para isso, basta adicionar os executáveis à variável PATH, dentro do .bashrc (considerando-se que o shell padrão seja o Bash):


```
export PATH="/pasta/onde/estao/os/executaveis":${PATH}
```


Com isso já pode-se utilizar o novo programa, chamando-o a partir do terminal. Mas e se o programa possuir páginas de manuais, aquelas em que se digita “man comando” no terminal para consultar? Neste caso, a variável a ser incrementada é a MANPATH:


```
export MANPATH="/pasta/onde/estao/os/manuais":${MANPATH}
```


Em alguns outros casos, especialmente o de bibliotecas, é necessário informar ao sistema onde as bibliotecas se encontram, caso elas estejam fora do /usr/lib ou /lib. Deve-se, portanto, incrementar a variável LIBRARY_PATH:


```
export LIBRARY_PATH="/pasta/onde/estao/as/bibliotecas":${LIBRARY_PATH}
```


Da mesma forma, alguns programas possuem uma pasta chamada "include", que podem conter headers (ou cabeçalhos - "programas" necessários para a inicialização de um outro programa), e que são importantes para o sistema. Estes arquivos podem ser disponibilizados para o sistema através da variável C_INCLUDE_PATH:


```
export C_INCLUDE_PATH="/local/onde/se/encontra/a/pasta/include":${C_INCLUDE_PATH}
```


Se você programa em Python e quer utilizar algumas funções de dentro dos seus programas como se fossem programas ou funções do próprio shell, pode-se declarar a variável PYTHONPATH com o local onde estão os seus programas/scripts em Python:


```
export PYTHONPATH="/local/onde/estao/os/seus/programas/scripts/em/python"
```


É isso! Estas são as três principais variáveis de ambiente que podem ser incrementadas para se adicionar programas compilados a partir do código-fonte.
