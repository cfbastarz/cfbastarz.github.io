---
title: Fazendo um loop entre duas datas no Python
date: '2015-10-09 11:53:58'
tags:
- Matemática
- Python
- Shell
- Tudo
- Tutoriais
categories:
- Matemática
- Tudo
- Tutoriais
wordpress_id: 2533
original_url: https://craftmind.wordpress.com/2015/10/09/fazendo-um-loop-entre-duas-data-no-python/
---

# Fazendo um loop entre duas datas no Python

Quem trabalha com análise de dados sabe que muitas vezes é necessário agilizar o processo de organização e compreensão através de programas e scripts que sejam capazes de entender padrões. A utilização de scripts Shell são uma poderosa ferramenta e programas em linguagens de alto nível como C e FORTRAN permitem o processamento eficiente dos dados representados. Em muitas ocasiões, dependendo das suas habilidades computacionais e da sua proficiência em algum tipo de linguagem, você será capaz de trabalhar com esta(s) linguagem(ns), aplicando conceitos de forma quase exclusiva, sem a necessidade de recorrer a linguagens adicionais e tornar a solução do problema excessivamente complicada.



Python é uma linguagem de programação que une as potencialidades de um script Shell e um programa de linguagem de alto nível: com ela, é possível criar sctipts e programas que analisam e processam dados, utilizando o mesmo framework.

Neste post vou mostrar algo mais simples, mas que pode ser aplicado ao seu problema e incrementado para fazer a análise dos seus dados.

O objetivo é criar um script em linguagem Python em que seja realizado um loop entre duas datas formatadas. Em linguagem literal, escreveremos algo como:


```
Enquanto Data for menor do que Data_Final, execute:
    Procedimentos
```


O formato da data deverá ser: YYYYMMDDHH, ou seja, o dia de hoje "09 de Outubro de 2015", será representado como "2015100900", considerando o horário 00UTC (apenas como exemplo). O incremento das horas será feito da seguinte maneira:


```
2015100900 +12 = 2015100912
```


de forma que:


```
2015100912 +12 = 2015101000
```


ou seja, a cada duas somas de 12 horas (24 horas ou 1 dia), teremos um incremento de 1 dia.

No Python, podemos utilizar o módulo "datetime" para manipular datas e os formatos; além disso, podemos utilizar também a função "timedelta" para fazer o incremento das horas.

Juntando as idéias e as informações iniciais em um script Python, chegamos no seguinte:

```python
#!/usr/bin/env python

from datetime import datetime, timedelta

datai = datetime.strptime("2015100900", "%Y%m%d%H")
dataf = datetime.strptime("2015102900", "%Y%m%d%H")

delta = 12
data = datai

while (data <= dataf):

    print data.strftime("%Y%m%d%H")
    data = data + timedelta(hours=delta)
```

No script acima, utilizamos a função "strptime" para poder formatar a data utilizando o padrão %Y%m%d%H (clique [aqui](http://www.tutorialspoint.com/python/time_strptime.htm) para saber mais), que é o mesmo que YYYYMMDDHH, ou seja, 4 dígitos para o ano; dois para o mês, dia e hora. O loop é bastante literal, sendo indicado pela instrução "while (data <= dataf)". Enquanto o teste "data <= dataf" for verdadeiro, a data será impressa no formato indicado e logo em seguida será incrementada em 12 horas. Quando a condição "data <= dataf" for falsa (ou seja, quando "data > dataf"), o loop é encerrado e o script pára.

É isso!

**Referências:**

- <https://pymotw.com/2/datetime/>
