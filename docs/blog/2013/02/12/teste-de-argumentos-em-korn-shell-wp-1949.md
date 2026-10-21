---
title: Teste de argumentos em Korn Shell
date: '2013-02-12 19:16:59'
tags:
- Korn Shell
- Shell
- Tudo
- Tutoriais
- ksh
categories:
- Tudo
- Tutoriais
wordpress_id: 1949
original_url: https://craftmind.wordpress.com/2013/02/12/teste-de-argumentos-em-korn-shell/
---

# Teste de argumentos em Korn Shell

Quando se programa scripts no Shell, muitas vezes torna-se conveniente passar argumentos junto com o script para tornar sua execução mais dinâmica e genérica. Mas esta prática também pode trazer alguns problemas: o script pode ser executado mesmo com um argumento errado! Por isso, é importante testar os argumentos antes de se executar as funções ou comandos do script.

Neste artigo, criaremos um script Korn Shell (KSH) que contém algumas funções, que serão executadas dependendo do argumento passado pela linha de comando. As funções, por simplicidade, conterão apenas o comando "print" com uma mensagem indicando qual função foi chamada. Veja abaixo, as etapas e a lógica do teste de argumentos:

**Estrutura do Script**

O script que montaremos, terá a seguinte estrutura - que pode ser copiada para qualquer outro script que faça qualquer outra coisa e que receba argumentos de entrada:


```
#! /bin/ksh
# set -o xtrace
# Funcoes
funcao_01() {
  print "Voce escolheu a funcao_01"
}
funcao_02() {
  print "Voce escolheu a funcao_02"
}
funcao_03(){
  print "Voce escolheu a funcao_03"
}
ajuda(){
  print "Uso: ./teste.ksh <argumento>"
}
# Teste dos argumentos
if [[ $# = 0 ]]
then
  print "Erro: Nao foi passado nehum argumento!"
  ajuda
elif [[ #1 != 1 ]]
then
  print "Apenas um argumento e necessario!"
elif [[ ${1} = "funcao_01" ]]
then
  print "Executando funcao ${1}"
  funcao_02
elif [[ ${1} = "funcao_02" ]]
then
  print "Executando funcao ${1}"
  funcao_02
elif [[ ${1} = "funcao_03" ]]
then
  print "Executando funcao ${1}"
  funcao_03
else
  print "Comando desconhecido: ${1}"
  ajuda
  exit 1
fi
exit 0
```


O script acima pode ser dividido em duas partes: uma contendo as funções, e outra contendo o teste dos argumentos. Na primera parte há três funções definidas que são executadas apenas quando chamadas, ou melhor, quando invocadas pela linha de comando através do argumento passado. Um das funções, chama-se "ajuda" e pode ser utilizada quando nenhum argumento é passado junto com o script, quando um número errado de argumentos é passado junto com o script (por exemplo, quando é necessário apenas um argumento e dois ou mais argumentos são passados) ou quando um argumento inválido é passado junto com o script - neste caso não haveria uma função associada ao argumento passado. Na segunda parte, é feito o teste dos argumentos. Esta estrutura do script é vantajosa pois impede que comando perigosos (como um "rm -rf") sejam executados na ausência de argumentos ou ainda na presença de um argumento errado. Geralmente, estas situações ocorrem com usuários que não têm o hábito de ler o script antes de executar.

**Algorítimo dos testes**

O algorítimo para o teste de argumentos é o seguinte:

1. Teste se algum argumento é passado. Caso positivo, passa-se para o próximo teste; caso negativo, mostra-se a função "ajuda".
2. Teste se mais do que um argumento é passado. Caso negativo, passa-se para o próximo teste; caso positivo, mostra-se a função "ajuda".
3. Teste se o argumento passado está associado à função funcao_01. Caso positivo, executa-se a função funcao_01; caso negativo, passa-se para o próximo teste.
4. Teste se o argumento passado está associado à função funcao_02. Caso positivo, executa-se a função funcao_02; caso negativo, passa-se para o próximo teste.
5. Teste se o argumento passado está associado à função funcao_03. Caso positivo, executa-se a função funcao_03; caso negativo, encerra-se o script com status de erro (1).

Observe que os argumentos possíveis neste script têm o mesmo nome que as funções definidas: funcao_01, funcao_02 e funcao_03. Qualquer nome (ou argumento) passado junto com o script e que for diferentes destes nomes, fará com que nenhuma das funções definidas seja executada.

**Conclusão**

O teste de argumentos deve englobar todas as possibilidades. Neste simples caso, apenas um argumento é testado o que torna simples a estruturação dos testes. Aumentando-se o número de argumentos, a complexidade dos testes pode aumentar e é aí que o programador deve avaliar a necessidade de se utilizar muitos argumentos dentro de um script. A idéia principal é manter o script simples e enxuto.
