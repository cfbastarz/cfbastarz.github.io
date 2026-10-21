---
title: Instalando GCC, GFORTRAN, ZLIB, HDF5, NETCDF4 e OpenMPI no Mac OS X
date: '2012-10-07 17:24:23'
tags:
- BSD
- CPPFLAGS
- Ciência
- GCC
- GFORTRAN
- LDFLAGS
- Linux
- Mac OS X
- Tudo
- Tutoriais
- UNIX
- hdf5
- netcdf4
- openmpi
- zlib
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 1852
original_url: https://craftmind.wordpress.com/2012/10/07/instalando-gcc-gfortran-zlib-hdf5-netcdf4-e-openmpi-no-mac-os-x/
---

# Instalando GCC, GFORTRAN, ZLIB, HDF5, NETCDF4 e OpenMPI no Mac OS X

Quem trabalha com programas compilados a partir do código fonte sem ter a disposição um gerenciador de pacotes tal como o apt-get ou o port sabe o trabalho que dá instalar os pré-requisitos e dependências para preparar o ambiente de execução do programa principal. Muitas vezes, os gerenciadores de pacotes facilitam, automatizando as tarefas e principalmente, tratando automaticamente as dependências dos pacotes. Mas nem tudo são vantagens: muitas vezes, há a necessidade de se instalar um novo compilador e nem sempre será possível fazer com que todos os outros pacotes instalados sejam recompilados utilizando as bibliotecas e utilitários do novo compilador; ou ainda, pode ser que seja mais complicado fazer com que o gerenciador de pacotes utilize o novo compilador para recriar os novos executáveis etc (para ver como fazer com que o HomeBrew do Mac OS X trabalhe com um compilador diferente do gfortran clique [aqui](../../08/14/instalando-o-mpich2-pelo-homebrew-compilado-com-o-ifort-wp-1763.md)).

O objetivo deste post é tentar mostrar uma forma objetiva de se utilizar o [MacPorts](http://www.macports.org) para a instalação de alguns programas, mantendo-se mais de um compilador fortran instalado na máquina. Com isso, pode-se pensar na vantagem de se instalar um programa pelo MacPorts ou manualmente. Em ambos os casos a instalação é feita a partir do código fonte, mas com a diferença de que pode-se especificar o local, o compilador e as bibliotecas (versões) a serem utilizadas.

Para exemplificar, serão instalados os pacotes [gcc](http://gcc.gnu.org), [gfortran](http://gcc.gnu.org/wiki/GFortran), [zlib](http://www.zlib.net), [hdf5](http://www.hdfgroup.org/HDF5/), [netcdf4](http://www.unidata.ucar.edu/downloads/netcdf/netcdf-4_0/index.jsp) e [openmpi](http://www.open-mpi.org) no Mac OS X. É possível pensar da mesma forma em qualquer sistema tipo UNIX em que se tem (ou não) um gerenciador de pacotes. Salienta-se, no entanto, que a instalação de alguns pacotes pode levar algumas horas, como é o caso da compilação do pacote gcc.

O gcc é um conjunto de programas essenciais para um sistema em que serão compilados quaisquer tipos de programas a partir do código fonte. Este pacote possui compiladores para as linguagens C, C++ e fortran. Há diversas versões disponíveis do gcc e a que será utilizada será a versão 4.4, sendo que a última versão mais recente (até outubro de 2012, pelo menos) é a versão 4.8. Sua compilação não é muito complicada, sendo feita com a utilização típica dos comandos **configure**, **make** e **make install**. Mas como o gcc é o pacote base para a instalação dos demais, ele será instalado primeiro e isso será feito a partir do MacPorts (se você não tem o MacPorts instalado, baixe o instalador correto para o seu Mac OS X [aqui](http://www.macports.org/install.php)), que já ajusta todas as flags de compilação e otimização automaticamente.

**Para instalar o gcc4.4 no Mac OS X utilizando o MacPorts, basta fazer:**


```
$ sudo port install gcc44
```


Como mencionado acima, o gcc é um pacote que traz os compiladores das linguagens C, C++ e fortran. Este comando poderá demorar várias horas para terminar de ser executado, portanto é uma boa idéia deixar esta tarefa para ser feita durante a noite. A compilação do gcc4.4 é feita através do compilador nativo do Mac OS X, uma versão do gcc (versão 4.2.1 no OS X Mountain Lion) fornecida pela Apple, que vem junto com o Xcode4.X.

Depois da instalação do gcc4.4, é necessário fazer com que toda a suíte trazida pelo gcc4.4 esteja disponível no shell do Mac OS X por padrão. Para isso, basta fazer:


```
$ sudo port select gcc mp-gcc44
```


Este comando fará com que as versões dos compiladores do gcc não conflitem (eg, gcc4.2 nativo com o gfortran4.4 instalado pelo port) e que tudo passe a ser compilado com a mesma versão dos programas da suíte do gcc. Para testar os comandos, basta abrir uma nova aba ou um novo terminal e digitar os comandos:


```
$ gcc -v
$ g++ -v
$ gfortran -v
```


Em todos os casos, as versões devem ser identificadas como "gcc version 4.4.7 (MacPorts gcc44 4.4.7_6)". É possível que algum número de versão se altere caso alguma atualização do port seja feita.

Com o gcc4.4 instalado e configurado, é possível começar a instalação dos programas zlib, hdf5, netcdf4 e openmpi. O programa zlib é um software de compressão, uma espécie de "zip", que pode ser utilizado por qualquer outro programa que trabalhe com algum formato padronizado que utilize compressão; o hdf e o netcdf são bibliotecas utilizadas para armazenamento de dados geofísicos. Eles serão instalados por uma necessidade específica, e este pode não ser o seu caso. O openmpi é uma implementação aberta do mpi ([Message Passing Interface](http://www.google.com.br/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CCAQFjAA&url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMessage_Passing_Interface&ei=kLFxUImjFqHu0gGvsID4DA&usg=AFQjCNFza1vKnEf_ha9dT1FVJWCmPqR6Yw)) e é utilizado para executar programas em paralelo. Entre estes quatro programas, o openmpi é o único que tem dependência apenas do compilador C, C++ e fortran instalados na máquina; os demais possuem uma ordem específica de compilação, a qual será abordada mais adiante. É importante ressaltar que todos estes programas estão disponíveis na árvore de programas do MacPorts. No entanto, eles serão compilados manualmente com o gcc4.4 para permitir, porteriormente, que sejam também compilados com outros compiladores (eg., pgi, intel), caso haja necessidade.

**Para a instalação do openmpi, é necessário obter o pacote da última versão do openmpi (atualmente na versão 1.6.2), descompactar e executar o comando:**


```
$ wget -c http://repository.timesys.com/buildsources/o/openmpi/openmpi-1.6.2/openmpi-1.6.2.tar.bz2
$ tar -xvf openmpi-1.6.2.tar.bz2
$ cd openmpi-1.6.2
$ ./configure CC=gcc CXX=g++ F77=gfortran FC=gfortran \ 
--prefix=/opt/openmpi-gcc_gfortran4.4
```


O último comando irá compilar o openmpi com as flags CC, CXX, F77 e FC que indicam, respectivamente, os compiladores que serão utilizados no processo (gcc, g++ e gfortran). Observe que não foi necessário especificar a versão do gcc, pois isso já foi feito anteriormente com um comando interno do MacPorts (port select). O argumento "--prefix" permite especificar o local em que serão instalados os executáveis e demais arquivos criados na compilação do openmpi. É importante escolher um nome que reflita a configuração escolhida para a compilação do pacote, por exemplo, "openmpi-gcc_gfortran4.4". Caso seja necessário instalar uma nova versão do gcc, uma nova compilação do openmpi será necessária para que se possa utilizar os comando mpif90, mpicc, mpicpp etc com a versão correta dos compiladores C, C++ e fortran. Isso é necessário porque nem sempre os módulos e bibliotecas são compatíveis entre as diferentes versões dos compiladores.

Depois de configurar o openmpi, basta executar os dois comandos abaixo para iniciar a compilação do pacote e finalizar a instalação, respectivamente:


```
$ make all
$ sudo make install
```


Com isso, o programa openmpi estará instalado. Os executáveis estarão em /opt/openmpi-gcc_gfortran4.4/bin. Para fazer com que esta versão seja a versão padrão disponível no seu Mac OS X, basta exportar as variáveis de ambiente necessárias, conforme este [post](../../../2011/04/25/variaveis-de-ambiente-para-programas-fonte-wp-1137.md). Caso você tenha outras versões do openmpi instalada, basta ajustar as variáveis de ambiente (PATH, MANPATH, C_INCLUDE_PATH e LIBRARY_PATH) para refletir os caminhos da instalação desejada.

Para a instalação do netcdf4, é necessário instalar o hdf5. Mas para instalar o hdf5, é necessário instalar primeiro a zlib.

**A instalação da zlib é bastante simples e rápida também. Para baixar, configurar e instalar, execute:**


```
$ wget -c http://zlib.net/zlib-1.2.7.tar.gz
$ tar -zxvf zlib-1.2.7.tar.gz
$ cd zlib-1.2.7
$ ./configure --prefix=/opt/zlib-gcc_gfortran-4.4 
$ sudo make check install
```


**Com a zlib instalada, o próximo passo é a compilação do hdf5. Para baixar, configurar e instalar, basta fazer:**


```
$ wget -c http://www.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8.9/src/hdf5-1.8.9.tar.gz
$ tar -zxvf hdf5-1.8.9.tar.gz
$ cd hdf5-1.8.9
$ ./configure --with-zlib=/opt/zlib-gcc_gfortran-4.4 \ 
--prefix=/opt/hdf5-1.8.9-gcc_gfortran-4.4
$ sudo make check install
```


**Com o hdf5 instalado, finalmente pode-se instalar o netcdf4. Para baixar, configurar e instalar, basta fazer:**


```
$ wget -c http://www.unidata.ucar.edu/downloads/netcdf/ftp/netcdf-4.0.1.tar.gz
$ tar -zxvf netcdf-4.0.1.tar.gz
$ cd netcdf-4.0.1
$ ./configure CPPFLAGS="-I/opt/zlib-gcc_gfortran-4.4/include \
-I/opt/hdf5-1.8.9-gcc_gfortran-4.4/include" \ 
LDFLAGS="-L/opt/zlib-gcc_gfortran-4.4/lib \ 
-L/opt/hdf5-1.8.9-gcc_gfortran-4.4/lib" \ 
--prefix=/opt/netcdf-4.0.1-gcc_gfortran-4.4
$ sudo make check install
```


Observe que na instalação do netcdf4, foram especificadas as flags CPPFLAGS e LDFLAGS que representam, respectivamente, as pastas include e lib das instalações da zlib e do hdf5.

Feito isto, seu sistema estará pronto para utilizar o netcdf4, hdf5, zlib e openmpi. Estas mesmas instruções podem ser aplicadas em um sistema Linux ou BSD.

**Referências**

- <https://sites.google.com/site/dwhipp/tutorials/installing-open-mpi-on-mac-os-x>
- <http://www.unidata.ucar.edu/software/netcdf/docs/netcdf-install/Quick-Instructions.html>
