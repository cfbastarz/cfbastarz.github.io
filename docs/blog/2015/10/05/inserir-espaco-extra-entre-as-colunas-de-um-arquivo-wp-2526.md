---
title: Inserir espaço extra entre as colunas de um arquivo
date: '2015-10-05 22:04:20'
tags:
- Shell
- Tudo
- Tutoriais
- sed
categories:
- Tudo
- Tutoriais
wordpress_id: 2526
original_url: https://craftmind.wordpress.com/2015/10/05/inserir-espaco-extra-entre-as-colunas-de-um-arquivo/
---

# Inserir espaço extra entre as colunas de um arquivo

Ah o SED (e o AWK também)!

Estava lidando com arrays escritos em arquivos texto, mas a formatação desses arquivos não era muito boa. Dependendo da magnitude do número no array, não sobrava espaço entre uma coluna e outra.



Veja:


```
-0.11 -0.40 0.53 0.53 3.74E-02-0.48 9.93E-02-0.14 -4.58E-02-6.53E-02 4.20E-02
-0.15 -0.31 0.25 -0.28 -0.77 0.21 -0.21 -0.16 -0.18 4.08E-02-6.06E-02
-0.22 -0.39 0.12 -0.20 0.25 2.82E-02-0.49 0.54 0.37 9.66E-03 0.11 
-0.24 -0.34 -4.19E-02-0.37 0.35 -1.05E-02 0.29 9.77E-02-0.60 -8.60E-02-0.32 
-0.20 -0.35 -0.12 -6.43E-02 9.69E-03 0.27 0.59 -0.12 0.30 0.32 0.44 
-0.23 -0.23 -0.23 0.30 0.16 0.44 -0.18 -0.42 0.18 -0.48 -0.22 
-0.32 -7.84E-02-0.51 -0.14 -9.25E-02-0.60 -0.15 -0.29 0.20 0.23 -0.18 
-0.36 8.16E-02-0.34 0.30 -0.13 -2.42E-02-0.17 0.21 -0.47 -0.14 0.58 
-0.40 0.18 -4.76E-03 0.43 -0.15 0.22 0.13 0.37 3.90E-02 0.39 -0.49 
-0.44 0.35 0.20 -0.25 -0.16 -0.18 0.33 0.14 0.28 -0.57 9.28E-03
-0.42 0.37 0.40 -0.15 0.34 0.13 -0.26 -0.41 -9.80E-02 0.32 0.16
```


Para poder fazer um gráfico com as colunas desses arquivos, seria necessário acrescentar um espaço extre entre as colunas, de forma que os elementos (1,5) e (1,6) pudessem estar representados como "3.74E-02" e "-0.48", ao invés de "3.74E-02-0.48".

Com o sed, é simples fazer essa modificação. Neste caso, estou considerando que as colunas possuem um tamanho fixo, e no meu caso, as colunas tem 9 posições.

Portanto:


```
$ cat arquivo.txt | sed 's/\(.\{9\}\)/\1 /g'
```


E o resultado:


```
-0.11 -0.40 0.53 0.53 3.74E-02 -0.48 9.93E-02 -0.14 -4.58E-02 -6.53E-02 4.20E-02 
-0.15 -0.31 0.25 -0.28 -0.77 0.21 -0.21 -0.16 -0.18 4.08E-02 -6.06E-02 
-0.22 -0.39 0.12 -0.20 0.25 2.82E-02 -0.49 0.54 0.37 9.66E-03 0.11 
-0.24 -0.34 -4.19E-02 -0.37 0.35 -1.05E-02 0.29 9.77E-02 -0.60 -8.60E-02 -0.32 
-0.20 -0.35 -0.12 -6.43E-02 9.69E-03 0.27 0.59 -0.12 0.30 0.32 0.44 
-0.23 -0.23 -0.23 0.30 0.16 0.44 -0.18 -0.42 0.18 -0.48 -0.22 
-0.32 -7.84E-02 -0.51 -0.14 -9.25E-02 -0.60 -0.15 -0.29 0.20 0.23 -0.18 
-0.36 8.16E-02 -0.34 0.30 -0.13 -2.42E-02 -0.17 0.21 -0.47 -0.14 0.58 
-0.40 0.18 -4.76E-03 0.43 -0.15 0.22 0.13 0.37 3.90E-02 0.39 -0.49 
-0.44 0.35 0.20 -0.25 -0.16 -0.18 0.33 0.14 0.28 -0.57 9.28E-03 
-0.42 0.37 0.40 -0.15 0.34 0.13 -0.26 -0.41 -9.80E-02 0.32 0.16
```


Se forem vários arquivos e eles possuírem alguma expressão regular no nome, basta fazer:


```
$ for i in `ls *out*`; do cat $i | sed 's/\(.\{9\}\)/\1 /g' > $i.form; done
```


É isso!

**Referência:**

- <http://www.unix.com/shell-programming-and-scripting/142815-insert-space-between-characters-using-sed.html>
