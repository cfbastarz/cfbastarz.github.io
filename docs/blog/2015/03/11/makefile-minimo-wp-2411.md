---
title: Makefile (mínimo!)
date: '2015-03-11 02:14:05'
tags:
- Makefile
- Shell
- Tudo
- Tutoriais
- fortran
categories:
- Tudo
- Tutoriais
wordpress_id: 2411
original_url: https://craftmind.wordpress.com/2015/03/11/makefile-minimo/
---

# Makefile (mínimo!)

Quem trabalha com programação sabe que é necessário manter tudo em ordem: não importa se o trabalho é solo ou em grupo. Além de se utilizar um software de gerenciamento de códigos (eg., [CVS](http://www.nongnu.org/cvs/), [Subversion](https://subversion.apache.org), [git](http://git-scm.com)), à medida em que o(s) código(s) cresce(m), torna-se necessário (e desejável também), a utilização de algum software para o gerenciamento do projeto (eg., [Redmine](http://www.redmine.org), [Trac](http://trac.edgewall.org)). Mas no meio disso tudo - na verdade, antes disso tudo, há um pequeno pedaço de software que é responsável pela organização hierárquica de todo o projeto. Estamos falando sobre o [Makefile](https://www.gnu.org/software/make/manual/html_node/Makefiles.html).



O Makefile é o arquivo lido pelo comando "make" (ou GNUmakefile, se estivermos utilizando o comando "gmake") e é ele quem vai dizer para o compilador por onde começar e como compilar o código. Obviamente, se temos apenas uma rotina (eg., exemplo.f90, ou exemplo.coloqueaquiasualinguagempreferida), não há necessidade de se construir um Makefile (a menos que você precise lincar contra várias bibliotecas - libraries, e incluir vários cabeçalhos - headers). Para o caso mais simples, fazemos a seguinte compilação (utilizando a linguagem fortran e a suíte GCC como exemplo):


```
$ gfortran exemplo.f90
```


Se o programa exemplo.f90 não contiver erros, como resultado obteremos um executável de nome "a.out". Para executá-lo, basta fazer:


```
$ ./a.out
```


Caso queiramos especificar um nome diferente para o executável, podemos fazê-lo com a opção "-o":


```
$ gfortran exemplo.f90 -o exemplo.x
```


Nesse caso, ao invés de obtermos um executável com o nome padrão "a.out", o compilador (no nosso caso, o gfortran) vai gerar um executável com o nome "exemplo.x". É possível especificar qualquer nome, desde que este não contenha espaços e/ou caracteres especiais.

Podemos considerar também a situação em que o programa exemplo.f90 faz referência a um módulo que está escrito dentro de uma outra rotina de nome "modulo.f90". Neste caso, para que possamos gerar um executável para o programa principal (exemplo.f90), podemos fazer da seguinte maneira:


```
$ gfortran -c modulo.f90 exemplo.f90
```




```
$ gfortran modulo.o exemplo.o -o exemplo.x
```


Observe que desta vez, utilizamos a opção "-c" do compilador ( assim como a opção "-o", essa opção deve funcionar para qualquer compilador). A opção "-c" faz com que o compilador, ao invés de gerar um executável, crie dois arquivos diferentes para cada arquivo fonte compilado: um com a extensão ".mod" e outro com a extensão ".o". O primeiro, é um arquivo binário que contém todas as instruções específicas daquele módulo. O segundo é um objeto que pode ser utilizado para compor uma biblioteca (geralmente com a extensão ".a"). Imagine que a rotina module.f90 contenha vários módulos. Quando você a compilar com a opção "-c", o compilador vai gerar um par de arquivos ".mod" e ".o" para cada um dos módulos contidos na rotina modulo.f90. Neste caso, a compilação seria feita da mesma forma acima, e é neste tipo de situação (também) que o Makefile cumpre o seu papel.

Então, um Makefile mínimo é aquele que vai resolver o seu problema sem exigir muitos conhecimentos sobre o assunto.

Mas antes, para tornar este exemplo um pouco mais palpável, vamos considerar o seguinte:

- exemplo.f90 - é o programa principal;
- modulo1.f90 - é o módulo 1, que pode conter vários módulos e funções embutidas;
- modulo2.f90 - é o módulo 2, que pode conter vários módulos e funções embutidas;
- modulo3.f90 - é o módulo 3, que pode conter vários módulos e funções embutidas;

Tudo o que você precisa saber para construir manualmente o seu Makefile é a seguinte sintaxe (e sim, há alguns programas que criam os Makefiles automaticamente, como por exemplo, o [fgen](http://hpux.connect.org.uk/hppd/hpux/Misc/fgen-0.3/)):

```bash
alvo: dependências
[TAB] comandos
```

Só isso. Observe bem que os parágrafos - ou melhor, a identação dentro do Makefile, é feita com a tecla TAB e nunca com espaços.

Então, para escrever o seu Makefile, abra o se editor de textos preferido e digite as seguintes instruções (na mesma ordem) abaixo:

```bash
OBJS = modulo1.o modulo2.o modulo3.o exemplo.o
FC = gfortran
RM = rm
main: $(OBJS)
        $(FC) -o exemplo.x $(OBJS)
%.o: %.f90
        $(FC) -c $&lt;
clean:
        $(RM) *.o *.mod exemplo.x
```

A primeira linha do Makefile com a variável "OBJS", faz referências a todos os objetos de todos os arquivos fontes (incluindo o programa principal) que serão criados. Na segunda linha, a variável "FC" refere-se ao compilador que será utilizado (que no nosso caso, é o gfortran). Na próxima linha, fazemos referência ao programa "rm", utilizando uma variável de nome "RM". Observe que, eventualmente, pode ser uma boa idéia especificar o caminho absoluto, ou seja, ao invés de indicar apenas "FC = gfortran" e "RM = rm", pode-se indicar "FC = /usr/bin/gfortran"  e "RM = /usr/bin/rm". Estes caminhos podem mudar de sistema para sistema. Para saber onde se encontram estes comandos no seu Shell, basta utilizar o comando "which" (por exemplo, "which gfortran" e "which rm"). Além disso, o Makefile acima contém duas funções: a primeira, é a função "main" que se encarrega de criar os objetos necessários para a compilação da rotina exemplo.f90; a segunda função "clean" é a responsável por apagar ou "limpar" a compilação. Observe que neste caso, a função "clean" vai apagar qualquer arquivo com extensão ".o", ".mod" e também o executável do programa principal "exemplo.x". Você pode querer utilizar esta função quando for necessário fornecer o seu código para alguém.

Observe também as seguintes instruções contidas nesse Makefile:

```bash
%.o: %.f90
        $(FC) -c $&lt;
```

É esta instrução que indica que os objetos devem ser gerados a partir de todos os arquivos com a extensão ".f90". Se o seu projeto possui arquivos com a extensão ".F90" (maiúsculo - neste caso, o seu programa pode conter instruções de pré-processamento, como instruções em [MPI](http://en.wikipedia.org/wiki/Message_Passing_Interface) etc), a partir dos quais você queira também criar os objetos, então basta acrescentar:

```bash
%.o: %.f90
        $(FC) -c $&lt;
%.o: %.F90
        $(FC) -c $&lt;
```

Para utilizar este Makefile, basta digitar "make" para então compilar o seu projeto ou "make clean" para apagar os arquivos ".mod" e ".o". Estes comando devem ser executados na mesma pasta em que o Makefile estiver:


```
$ make
```




```
$ make clean
```


Você pode ainda querer renomear o arquivo Makefile para um outro nome. Neste caso, basta utilizar o modificador "-f" do comando make e indicar o arquivo:


```
$ make -f MeuMakefile
```


Ok, mas afinal, qual é a vantagem de um Makefile? Se o seu projeto é muito complexo, contendo vários programas, módulos e etc, certamente a compilação também é complexa. Se você quiser fazer uma pequena alteração em um módulo qualquer, ou em um outro programa qualquer dentro do seu projeto, a menos que você esteja utilizando um Makefile, você vai ter que compilar todas as rotinas novamente, para criar todos os objetos novamente e possivelmente, todas as bibliotecas também. Então, como o Makefile sabe quais são as rotinas que precisam ser compiladas, quais os objetos que devem ser criados e quais são as instruções para a compilação, logo, quando você fizer uma alteração qualquer no seu projeto, ele vai compilar apenas aquelas rotinas que foram modificadas. Isso reduz muito o tempo de compilação e ajuda a evitar erros.

É isso!

**Referências:**

- <http://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html>
- <http://kiwi.atmos.colostate.edu/fortran/docs/fortran90-mar30.pdf>
- <https://www.gnu.org/software/make/manual/html_node/Makefiles.html>
- <http://www.veryarm.com/1226.html> (link para a imagem em destaque)
