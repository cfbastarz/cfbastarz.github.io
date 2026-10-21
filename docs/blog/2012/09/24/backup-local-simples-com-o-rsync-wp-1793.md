---
title: Backup local simples com o rsync
date: '2012-09-24 11:34:26'
tags:
- Shell
- Tudo
- Tutoriais
- backup
- ksh
- rsync
- script
categories:
- Tudo
- Tutoriais
wordpress_id: 1793
original_url: https://craftmind.wordpress.com/2012/09/24/backup-local-simples-com-o-rsync/
---

# Backup local simples com o rsync

O script abaixo tem por objetivo realizar o backup/sincronização (incremental) entre duas pastas diferentes, facilitando e agilizando p processo de cópia de grandes volumes de arquivos.

**Algorítmo**

O algorítmo deste script segue os seguintes passos:

1. Verificação dos argumentos de entrada:
   1. Verifica se a quantidade de argumentos não é dois (caso postivo, mostra a função ajuda e finaliza);
   2. Verifica se a quantidade de argumentos é dois (caso positivo, verifica os locais - se são acessíveis ou não);
2. Com os dois argumentos de entrada (origem e destino, respectivamente), chama a função backup
3. Finaliza o script



```
#!/bin/ksh
#set -o xtrace
ajuda() {
print "Uso: ./backup_rsync.ksh <origem> <destino>"
 exit 1
}
backup() {
origem=${1}
 destino=${2}
rsync -av ${origem}/ ${destino}/
}
if [ $# -ne 2 ]
 then
ajuda
elif [ $# -eq 2 ]
 then
print "Verificando os locais:"
 print "${1}"
 print "${2}"
if [ ${1} == ${2} ]
 then
print "${1} e o mesmo local de destino (${2})"
 exit 1
elif [ ${1} != ${2} -a -r ${1} -a -w ${2} ]
 then
backup ${1} ${2}
else
print "${1} inacessivel ou ${2} nao pode ser escrito"
 exit 1
fi
else
ajuda
fi
exit 0
```


**Exemplo**

No exemplo abaixo, serão sincronizadas as pastas "teste1" e "teste2", ambas presentes no mesmo diretório em que o script será executado (o que não é uma necessidade). Cada uma das pastas contém os arquivos "arquivo1" e "arquivo2", respectivamente. O objetivo é fazer com que a "pasta2" contenha os "arquivo1" e "arquivo2". Em qualquer caso, nenhum arquivos é apagado.


```
./backup_rsync.ksh teste2 teste1
 Verificando os locais:
 teste2
 teste1
 sending incremental file list
 arquivo2
sent 127 bytes received 31 bytes 316.00 bytes/sec
 total size is 0 speedup is 0.00
```


**Observações**

- Na primeira vez em que o script for utilizado, pode ser que leve um tempo maior; depois disso, o processo de sincronização é mais rápido;
- Na linha 17 do script, a barra no final de ${origem} e ${destino} é necessária para que o conteúdo de ${origem} seja armazenado no primeiro nível de ${destino}, caso contrário a pasta ${origem} será criada dentro de ${destino}.
