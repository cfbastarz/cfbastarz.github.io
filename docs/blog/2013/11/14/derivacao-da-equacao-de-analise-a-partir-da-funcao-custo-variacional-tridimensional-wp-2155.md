---
title: Derivaçao da Equação de Análise a partir da Função Custo Variacional Tridimensional
date: '2013-11-14 13:46:46'
tags:
- 3DVar
- Assimilação de Dados
- Ciência
- Equação de Análise
- Função Custo Variacional
- Tudo
categories:
- Ciência
- Tudo
wordpress_id: 2155
original_url: https://craftmind.wordpress.com/2013/11/14/derivacao-da-equacao-de-analise-a-partir-da-funcao-custo-variacional-tridimensional/
---

# Derivaçao da Equação de Análise a partir da Função Custo Variacional Tridimensional

Abaixo apresento uma derivação da equação de análise utilizada em assimilação de dados para a determinação da condição inicial dos modelos de previsão numérica de tempo. Esta equação é obtida a partir da função custo variacional tridimensional (3DVar), sem considerar a dimensão temporal das observações. Logo, todos os elementos do vetor observação $\mathbf{y^{o}}$ são considerados em um mesmo $t=t_{0}$, enquanto que o background $\mathbf{x_{b}}$ é considerado no tempo $t=t_{0}-1$ e a análise $\mathbf{x_{a}}$ é obtida para o mesmo tempo das observações ($t=t_{0}$).

Apesar de parecer um tanto quanto enfadonho (principalmente porque este é um passo a passo), acho interessante apresentar as idéias relacionadas à derivação porque não se tem textos semelhantes em português. Para um texto científico, a maioria das passagens abaixo seriam descartadas, reduzindo esta derivação a poucas equações. De antemão, acrescento que sugestões e correções são bem vindas, visto que algumas imprecisões podem existir.

Seja (1) a função custo variacional tridimensional:



$$
J(\mathbf{x}) = \frac{1}{2}(\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{B}^{-1}(\mathbf{x} - \mathbf{x_{b}}) + \frac{1}{2}(\mathbf{y^o} - \textit{H}(\mathbf{x}))^{T}\mathbf{R}^{-1}(\mathbf{y^o} - \textit{H}(\mathbf{x}))
$$


(1)

**Onde:**

- $\mathbf{x}$ é o vetor de estado a ser analisado de dimensão $\textit{p}$
- $\mathbf{x_{b}}$ é o vetor de estado do background de dimensão $\textit{p}$
- $\mathbf{B}$ é a matriz de covariâncias dos erros de background de dimensão $\textit{p}\times\textit{p}$
- $\mathbf{y^{o}}$ é o vetor observação de dimensão $\textit{n}$
- $\mathbf{R}$ é a matriz de covariâncias dos erros de observação de dimensão $\textit{n}\times\textit{n}$
- $\textit{H}$ é o operador observação não linear

**Oservação:** Em geral $\textit{H}$ é um modelo linearizado (portanto sob a forma $\mathbf{H}$) que mapeia os valores do background para os pontos em que estão as observações.

Na Eq. (1), o termo $(\mathbf{x} - \mathbf{x_{b}})$ representa o vetor incremento de análise e o termo $(\mathbf{y^{o}} - \textit{H}(\mathbf{x}))$ representa o vetor inovação.

Para derivar a equação de análise a partir de (1), consideramos (por simplicidade) apenas uma observação e que o vetor incremento de análise é pequeno o suficiente para que possamos linearizar o operador observação:



$$
\mathbf{x} = \mathbf{x_{b}} + (\mathbf{x} - \mathbf{x_{b}})
$$


(2)

Ou seja, em (2) expressamos que o vetor de estado a ser analisado (a análise) é igual ao vetor de estado do background somado ao incremento de análise. Substituindo $\mathbf{x}$ da Eq. (2) na relação do vetor inovação:



$$
\mathbf{y^{o}} - \textit{H}(\mathbf{x}) = \mathbf{y^{o}} - \textit{H}[\mathbf{x_{b}} + (\mathbf{x} - \mathbf{x_{b}})]
$$


(3)



$$
\mathbf{y^{o}} - \textit{H}(\mathbf{x}) = \mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}) - \textit{H}(\mathbf{x} - \mathbf{x_{b}})
$$


(4)

Na Eq. (4) o operador observação não linear $\textit{H}$ é aplicado sobre o incremento de análise $(\mathbf{x} - \mathbf{x_{b}})$, o qual é muito pequeno. Sendo assim, considera-se que o operador observação a ser aplicado sobre o incremento de análise pode ser linearizado. Isto significa que pequenas variações do vetor incremento de análise fazem com que $\textit{H}$ varie muito pouco. Portanto, a Eq. (4) pode ser reescrita como:



$$
\mathbf{y^{o}} - \textit{H}(\mathbf{x}) = \mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}) - \mathbf{H}(\mathbf{x} - \mathbf{x_{b}})
$$


(5)

**Onde:**

- $\mathbf{H}$ é a versão linearizada do operador observação não linear ($\textit{H}$).

Substituindo a Eq. (5) na Eq. (1):



$$
J(\mathbf{x}) = \frac{1}{2}(\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{B}^{-1}(\mathbf{x} - \mathbf{x_{b}}) + \frac{1}{2}[\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}) - \mathbf{H}(\mathbf{x} - \mathbf{x_{b}})]^{T}\mathbf{R}^{-1}[\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}) - \mathbf{H}(\mathbf{x} - \mathbf{x_{b}})]
$$


(6)

Fatorando e desenvolvendo a Eq. (6):



$$
J(\mathbf{x}) = \frac{1}{2}\lbrace(\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{B}^{-1}(\mathbf{x} - \mathbf{x_{b}}) + [\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}) - \mathbf{H}(\mathbf{x} - \mathbf{x_{b}})]^{T}\mathbf{R}^{-1}[\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}) - \mathbf{H}(\mathbf{x} - \mathbf{x_{b}})]\rbrace
$$


(7)



$$
2J(\mathbf{x}) = (\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{B}^{-1}(\mathbf{x} - \mathbf{x_{b}}) + [\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}) - \mathbf{H}(\mathbf{x} - \mathbf{x_{b}})]^{T}\mathbf{R}^{-1}[\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}) - \mathbf{H}(\mathbf{x} - \mathbf{x_{b}})]
$$


(8)



$$
2J(\mathbf{x}) = (\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{B}^{-1}(\mathbf{x} - \mathbf{x_{b}}) + [(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T} - (\mathbf{H}(\mathbf{x} - \mathbf{x_{b}}))^{T}]\mathbf{R}^{-1}[\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}) - \mathbf{H}(\mathbf{x} - \mathbf{x_{b}})]
$$


(9)



$$
2J(\mathbf{x}) = (\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{B}^{-1}(\mathbf{x} - \mathbf{x_{b}}) + [(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T} - \mathbf{H}^{T}(\mathbf{x} - \mathbf{x_{b}})^{T}]\mathbf{R}^{-1}[\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}) - \mathbf{H}(\mathbf{x} - \mathbf{x_{b}})]
$$


(10)



$$
2J(\mathbf{x}) = (\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{B}^{-1}(\mathbf{x} - \mathbf{x_{b}}) + [(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T}\mathbf{R}^{-1} - \mathbf{H}^{T}(\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{R}^{-1}][\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}) - \mathbf{H}(\mathbf{x} - \mathbf{x_{b}})]
$$


(11)



$$
2J(\mathbf{x}) = (\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{B}^{-1}(\mathbf{x} - \mathbf{x_{b}}) + (\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T}\mathbf{R}^{-1}(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}})) - (\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T}\mathbf{R}^{-1}\mathbf{H}(\mathbf{x} - \mathbf{x_{b}}) - \mathbf{H}^{T}(\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{R}^{-1}(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}})) + \mathbf{H}^{T}(\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{R}^{-1}\mathbf{H}(\mathbf{x} - \mathbf{x_{b}})
$$


(12)

Reorganizando a Eq. (12) - aqui serão fatorados os termos 1 e 5 do lado direito:



$$
2J(\mathbf{x}) = (\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{B}^{-1}(\mathbf{x} - \mathbf{x_{b}}) + (\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H}(\mathbf{x} - \mathbf{x_{b}}) - (\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T}\mathbf{R}^{-1}\mathbf{H}(\mathbf{x} - \mathbf{x_{b}}) - (\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{H}^{T}\mathbf{R}^{-1}(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}})) + (\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T}\mathbf{R}^{-1}(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))
$$


(13)

Combinando os dois primeiros termos do lado direito de (13), obtemos:



$$
2J(\mathbf{x}) = (\mathbf{x} - \mathbf{x_{b}})^{T}[\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H}](\mathbf{x} - \mathbf{x_{b}}) - (\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T}\mathbf{R}^{-1}\mathbf{H}(\mathbf{x} - \mathbf{x_{b}}) - (\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{H}^{T}\mathbf{R}^{-1}(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}})) + (\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T}\mathbf{R}^{-1}(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))
$$


(14)

A forma da Eq. (14) é a forma em que será aplicado o operador gradiente. O gradiente é aplicado na função custo variacional para se determinar o vetor de estado de análise $\mathbf{x_{a}}$ tal que $\nabla_{x}{J(\mathbf{x})} = 0$. Ou seja, o mínimo de $J(\mathbf{x})$ fornece os valores do vetor de estado analisado.

**Teorema (1):**
Dada a função quadrática $F(\mathbf{x}) = \frac{1}{2}\mathbf{x}^{T}\mathbf{A}\mathbf{x} + \mathbf{d} + c$, onde $\mathbf{A}$ é uma matriz simétrica (ou seja, é igual à sua transposta), $\mathbf{x}$ e $\mathbf{d}$ são vetores e $c$ é um escalar, o gradiente de $F(\mathbf{x})$ é dado por $\nabla_{x}{F(\mathbf{x})} = \mathbf{A}\mathbf{x} + \mathbf{d}$.

**Demonstração (1):**

$F(\mathbf{x}) = \frac{1}{2}\mathbf{x}^{T}\mathbf{A}\mathbf{x} + \mathbf{d} + c \\
\frac{\partial F}{\partial x} = \frac{1}{2}(\mathbf{A}\mathbf{x} + \mathbf{A}^{T}\mathbf{x}) + \mathbf{d}$
(15)

Se $\mathbf{A}$ é simétrica, então $\mathbf{A}^{T} = \mathbf{A}$, logo:

$\frac{\partial F}{\partial x} = \frac{1}{2}(\mathbf{A}\mathbf{x} + \mathbf{A}\mathbf{x}) + \mathbf{d} \\
\frac{\partial F}{\partial x} = \frac{1}{2}(2\mathbf{A}\mathbf{x}) + \mathbf{d} \\
\frac{\partial F}{\partial x} = \mathbf{A}\mathbf{x} + \mathbf{d}$
(16)

Aplicando o operador gradiente na Eq. (14), obtem-se:



$$
\nabla_{x}{2J(\mathbf{x})} = \frac{\partial \lbrace(\mathbf{x} - \mathbf{x_{b}})^{T}[\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H}](\mathbf{x} - \mathbf{x_{b}})\rbrace}{\partial x} - \frac{\partial \lbrace(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T}\mathbf{R}^{-1}\mathbf{H}(\mathbf{x} - \mathbf{x_{b}})\rbrace}{\partial x} - \frac{\partial \lbrace(\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{H}^{T}\mathbf{R}^{-1}(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))\rbrace}{\partial x} + \frac{\partial \lbrace(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T}\mathbf{R}^{-1}(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))\rbrace}{\partial x}
$$


(17)

Na Eq. (17) observamos que o termo 4 do lado direito não depende do vetor de estado analisado $\mathbf{x}$ e que portanto $\frac{\partial \lbrace(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T}\mathbf{R}^{-1}(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))\rbrace}{\partial x} = 0$, logo:



$$
2\nabla_{x}{J(\mathbf{x})} = \frac{\partial \lbrace(\mathbf{x} - \mathbf{x_{b}})^{T}[\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H}](\mathbf{x} - \mathbf{x_{b}})\rbrace}{\partial x} - \frac{\partial \lbrace(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T}\mathbf{R}^{-1}\mathbf{H}(\mathbf{x} - \mathbf{x_{b}})\rbrace}{\partial x} - \frac{\partial \lbrace(\mathbf{x} - \mathbf{x_{b}})^{T}\mathbf{H}^{T}\mathbf{R}^{-1}(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))\rbrace}{\partial x}
$$


(18)

Utilizando o Teorema (1), obtem-se:



$$
2\nabla_{x}{J(\mathbf{x})} = [(\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H})^{T}(\mathbf{x} - \mathbf{x_{b}}) + (\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H})(\mathbf{x} - \mathbf{x_{b}})] - \frac{\partial \lbrace(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))^{T}\mathbf{R}^{-1}\mathbf{H}(\mathbf{x} - \mathbf{x_{b}})\rbrace}{\partial x} - [(\mathbf{H}^{T}\mathbf{R}^{-1})^{T}(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}})) + (\mathbf{H}^{T}\mathbf{R}^{-1})(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))]
$$


(19)

O segundo termo da Eq. (19) resulta em zero, pois a derivada da constante $(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))\mathbf{R}^{-1}\mathbf{H}$ é zero.

Utilizando-se do fato de que as relações entre as matrizes nos termos 1-3 do lado direito da Eq. (18) geram matrizes simétricas (e.g., $(\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H})^{T}= (\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H})$), a Eq. (19) reduz-se a:



$$
2\nabla_{x}{J(\mathbf{x})} = 2[(\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H})(\mathbf{x} - \mathbf{x_{b}})] - 2[(\mathbf{H}^{T}\mathbf{R}^{-1})(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))]
$$


(20)

e,



$$
\nabla_{x}{J(\mathbf{x})} = (\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H})(\mathbf{x} - \mathbf{x_{b}}) - (\mathbf{H}^{T}\mathbf{R}^{-1})(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))
$$


(21)

No inicio foi feita consideração de que o vetor de estados analisado $\mathbf{x}$ é a própria análise quando $\nabla_{x}{J(\mathbf{x})} = 0$, logo iguala-se a Eq. (21) a zero, de forma que $\mathbf{x} = \mathbf{x_{a}}$:



$$
0 = (\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H})(\mathbf{x_{a}} - \mathbf{x_{b}}) - (\mathbf{H}^{T}\mathbf{R}^{-1})(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))
$$


(22)

Reorganizando a Eq. (22):

$(\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H})(\mathbf{x_{a}} - \mathbf{x_{b}}) - (\mathbf{H}^{T}\mathbf{R}^{-1})(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}})) = 0 \\
(\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H})(\mathbf{x_{a}} - \mathbf{x_{b}}) = (\mathbf{H}^{T}\mathbf{R}^{-1})(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}})) \\
(\mathbf{x_{a}} - \mathbf{x_{b}}) = (\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H})^{-1}[(\mathbf{H}^{T}\mathbf{R}^{-1})(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))]$
(23)

A partir da Eq. (23), obtemos a Equação de Análise:



$$
\mathbf{x_{a}} = \mathbf{x_{b}} + (\mathbf{B}^{-1} + \mathbf{H}^{T}\mathbf{R}^{-1}\mathbf{H})^{-1}[(\mathbf{H}^{T}\mathbf{R}^{-1})(\mathbf{y^{o}} - \textit{H}(\mathbf{x_{b}}))]
$$


(24)
