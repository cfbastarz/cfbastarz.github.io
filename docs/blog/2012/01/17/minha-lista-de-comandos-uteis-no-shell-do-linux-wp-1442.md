---
title: Minha lista de comandos úteis no shell do linux
date: '2012-01-17 08:21:06'
tags:
- Ciência
- Linux
- Shell
- Tudo
- Tutoriais
- awk
- comando
- ksh
- sed
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 1442
original_url: https://craftmind.wordpress.com/2012/01/17/minha-lista-de-comandos-uteis-no-shell-do-linux/
---

# Minha lista de comandos úteis no shell do linux

Depois de algum tempo fazendo scripts e tentando lançar uma solução aqui e ali, montei uma lista de alguns comando do shell do linux que me quebram uma galhão. Espero que lhe ajude também! Só para melhorar a diagramação dos comando, coloquei alguns "\n" para quebrar a linha, mas você suprimir esta parte e colocar tudo em uma linha só:

**1. Operações de busca com o comando find**


```
$ find <diretorio> -name ""
```


**Exemplos:**
**1.1 Procurar arquivos com o nome "run" na pasta atual em diante**


```
 $ find . -name "run" 
```


**1.2 Procurar arquivo com a extensão ".ksh" na pasta /etc**


```
 $ find /etc -name "*.ksh" 
```


**1.3 Procurar por links simbólicos na pasta atual em diante**


```
 $ find . type -l 
```


**1.4 Procurar por links simbólicos na pasta atual em diante, com saída formatada (indicando a origem e o destino do link)**


```
 $ find . -type l -printf "%p -> %l\n" 
```


**1.5 Apagar todos os links simbólicos encontrados utilizando o comando xargs**


```
 $ find . -type l | xargs rm -rf 
```


**1.6 Procurar todos os arquivos de nome "monitor.t" em pastas com nome sequencial formatado de "001" a "040", na pasta atual**


```
 $ for pasta in $(seq -f "%03g" 1 40); do echo $pasta; cd $pasta; \n 
 if test ! -e monitor.t; then echo ">>> $pasta falhou"; fi; cd -; done 
```


**2. Operações de pesquisa em arquivos com o comando grep**


```
$ grep <opcoes> <expressao> <arquivo(s)>
```


**Exemplos:**
**2.1 Pesquisa recursiva pela expressão "letkf" em todos os scripts ksh na pasta atual em diante**


```
 $ grep -R "letkf" *.ksh 
```


**2.2 Pesquisa recursiva pela exporessão "letkf" ou "LETKF" (ou uma mistura de maiúsculas/minúsculas) em todos os scripts ksh na pasta atual em diante**


```
 $ grep -iR "letkf" *.ksh 
```


**3. Operações com arquivos utilizando o comando awk**


```
 $ awk <opcoes> <comandos> <arquivo>
```


ou


```
 $ cat <arquivo> | awk <opcoes> <comandos>
```


**Exemplos:**
**3.1 Filtrando um arquivo com colunas separadas por espaços, mostrando apenas a coluna "n"**


```
 $ cat <arquivo> | awk -F " " '{print $n}'
```


**4. Operações com arquivos utilizando o comando sed**


```
 $ sed <opcoes> <comandos> <arquivo(s)>
```


ou


```
 $ cat <arqvuivo> | sed <opcoes> <comandos>
```


**Exemplos:**
**4.1 Substituindo todas as ocorrências da string "A" pela string "B" em todos os scripts .ksh (apenas na pasta atual)**


```
 $ sed -i "s,A,B,g" *.ksh 
```


**4.2 Comentando a linha "n" em um arquivo (comentário é dados por #)**


```
 $ sed -i 'ns/^/#/' 
```


**4.3 Inserindo um comentário na primeira linha de um arquivo**


```
 $ sed -i "1s/^/# Comentario/" > 
```


**5. Criando uma sequência de números no shell com o comando seq**


```
 $(seq <inicio> <fim>)
```


**Exemplos:**
**5.1 Imprimir no shell a sequencia de 1 a 20**


```
 $ echo $(seq 1 20) 
```


**6. Operações com loops no shell:**
**Comando for; do; done**
**Exemplos:**
**6.1 Imprimir a sequência de 1 a 30 utilizando o comando de laço for**


```
 $ for i in $(seq 1 30); do echo $i; done 
```


**6.2 Renomear todos os arquivos com extensão .txt adicionando uma nova extensão .dat**


```
 $ for i in `find . -name *.txt`; do mv ${i} ${i}.dat; done 
```


**6.3 Alterar todos os arquivos com a extensão .TQ0213L042 para .T213L42, utilizando o for e o sed**


```
 $ for arq1 in `ls *.TQ0213L042`; do arq2=`echo ${arq1} | sed "s,TQ0213L042,T213L42,g"`; \n 
 cp ${arq1} ${arq2}; done 
```


**Comando until; do; done**
**Exemplos:**
**6.4 Aguardar até que um arquivo esteja disponível**


```
 $ until [ -e <arquivo> ]; do sleep .1s; done
```


**Comando if; then; fi**
**Exemplos:**
**6.5 Verifica se uma pasta existe; se não existir, cria, se existir sai do teste**


```
 $ if test ! -s <pasta>; then mkdir -p <pasta>; fi
```


**6.6 Lê um lista chamada "lista" com os nomes das pastas que contém um script de submissão, dá permissão de execução e executa** 


```
 $ for i in `cat lista`; do cd $i; chmod +x qsub_interface.g2s.$i; \n 
 ./qsub_interface.g2s.$i; cd -; done
```


**Comando while; do; done**
**6.6 Faz um loop em cima de datas; verifica se a primeira data é menor ou igual do que a segunda. Quando esta condição é alcançada, sai do loop**


```
 $ while [ <data_inicio> -le <data_fim> ]; do <operacoes>; done
```


**Referências Úteis:**

- [Canivete Suíço do Shell](http://aurelio.net/shell/canivete/)
- [Só Sed](http://thobias.org/doc/sosed.html)
- [SED](http://aurelio.net/sed/)
