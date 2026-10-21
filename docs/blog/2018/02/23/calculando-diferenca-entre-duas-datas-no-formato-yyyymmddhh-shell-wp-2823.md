---
title: Calculando diferença entre duas datas no formato YYYYMMDDHH (Shell)
date: '2018-02-23 10:34:31'
tags:
- Ciência
- Datas
- Shell
- Tudo
- Tutoriais
- ksh
- script
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 2823
original_url: https://craftmind.wordpress.com/2018/02/23/calculando-diferenca-entre-duas-datas-no-formato-yyyymmddhh-shell/
---

# Calculando diferença entre duas datas no formato YYYYMMDDHH (Shell)

Neste post vou apresentar um script que escrevi há alguns meses atrás para calcular a diferença entre duas datas quaisquer, no formato YYYYMMDDHH (ou seja, no formato ANO, MÊS, DIA, HORA SINÓTICA).

# Exemplo

Qual a diferença (em dias ou em horas) entre as datas "2013010100" e "2013011512"?

O script irá calcular a diferença entre estas duas datas e o resultado será dado em dias e em horas:


```
$ ./calc_date_diff.ksh 2013010100 2013011512
```


14 dia(s) e 12 hora(s) ou 348 hora(s)

# Script

O script possui o seguinte algorítmo:

1. Recebe as duas datas pela linha de comando;
2. As datas são fornecidas como argumentos para a função datediff;
3. Na função datediff, são separados os anos, os meses, os dias e os horários sinóticos;
4. A partir disso, são formatadas as datas data1 e data2 no formato 'YYYY-MM-DD HH:mm:ss UTC';
5. Verifica se a data2 é maior ou menor do que data1; se data2 for maior do que data1,
6. Verifica se HH da data2 é igual a zero e se não é igual a HH da data1;
   1. Se esta verificação for verdadeira, então a diferença entre HH (horas) das datas Informadas será calculada por 24-HH da data1;
   2. Caso contrário, a diferença entre HH (horas) das datas será calculada pela diferença entre os HH da data2 e data1;
7. Se HH da data1 for igual a zero e HH da data2 não for igual a HH da data1, então a diferença entre HH das datas é calculada por 24 menos HH da data2;
   1. Caso contrário, esta diferença será calculada pela diferença entre HH da data2 e data1.



```bash
#! /bin/ksh

#set -o xtrace

data_anl=${1}
data_fct=${2}

datediff(){

  yyyy_anl=$(echo ${data_anl} | cut -c 1-4)
  mm_anl=$(echo ${data_anl} | cut -c 5-6)
  dd_anl=$(echo ${data_anl} | cut -c 7-8)
  hh_anl=$(echo ${data_anl} | cut -c 9-10)

  yyyy_fct=$(echo ${data_fct} | cut -c 1-4)
  mm_fct=$(echo ${data_fct} | cut -c 5-6)
  dd_fct=$(echo ${data_fct} | cut -c 7-8)
  hh_fct=$(echo ${data_fct} | cut -c 9-10)

  data1=$(date -d "${yyyy_anl}-${mm_anl}-${dd_anl} ${hh_anl}:00:00 UTC" "+%s")
  data2=$(date -d "${yyyy_fct}-${mm_fct}-${dd_fct} ${hh_fct}:00:00 UTC" "+%s")

  if [ ${data2} -gt ${data1} ]
  then
    if [ ${hh_fct} -eq "0" -a ${hh_fct} -ne ${hh_anl} ]
    then
      hh_diff=$(( 24-${hh_anl} ))
    else
      hh_diff=$(( ${hh_fct}-${hh_anl} ))
    fi
  else
    if [ ${hh_anl} -eq "0" -a ${hh_fct} -ne ${hh_anl} ]
    then
      hh_diff=$(( 24-${hh_fct} ))
    else
      hh_diff=$(( ${hh_anl}-${hh_fct} ))
    fi
  fi

  dd_diff=$(((${data2}-${data1}) / 86400))

  hh_tot=$((${dd_diff}*24+${hh_diff}))

}

datediff ${data_anl} ${data_fct}

echo "${dd_diff} dia(s) e ${hh_diff} hora(s) ou ${hh_tot} hora(s)"

exit 0
```

É isso!
