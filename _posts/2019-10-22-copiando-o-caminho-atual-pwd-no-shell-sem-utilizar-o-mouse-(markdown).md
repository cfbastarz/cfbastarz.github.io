--- layout: post title: Copiando o caminho atual (pwd) no Shell sem utilizar o mouse date: 2018-10-16 10:40:59.000000000 -03:00 type: post parent\_id: '0' published: true password: '' status: publish categories: - Linux - Mac - Tudo tags: - ".bashrc" - ".bash\_aliases" meta: \_publicize\_job\_id: '23250302755' timeline\_notification: '1539693688' author: login: craftmind email: cfbastarz@gmail.com display\_name: cfbastarz first\_name: '' last\_name: '' permalink: "/2018/10/16/copiando-o-caminho-atual-pwd-no-shell-sem-utilizar-o-mouse/" ---

Quem trabalha muito na frente do terminal, acaba desenvolvendo a habilidade de não utilizar o mouse. Boa parte do meu tempo no trabalho, é em frente ao terminal (seja um terminal do Linux ou do OS X) e raramente utilizo o mouse para alguma coisa, a não ser para interagir com a interface gráfica (como arrastar janelas ou coisas do gênero). Mas uma situação que sempre me forçou a usar o mouse na frente do terminal, era simplesmente copiar o endereço do local onde estou e colar dentro do editor vi (ou vim) ou em outro local. Para isso, sempre utilizei o comando “pwd” e usava o mouse para copiar e colar. Percebendo que essa era praticamente a única ação que me fazia tirar as mãos do teclado enquanto trabalhava com o terminal, revolvi procurar uma solução. Eu a encontrei e é bastante simples. Há basicamente dois comandos que podem ser utilizados para esta função. Um deles é o “pbcopy” que pode ser utilizado no OS X e o outro, é o “xclip” que pode ser utilizado no Linux.

pbcopy no OS X
==============

No terminal do OS X, encontrei o comando “copypath”. Este comando é interno, ie., ele faz parte do conjunto de ferramentas do OS X e portanto, não é necessário instalar ele.

Uso
---

Um exemplo do seu uso é o seguinte:

\[code language="plain"\]$ pwd | pbcopy

\[/code\]

Utilizando o atalho do teclado “CMD+v”, posso colar no terminal (ou em qualquer outro local) o caminho indicado pelo comando “pwd”:

\[code language="plain"\]/Users/carlos

\[/code\]

Muito simples e funcional.

xclip no Linux
==============

Como eu não sabia que o “pbcopy” é um comando interno do OS X, fui tentar no terminal do Linux e não deu certo. Fui procurar e acabei encontrando o comando “xclip”, que tem a mesma função e funciona muito bem. Porém, na máquina em que eu estava trabalhando, este comando não estava instalado, mas nada me impediu de instalar ele localmente.

Instalação
----------

Para instalar o comando “xclip” em uma máquina a partir do código fonte do programa, basta seguir os passos abaixo:

\[code language="plain"\]$ wget -c https://github.com/astrand/xclip/archive/master.zip  
$ unzip master.zip  
$ cd master/  
$ ./bootstrap  
$ ./configure --prefix=${PWD}  
$ make  
$ make install  
\[/code\]

Com esses comandos, você irá instalar o “xclip” no mesmo diretório do código fonte do programa. Serão criados dois novos diretórios, “bin” e “share”. Dentro do primeiro, deverão estar presentes os executáveis do “xclip” e dentro do segundo, os manuais. Para adicionar os novos comandos e manuais ao PATH do Shell, basta configurar o seu arquivo ~/.bashrc (ou ~/.bash\_profile ou mesmo ~/.profile), adicionando as seguintes linhas ao final do arquivo:

\[code language="plain"\]export PATH=“/caminho/para/o/diretorio/bin/do/xclip”:${PATH}  
export MANPATH=“/caminho/para/o/diretorio/share/man/do/xclip”:${MANPATH}  
\[/code\]

Com isso, basta dar um source no arquivo alterado (eg., “source ~/.bashrc”) ou abrir um nova aba no terminal.

Uso
---

O uso do comando “xclip” no Shell do Linux é bastante simples. Por exemplo, copiando o caminho atual e redirecionando a saida para dentro de um arquivo texto (arq.txt):

\[code language="plain"\]$ pwd | xclip  
$ xclip -o &gt; arq.txt  
\[/code\]

Para colar o caminho copiado com o xclip dentro do editor vim, basta digitar “SHIFT+p”.

É isso!

**Referências:**

-   <https://www.cyberciti.biz/faq/xclip-linux-insert-files-command-output-intoclipboard/>
-   <https://langui.sh/2010/11/14/pbpaste-pbcopy-in-mac-os-x-or-terminal-clipboard-fun/>
