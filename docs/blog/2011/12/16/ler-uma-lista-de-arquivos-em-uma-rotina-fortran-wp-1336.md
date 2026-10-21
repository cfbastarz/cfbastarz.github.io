---
title: Ler uma lista de arquivos em uma rotina fortran
date: '2011-12-16 12:30:16'
tags:
- Ciência
- Tudo
- Tutoriais
- fortran
- ler lista de arquivos
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 1336
original_url: https://craftmind.wordpress.com/2011/12/16/ler-uma-lista-de-arquivos-em-uma-rotina-fortran/
---

# Ler uma lista de arquivos em uma rotina fortran

Esses dias estava tentanto executar uma rotina em fortran que lia um arquivo texto e convertia em binário. Como eram vários arquivos a serem lidos, eu tinha duas opções: primeira, que seria fazer um script em shell com um loop para ler os arquivos, gerar a rotina para ler cada arquivo e executar; segunda, melhorar a rotina para que ela pudesse ler uma lista com arquivos e executar a conversão para cada arquivo lido da lista. É claro que a segunda opção é mais eficiente e elegante, e também a que dá mais preguiça de pensar. Eis a solução (não sei se é a melhor, mas funciona):

```matlab
program le_lista_arquivos                                                                                                             
   implicit none
 
  ! Variaveis:
  ! file: e o nome do arquivo a ser lido
  ! filelist: e o nome da lista com os arquivos a serem lidos
  ! cont: e um contador
  ! ierro: e uma variavel de status (se ierro=1, entao ocorreu erro de I/O)
  ! total: vai receber a quantidade total de arquivos lidos
 
  integer                            :: cont, total, ierro
  character(len=200)                 :: arquivo, lista
  character(len=200), dimension(500) :: vetor
 
  call getarg(1,lista)
 
  open(unit=10,file=trim(lista),status="old",form="formatted")
 
  cont=0
 
  do  
 
    read(10,"(A)",iostat=ierro) arquivo

    if(ierro.ne.0) exit

    cont = cont + 1 
    vetor(cont) = trim(arquivo)

    print *, "Arquivo: ", arquivo
 
  enddo
 
  total=cont
 
  close(10)
 
  print *, "Numero de arquivos lidos: ", total
 
end program le_lista_arquivos
```

No programa acima, há um loop que se encarrega de ler um arquivo de texto (lista) cujo conteúdo é o nome de cada arquivo texto, da seguinte forma:


```
$ more lista
 arquivo1.txt
 arquivo2.txt
 arquivo3.txt
 ...
```


O pulo do gato nesse programa, é o comando "call getarg" que vai permitir que a rotina tome o arquivo "lista" como se fosse um argumento.

Dentro desse loop em que os nomes dos arquivos são lidos, pode-se realizar as operações que se desejar com o conteúdo deles.

Para compilar, pode-se fazer assim (usando o ifort, mas funciona também com o gfortran):


```
$ ifort -traceback -o le_lista_arquivos.x le_lista_arquivos.f90
```


E para executar, basta fazer:


```
$ ./le_lista_arquivos.x lista
```


Como resultado, a execução do programa imprime a lista dos arquivos a serem lidos e informa a quantidade de arquivos lidos:


```
 
Arquivo: arquivo1.txt
Arquivo: arquivo2.txt
Arquivo: arquivo3.txt
Arquivo: arquivo4.txt
Arquivo: arquivo5.txt
Arquivo: arquivo6.txt
Arquivo: arquivo7.txt
Arquivo: arquivo8.txt
Arquivo: arquivo9.txt
Arquivo: arquivo10.txt
Arquivo: arquivo11.txt
Arquivo: arquivo12.txt
Arquivo: arquivo13.txt
Arquivo: arquivo14.txt
Arquivo: arquivo15.txt
Arquivo: arquivo16.txt
Arquivo: arquivo17.txt
Arquivo: arquivo18.txt
Arquivo: arquivo19.txt
Arquivo: arquivo20.txt
Numero de arquivos lidos: 20
```


A opção "-traceback" é interessante porque, mesmo quando a compilação é bem sucedida, pode ser que na execução exista algum erro, como a falta de um argumento. Assim, se você tentar executar o programa "le_lista_arquivos.x" sem o argumento "filelst", você vai receber a seguinte mensagem de erro:


```
$ ./le_lista.x
forrtl: severe (43): file name specification error, unit 100, file "Unknown"
Image              PC                Routine            Line        Source             
le_lista.x         000000000046FAFA  Unknown               Unknown  Unknown
le_lista.x         000000000046E5F6  Unknown               Unknown  Unknown
le_lista.x         000000000042FC60  Unknown               Unknown  Unknown
le_lista.x         0000000000405E6E  Unknown               Unknown  Unknown
le_lista.x         00000000004053AF  Unknown               Unknown  Unknown
le_lista.x         00000000004104ED  Unknown               Unknown  Unknown
le_lista.x         0000000000402BA9  MAIN__                     13  le_lista.f90
le_lista.x         0000000000402A9C  Unknown               Unknown  Unknown
libc.so.6          00007F03CA7A1EFF  Unknown               Unknown  Unknown
le_lista.x         0000000000402999  Unknown               Unknown  Unknown
```


Na [lista de erros de execução do ifort](http://software.intel.com/sites/products/documentation/hpc/compilerpro/en-us/fortran/lin/compiler_f/bldaps_for/common/bldaps_rterrs.htm), há a seguinte descrição da mensagem "severe (43)":
> severe (43): File name specification error
> FOR$IOS_FILNAMSPE. A pathname or file name given to an OPEN or INQUIRE statement was not acceptable to the Intel Fortran RTL I/O system.

Repare que na mensagem de erro, há a indicação de que na linha 13 há uma problema. Na verdade, a mensagem se refere ao arquivo "filelst" que está declarado na linha 13 do programa, que está sendo indicado pela mensagem "severe (43)".

É isso!
