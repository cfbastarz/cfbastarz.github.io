---
title: Rebloqueando o bootloader e restaurando a imagem de fábrica do Moto X (2013,
  primeira geração)
date: '2015-05-22 02:43:30'
tags:
- Android
- Bootloader
- DIY
- Developer Edition
- Moto X
- Motorola
- Tudo
- Tutoriais
- XT1053
categories:
- DIY
- Tudo
- Tutoriais
wordpress_id: 2505
original_url: https://craftmind.wordpress.com/2015/05/22/rebloqueando-o-bootloader-e-restaurando-a-imagem-de-fabrica-do-moto-x-2013-primeira-geracao/
---

# Rebloqueando o bootloader e restaurando a imagem de fábrica do Moto X (2013, primeira geração)

Pois bem jovem incauto gafanhoto: você desbloqueou o bootloader do seu Moto X 2013 de primeira geração, instalou uma custom recovery, instalou uma custom rom e se arrependeu. Ou apenas quer reverter as alterações. Sei bem como é isso.



Para rebloquear o bootloader e restaurar a imagem de fábrica do seu Moto X (2013), siga as instruções abaixo, mas preste atenção aos seguintes detalhes:

1. Este procedimento não é tão simples, se você não sabe o que está fazendo, pare por aqui, abra o Facebook e seja feliz. Ou seja sábio e vá ler um livro.
2. Se você é curioso o suficiente, continue e resolva o seu problema, mas leia com atenção o aviso mais abaixo!
3. Você vai utilizar o programa fastboot pela linha de comando;
4. Os links para os arquivos e programas, estão no próprio texto, portanto, leia com atenção!
5. Meu Moto X é a versão [Developer Edition (XT1053)](https://www.youtube.com/watch?v=xOCdM7O8aSI), americana e portanto a minha firmware pode não ser a mesma que a sua. Aliás, estou considerando que você já possui imagem (ou rom) do seu aparelho para o procedimento de restauração.

Apesar destes detalhes acredito que o procedimento seja o mesmo para rebloquear o bootloader e restaurar a [imagem de fábrica de qualquer versão do Moto X (2013, primeira geração)](https://motorola-global-portal.custhelp.com/app/standalone/bootloader/recovery-images). Mas por que você quer fazer isso? Porque sim, ou porque você precisa/quer vender ou seu telefone. Ou por questões de segurança.

**PARE: Se você não sabe o que é fastboot, bootloader, imagem de fábrica ou Android, pare por aqui. Não serei responsável por quaisquer danos causado a você ou ao seu aparelho ao seguir este tutorial.**

Depois deste simpático aviso, mais alguns detalhes a saber. A primeira coisa a saber, é que a motorola possui um fastboot específico (o [mfastboot](http://forum.xda-developers.com/moto-g-2014/development/unix-mfastboot-linux-mac-os-x-how-to-t2941888)), ou seja, se você utilizar o fastboot que vem no SDK da Google, é muito provável que não vá funcionar. Então é preciso utilizar uma versão do fastboot fornecida pela própria Motorola. Além disso, rebloquear o bootloader e restaurar a imagem de fábrica do seu Moto X (2013) não vai fazer com que a mensagem de bootloader desbloqueado desapareça! Mas por que? Porque a Motorola decidiu que se  você desbloqueou o seu aparelho uma vez, não faz sentido (para ela) que ele volte a ser desbloqueado. Mas essa é a minha visão, e como eu utilizo a Developer Edition, pode ser que a minha imagem do Android seja assim. Mas pode ser que não. Então quer dizer que mesmo rebloqueando o bootloader, meu aparelho vai continuar com a mensagem de bootloader bloqueado? Sim, mas você pode instalar a [imagem de boot original](http://forum.xda-developers.com/moto-x/general/4-4-3-remove-unlocked-bootloader-message-t2548566) ([ou alguma outra](http://forum.xda-developers.com/showpost.php?p=53098892&postcount=355)), assim fica tudo conforme: aparelho com bootloader bloqueado e imagem de boot original.

Antes de mais nada, considerando que você já tem o mfastboot instalado no seu Linux ou OS X (ou mesmo Windows), coloque o seu aparelho no modo fastboot (desligue o aparelho, e depois pressione o botão power e ao mesmo tempo segure o botão volume para baixo, segure ambos por alguns segundos e depois solte) e conecte o aparelho via USB ao computador. Verifique se [todos os drivers](https://motorola-global-portal.custhelp.com/app/answers/prod_detail/a_id/94931/p/30,6720,8696/reg/2298017) estão corretamente instalados no seu computador. Abra o terminal e digite o seguinte comando, para se certificar que ele foi reconhecido e está em pronto para receber os comandos e arquivos que serão enviados a ele:


```
$ mfastboot devices
```


O resultado desse comando deve ser algo como uma seqüência de números identificando o seu aparelho. Se você não receber um código, há algum problema e o seu aparelho não foi reconhecido. Verifique novamente se todos os drivers estão corretamente instalados no seu computador! Agora vamos ao passo-a-passo.

Digite os seguintes comandos no terminal, em ordem:


```
$ mfastboot oem lock begin 
$ mfastboot flash partition gpt.bin
$ mfastboot flash motoboot motoboot.img
$ mfastboot flash logo logo.bin
$ mfastboot flash boot boot.img
$ mfastboot flash recovery recovery.img
$ mfastboot flash system system.img
$ mfastboot flash modem NON-HLOS.bin
$ mfastboot erase modemst1
$ mfastboot erase modemst2
$ mfastboot flash fsg fsg.mbn
$ mfastboot erase userdata
$ mfastboot erase cache
$ mfastboot oem lock
```


Observe que o primeiro comando "mfastboot oem lock begin" é mandatário; se você se esquecer dele, o último comando "mfastboot oem lock" vai falhar! Além disso, observe que os arquivos "gpt.bin", motoboot.img", "logo.bin" etc, são os arquivos que vem no seu pacote de imagem de restauração do seu telefone. Você deve apontar o caminho para eles, de forma que o comando mfastboot possa encontrá-los. O arquivo "logo.bin" pode ser substituído por outro do mesmo formato, mas com a imagem que você quer. A original que vem no pacote de restauração, é [aquela com a mensagem de bootloader desbloqueado](https://motorola-global-portal.custhelp.com/euf/assets/images/bootloader/WARNING_WITH_EXCEPTION.png). É neste momento que você escolhe uma imagem alternativa. Depois de todos os estes comandos, basta executar o próximo comando para reiniciar seu aparelho:


```
$ mfastboot reboot
```


É isso, depois é só reconfigurar novamente o seu Android.

**Referências:**

- <http://forum.xda-developers.com/moto-x/general/4-4-3-remove-unlocked-bootloader-message-t2548566>
- <http://forum.xda-developers.com/moto-x/general/noob-guide-unroot-relock-bootloader-vzw-t2571786>
