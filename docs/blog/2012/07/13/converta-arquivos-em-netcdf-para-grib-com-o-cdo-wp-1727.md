---
title: Converta arquivos em NetCDF para GRIB com o CDO
date: '2012-07-13 09:09:10'
tags:
- Ciência
- GRIB
- NetCDF
- Tudo
- Tutoriais
- cdo
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 1727
original_url: https://craftmind.wordpress.com/2012/07/13/converta-arquivos-em-netcdf-para-grib-com-o-cdo/
---

# Converta arquivos em NetCDF para GRIB com o CDO

O CDO (Climate Data Operators) é um conjunto de rotinas para manipulação de dados meteorológicos bastante poderoso. Entre suas rotinas, há uma bastante interessante que permite a conversão de um arquivo NetCDF para GRIB (se você quer saber como fazer o contrário, ou seja, converter de GRIB para NetCDF, [clique aqui](converta-grib-em-netcdf-com-o-ncl-wp-1722.md)). Ele funciona em linha de comando e poder ser utilizado em scripts, sendo bastante prático por isso. Vejamos:

**1) Instalação:**

Para instalar no Ubuntu, digite no terminal:


```
$ sudo apt-get install cdo
```


Se você estiver no Mac OS X, instale o cdo pelo port:


```
$ sudo port install cdo
```


**2) Utilização:**

Com o cdo instalado, basta executar o comando abaixo para converter um arquivo NetCDF para GRIB:


```
$ cdo -f grb copy arquivo.nc arquivo.grib
```


Com isso, será criado o arquivo arquivo.grib, mas apenas ele. Ainda nos falta o arquivo descritor (ctl) e o respectivo arquivo de índice (idx). Para gerá-los numa tacada só, utilize o comando abaixo:


```
$ cdo gradsdes arquivo.grib
```


Feito isto, você poderá abrir o arquivo.grib no GrADS utilizando o ctl criado com o comando anterior! O único inconveniente nesse processo, é que o ctl criado não herda as informações como o nome das variáveis do arquivos grib - elas são renomeadas para var1, var1 etc.

**Referência:**
<http://www.mpimet.mpg.de/fileadmin/software/cdo/cdo.pdf>
