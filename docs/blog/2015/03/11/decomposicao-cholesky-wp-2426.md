---
title: Decomposição Cholesky
date: '2015-03-11 21:40:50'
tags:
- Ciência
- Decomposição Cholesky
- Matemática
- Tudo
- Álgebra Linear
categories:
- Ciência
- Tudo
wordpress_id: 2426
original_url: https://craftmind.wordpress.com/2015/03/11/decomposicao-cholesky/
---

# Decomposição Cholesky

A decomposição (ou fatoração) Cholesky (pronuncia-se "Colesqui") permite a solução de problemas que envolvam matrizes grandes em que há a necessidade de se fracionar a solução do problema (geralmente a solução de um ou mais sistemas de equações lineares), em que os fatores obtidos a partir da decomposição da matriz original, resulta em matrizes (os fatores) triangulares superior e inferior.



Toda matriz simétrica positiva $A$ pode ser decomposta em um produto único entre uma matriz $L$ triangular inferior e sua transposta:



$$
A=LL^{T}
$$



$L$ é chamada de fator Cholesky de $A$ e pode ser interpretada como a raiz quadrada generalizada de $A$.

Em um exemplo 3x3, podemos resolver o seguinte sistema de equações:



$$
A = \left| \begin{array}{ccc} a_{11} & a_{21} & a_{31} \\ a_{21} & a_{22} & a_{32} \\a_{31} & a_{32} & a_{33} \end{array} \right|
$$





$$
A = \left| \begin{array}{ccc} l_{11} & 0 & 0 \\ l_{21} & l_{22} & 0 \\l_{31} & l_{32} & l_{33} \end{array} \right| \left| \begin{array}{ccc} l_{11} & l_{21} & l_{31} \\ 0 & l_{22} & l_{32} \\ 0 & 0 & l_{33} \end{array} \right| \equiv LL^{T}
$$



Logo,



$$
LL^{T} = \left| \begin{array}{ccc} l_{11}^2 & l_{11}l_{21} & l_{11}l_{31} \\ l_{21}l_{11} & l_{21}^{2}+l_{22} & l_{21}l_{31}+l_{22}l_{32} \\l_{31}l_{11} & l_{31}l_{21}+l_{32}l_{22} & l_{31}^{2}+l_{32}^{2}+l_{33}^{2} \end{array} \right|
$$



Comparando as matrizes $A$ e $LL^T$, podemos observar que para os elementos da diagonal principal (elementos $l_{kk}$) de $LL^T$, há um determinado padrão:



$$
l_{11}^2=a_{11} \Rightarrow l_{11}=\sqrt{a_{11}}
$$





$$
l_{21}^{2}+l_{22}^2=a_{22} \Rightarrow l_{22}^2=a_{22}-l_{21}^2 \Rightarrow l_{22} = \sqrt{a_{22} - l_{21}^2}
$$





$$
l_{31}^2+l_{32}^2+l_{33}^2=a_{32} \Rightarrow l_{33}^2=a_{33}-(l_{31}^2+l_{32}^2) \Rightarrow l_{33}=\sqrt{a_{33}-(l_{31}^2+l_{32}^2)}
$$



Ou seja, os elementos da diagonal principal de $LL^T$, podem ser escritos da seguinte forma:



$$
l_{kk}=\sqrt{a_{kk}-\sum_{j=1}^{k-1}{l_{kj}^2}}
$$



Comparando-se as matrizes $A$ e $LL^T$, podemos observar que os elementos abaixo da diagonal principal de $LL^T$ (elementos $l_{ik}$ com $i>k$), podem ser escritos da seguinte forma:



$$
l_{21}l_{11}=a_{21} \Rightarrow l_{21}=\frac{1}{l_{11}}a_{21}
$$




$$
l_{31}l_{11}=a_{31} \Rightarrow l_{31}=\frac{1}{l_{11}}a_{31}
$$




$$
l_{31}l_{21}+l_{32}l_{22}=a_{32} \Rightarrow l_{32}l_{22}=a_{32}-l_{31}l_{21} \Rightarrow l_{32}=\frac{1}{l_{22}}(a_{32}-l_{31}l_{21})
$$



Ou seja, estes elementos que estão abaixo da diagonal principal de $LL^T$ podem ser escrito da seguinte forma:



$$
l_{ik}=\frac{1}{l_{kk}}(a_{ik}-\sum_{j=1}^{k-1}{l_{ij}l_{kj}})
$$



**Referências:**

- <http://rosettacode.org/wiki/Cholesky_decomposition>
