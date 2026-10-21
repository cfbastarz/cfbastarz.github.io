---
title: Dicas para quem está iniciando em "modelagem"
date: '2012-04-11 13:48:14'
tags:
- Ciência
- SVN
- Shell
- Tudo
- Tutoriais
- fortran
- modelagem
- programação
- repositório
- testes
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 1495
original_url: https://craftmind.wordpress.com/2012/04/11/dicas-para-quem-esta-iniciando-em-modelagem/
---

# Dicas para quem está iniciando em &quot;modelagem&quot;

A idéia deste post é mostrar algumas dicas para quem está iniciando a "rodar" modelos, seja realizando testes, seja realizando implementações. Com algum tempo trabalhando com modelagem (no meu caso em meteorologia), você acaba colecionando algumas dicas que podem ser preciosas em diversos aspectos da atividade prática da modelagem. Mas antes de mais nada, vou definir aqui que o termo "modelagem", se refere à atividade prática (à execução da modelagem) de preparar um determinado sistema ou modelo computacional e seu respectivo ambiante de compilação/submissão, e não necessariamente a modelagem em si - que por si só tem seus desafios. Estas mesmas idéias podem ser facilmente aplicadas a situações mais simples, como por exemplo, desenvolver um programa em linguagem C, fortran ou um script shell simples que automatize algumas tarefas. É preciso ter em mente apenas começar da forma correta, o não o isenta de cometer erros (inerentes ao seu trabalho) e aprender com eles.

Pois bem, quem está começando sempre tem um pouco de pressa, ou por não saber que o processo prático da modelagem é não linear, ou porque é muito apressado e sabe que não tem muito tempo para gerar e analisar os seus resultados. Nesse caso, há um caminho bastante longo e complicado entre "gerar" e "analisar" os resultados. Muitas vezes, gerar os resultados pode parecer um alívio, mas se eles não foram gerados da forma correta, podem lhe trazer muita dor de cabeça. Então, para começarmos, vamos colocar os tópicos desta discussão na seguinte ordem:

1. Cheguei agora, o que faço?
2. Certo, agora que já comecei, o que faço?
3. Deu pau, o que faço?
4. Deu pau de novo, o que posso fazer?
5. Acho que agora está dando certo..., o que faço?
6. Meu primeiro resultado! E agora, o que faço?
7. Meu tempo acabou, o que faço?
8. Outras dúvidas...

Certamente, poderiam haver outros "... e agora, o que faço?", mas com certeza estes sete tópicos são bastante representativos do processo prático da modelagem como um todo e certamente podem lhe ajudar. Portanto, entenda este texto como uma espécie de "auto-ajuda" da prática da modelagem (antes que você tenha que recorrer à alguma ajuda externa) ou um "caminho-zen" para as suas atividades em modelagem.

**1. Cheguei agora, o que faço?**

Com certeza, essa é a sua primeira dúvida quando não se tem experiência prévia na prática do seu trabalho de pesquisa. Geralmente, a iniciação científica nos serve como uma espécie de laboratório com experimentos controlados em que não se assume a responsabilidade por um determinado resultado, ou melhor, aprende-se - num espaço curto de tempo, a colocar a mão na massa. Mas nem sempre, quem faz iniciação científica, acaba trabalhando com os mesmo temas em pesquisas futuras. Nesse momento, as dúvidas e aflições de quem está começando são, frequentemente, as seguintes: "putz, vou ter que mexer no linux...", "putz, vou ter que mexer no terminal do linux...", "putz, vou ter que trabalhar com programação...", "putz, vou ter que trabalhar com o cluster...", "putz, vou ter que trabalhar com o supercomputador..." etc. Na verdade, a grande sacada nesse momento é não se aborrecer e nem se preocupar com o tal do linux e seu terminal, até porque - dependendo da área em que você trabalhe, vai acabar percebendo que ao invés dele ser um vilão, ele será a melhor ferramenta com que você vai trabalhar. Dito isto, comece a se preparar fazendo-se as seguintes perguntas:
> Se eu vou trabalhar com um modelo computacional ou um programa fortran, ou script do matlab etc, onde ele(s) está(ão)?

Essa é a primeira coisa que você tem que se perguntar. Se isso lhe parecer um pouco óbvio demais, saiba que se você não for cuidadoso(a) a partir daqui, os seus problemas podem começar logo de início. Se você for trabalhar no linux (sendo no seu computador/notebook, em um cluster ou em um supercomputador), com certeza terá que lidar com o terminal. Por isso, pesquise com os seus colegas de trabalho onde pode-se obter o modelo ou programa com que você vai trabalhar. Não se preocupe demais com o terminal e os seus comandos, com certeza você vai aprender praticando.
> Sempre, eu eu disse SEMPRE, a melhor situação é quando você pode trabalhar com repositórios (em cvs, svn, git, bazar etc).

Os repositórios são importantes porque permitem que você crie um histórico de alterações e de versões dos seus scripts e rotinas que for trabalhar/criar/modificar. Além disso, ele vai lhe ajudar naquele momento em que você estiver escrevendo um relatório ou em que precisar lembrar de uma determinada data em que modificações ou implementações foram realizadas. Portanto, nessa primeira situação, pergunte a seus chefes, colegas, orientadores se o código com o qual você for trabalhar está em um repositório e em que tipo de repositório. Pergunte também se você pode criar um ramo (repositório) próprio para realizar os seus desenvolvimentos. Com certeza, essa é a melhor maneira de se iniciar o trabalho com códigos computacionais em sistemas e modelos. Para exemplos de utilização do svn, por exemplo (eu aprendi a trabalhar com o svn), leia este post sobre a criação de um repositório svn em sua máquina local ([http://craftmind.wordpress.com/2011/04/25/criando-um-repositorio-svn-local/](../../../2011/04/25/criando-um-repositorio-svn-local-wp-1130.md)) e este sobre como utilizar o svn (<http://samuca.wordpress.com/2007/04/12/tutorial-subversion/>).

**2. Certo, agora que já comecei, o que faço?**

Se você já sabe onde está o código ou modelo com que vai trabalhar, agora é o momento de aprender a instalar/utilizar/testar o seu código. Todo código que tem um desenvolvimento ordenado e, por mais simples que seja, deve ter um README ou um LEIAME com a descrição do programa, notas de versão, bugs conhecidos e - principalmente, como instalar/utilizar/testar. Este trio (instalar/utilizar/testar) é essencial e deve ser seguido antes que qualquer outro tipo de teste seja feito com o código que você vai trabalhar. Procure saber se há uma conjunto de dados de teste (geralmente um conjunto pequeno de dados que permita testar todos os aspectos do programa).
> Leia o README, siga as instruções, tire suas dúvidas e quando se sentir confortável o suficiente para começar, inicie o trio instalar/utilizar/testar.

**3. Deu pau, o que faço?**
Tem certeza de que leu o README por completo? Tem certeza de que não surgiram dúvidas? Se alguém lhe deu uma explicação e você não entendeu muito bem, volte e pergunte novamente. Não se acanhe! Quanto menos dúvidas você tiver sobre o processo de instalar/utilizar/testar, melhor. Assim você poderá se preocupar menos com os aspectos práticos do sistema e mais com os aspectos teóricos da sua pesquisa. Caso todas as informações do README e as instruções que lhe foram fornecidas tenham sido completamente atendidas, então o problema pode ser outro. Será necessário ler todos os logs do sistema e procurar por erros desconhecidos ou que, por uma razão ou outra, ainda não foram relatados.
> Inclusive, esta pode ser uma oportunidade para que você colabore com os desenvolvedores do sistema que você está utilizando.

**4. Deu pau de novo, o que posso fazer?**

Se o problema persiste ou lhe parece ser algo sistemático (que está se repetindo sempre, da mesma forma), pode ser que o problema não seja com o seu sistema, mas sim com a máquina em que está sendo executado.
> Lembre-se que assim como o seu computador, qualquer sistema - por mais moderno e seguro que seja, ele é suscetivel a problemas de software e hardware diversos. Se você tiver certeza de que os problemas não fazem parte do seu sistema (dos modelos/rotinas/scripts), entre em contato com o administrador da máquina que você está utilizando.

Se você está utilizando apenas o seu computador, não perca tempo e peça ajuda a alguém mais experiente. Geralmente, problemas de compilação estão relacionados à variáveis de ambiente mal ajustadas e programas que não estão completamente instalados. Se você depende de algum tipo de biblioteca que não é fornecida com o seu sistema, leia este post para uma explanação geral sobre a instalação de programas a partir do código fonte no linux ([http://craftmind.wordpress.com/2011/04/25/variaveis-de-ambiente-para-programas-fonte/](../../../2011/04/25/variaveis-de-ambiente-para-programas-fonte-wp-1137.md)).

**5. Acho que agora está dando certo..., o que faço?**

Com muita sorte, as coisas dão certo logo de primeira ou pelo menos nas primeiras tentativas. Se não derem certo de primeira e você teve que queimar uma pouco da sua preciosa mufa para resolver, parabéns: com certeza você aprendeu mais coisas do que esperava. Uma vez que as coisas começam a fluir e a funcionar de forma como tem que ser (ou pelo menos da forma como se espera), fique atento com a performance do seu modelo/programa e veja se os resultados preliminares (on the flie) estão razoavelmente dentro do que se sabe/conhece. Geralmente os modelos computacionais geram saídas de log e erro a partir das quais pode-se acompanhar os valores calculados de uma determinada variável ou o tempo que está demorando para realizar algum cálculo. Observando estes aspectos, você poderá ser capaz de identificar problemas como: valores espúrios, situações fisicamente impossíveis, instabilidade numérica, problemas de paralelismo etc. Este tipo de diagnóstico pode lhe poupar horas, dias ou até semanas de trabalho! Imagine a situação em que um modelo numérico de previsão de tempo é empregrado para integrar uma condição inicial durante sete dias. Atualmente, dependendo de onde o modelo está sendo executado, este trabalho pode demorar de horas a dias e se você não se preocupar em olhar os valores que estão sendo escritos no log do sistema, só vai perceber que alguma coisa está errada no final.
> Portanto, fique atento aos logs e aprenda a interpretar os valores e resultados preliminares. Ah, não se engane com as médias!!

**6. Meu primeiro resultado! E agora, o que faço?**

Ótimo, se você conseguiu chegar até aqui, já deve ter alguma bagagem com coisas interessantes que aprendeu sobre o processo prático da modelagem. No caso dos resultados de modelo, certamente haverá um arquivo final com os valores/campos e, dependendo do sistema empregado, esse arquivo poderá ser convertido para um formato padrão (por exemplo, grib, netcdf, hdf etc) que, além de ocupar menos espaço, já disponibiliza o arquivo final para visualização em um software específico (por exemplo, o GrADS). Geralmente, o conjunto dessas rotinas de conversão é chamada de pós-processamento e geralmente, são feitas interpolações e outros procedimentos matemáticos que podem embutir pequenos erros oriundos de aproximações. Fique atento às fontes de erros nos seus resultados e saiba ponderá-las em sua avaliação. Procure também comparar os dados brutos (antes do pós-processamento) com os dados finais (pós-processados).
> Certamente, estas informações podem lhe assegurar um controle e visão melhores sobre os resultados que você obteve.

Ao sinal de qualquer dúvida sobre os resultados gerados, se você tiver tempo, refaça os experimentos e tire suas dúvidas. Além disso, a avaliação estatística e/ou interpretação física dos resultados deve ser feita de forma bastante consistente. Leve em consideração os tipos de avaliação que outros pesquisadores estão fazendo e tente comparar os seus resultados com os deles. Isso ajuda e muito na validação dos seus experimentos e também vai lhe assegurar que a sua metodologia não contém falhas.

**7. Meu tempo acabou, o que faço?**

Isso vai acontecer e, geralmente no mestrado - em que se tem pouco tempo para executar a parte prática, você pode se desesperar com a qualidade dos seus resultados.
> Se você tomar todos os cuidados e rever sempre os seus passos, dificilmente passará por algum problema por culpa sua.

Acredite, erros todos comentem e perder o tempo que se tem para uma determinada tarefa, é o pior deles. Então, tome os devidos cuidados e extraia o máximo que puder do aprendizado da prática de modelagem. Com certeza, numa outra oportunidade, você estará mais calejado e esperto para enfrentar novos desafios e saberá como começar...

 **Outras dúvidas...**

Na verdade, este tópico não é sobre dúvidas, mas sim recomendações. Sempre que você estiver desenvolvendo algo, seja minucioso, documente tudo o que você está fazendo. Se a sua memória é fraca, certamente você estará se livrando de um imprevisto ou de ter que bolar uma solução para um problema que você já resolveu. Para as rotinas e scripts que você escrever, utilize o [Doxygen](http://www.stack.nl/~dimitri/doxygen/) ou o [ProTeX](http://gmao.gsfc.nasa.gov/software/protex/) para gerar a documentação. É justo com você, porque agrega valor ao seu trabalho e justo com quem vai colaborar ou dar continuidade aos desenvolvimentos que você iniciou. Lembre-se que linguagem de máquina é para máquina, humanos lêem textos.
> Se ao escrever a documentação você ficar na dúvida se escreve em português ou em inglês, não exite: escreva em português.

Sempre tem alguém que diz "tem que escrever em inglês porque se houver alguma colaboração de fora, todos têm que entender". Isso está correto, desde que se saiba escrever corretamente em inglês... não adianta nada escrever em inglês se apenas os nativos procurarem a documentação para ler, e vai ser pior se estiver em inglês mal escrito. Portanto, a menos que alguém se disponha a revisar a documentação, escreva em bom português mesmo. Vale lembrar que a documentação, além de ajudar no entendimento dos seus programas, ajuda também a escrever o trabalho final ou relatório.

Ao escrevermos, sempre confrontamos e revisamos idéias anteriores e fixamos o que sabemos.

Boa sorte!

**PS.:** Este texto deverá ser melhorado ao longo do tempo.
