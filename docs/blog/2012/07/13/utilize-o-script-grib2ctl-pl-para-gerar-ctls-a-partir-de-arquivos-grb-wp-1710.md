---
title: Utilize o script grib2ctl.pl para gerar ctl's a partir de arquivos GRIB
date: '2012-07-13 01:01:26'
tags:
- Ciência
- GRB
- GRIB
- Tudo
- Tutoriais
- grib2ctl.pl
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 1710
original_url: https://craftmind.wordpress.com/2012/07/13/utilize-o-script-grib2ctl-pl-para-gerar-ctls-a-partir-de-arquivos-grb/
---

# Utilize o script grib2ctl.pl para gerar ctl&#x27;s a partir de arquivos GRIB

Um arquivo GRIB (Grid In Binary) é um arquivo binário em ponto de grade padrão recomendado pela OMM (Organização Meteorológica Mundial) para armazenamento de dados meteorológicos em ponto de grade. É um arquivo sequencial binário e que pode ser aberto pelo software GrADS (Gridpoint Analysis and Display System) por meio de um arquivo descritor, o ctl. Se você tem um arquivo GRIB mas não tem o seu respectivo descritor (ctl), você pode tentar utilizar o script [grib2ctl.pl](ftp://ftp.cpc.ncep.noaa.gov/wd51we/wgrib.scripts/grib2ctl.pl) do NCEP (National Centers for Environmental Predictions) para gerar os seus ctl's. Veja como:

1) Baixe o script grib2ctl.pl do servidor ftp do NCEP:


```
$ wget ftp://ftp.cpc.ncep.noaa.gov/wd51we/wgrib.scripts/grib2ctl.pl
```


2) Copie o script grib2ctl.pl para a pasta /usr/local/bin do seu Linux (ou Mac OS X):


```
$ sudo cp grib2ctl.pl /usr/local/bin
```


3) Dê permissão de execução:


```
$ sudo chmod +x /usr/local/bin/grib2ctl.pl
```


Para utilizar, basta fazer o seguinte:


```
$ grib2ctl.pl arquivo.grib > arquivo.ctl
```


Com este comando, o script grib2ctl.pl irá ler as informações do arquivo GRIB que serão escritas no arquivo "arquivo.ctl". Com isso, já temos um arquivo descritor. Mas ainda, nos falta um arquivo de índice, que mapeia a grade do arquivo binário. Para criá-lo, podemos utilizar o programa "gribmap"do GrADS para gerar o arquivo de índice, geralmente com a extensão idx ou gmp. Para isto, podemos fazer:


```
$ gribmap -v -i arquivo.ctl
```


As opções "v",  e "i" são opções para, respectivamente, "verbose" e "input". Feito isto, podemos abrir o arquivo no GrADS e visualizar as informações:


```
$ grads -blc "open arquivo.ctl"
```


**Referência:**
<http://www.cpc.ncep.noaa.gov/products/wesley/grib2ctl.html>
