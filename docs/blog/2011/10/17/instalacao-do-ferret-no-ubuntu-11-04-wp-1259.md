---
title: Instalação do Ferret no Ubuntu 11.04
date: '2011-10-17 12:24:35'
tags:
- Ciência
- Ferret
- Tudo
- Tutoriais
- Ubuntu
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 1259
original_url: https://craftmind.wordpress.com/2011/10/17/instalacao-do-ferret-no-ubuntu-11-04/
---

# Instalação do Ferret no Ubuntu 11.04

O Ferret é um software de visualização de arquivos NetCDF largamente utilizado na área de Geociências. Para instalar no Ubuntu 11.04 (o mesmo procedimento poderá servir para outras distribuições), siga os passos:

Baixar os arquivos de instalação (3 pacotes):


```
$ cd ~/Downloads
$ wget -c ftp://ftp.pmel.noaa.gov/ferret/pub/linux_32_rhel6/fer_executables.tar.gz
$ wget -c ftp://ftp.pmel.noaa.gov/ferret/pub/linux_32_rhel6/fer_environment.tar.gz
$ wget -c ftp://ftp.pmel.noaa.gov/ferret/pub/data/fer_dsets.tar.gz
```


Antes de iniciar a instalação, instale o pacote "csh" (C-Shell) no seu linux. No Ubuntu, o comando é:


```
$ sudo apt-get install csh
```


Para a instalação, foi escolhido a pasta /opt. Em /opt, cria uma pasta para o Ferret:


```
$ cd /opt
$ mkdir ferret
```


Dentro da pasta ferret criada, crie também as pastas fer_dsets e fer_env:


```
$ cd ferret
$ mkdir fer_dsets e fer_env
```


Vá para a pasta onde os downloads foram efetuados e descompacte os arquivos nas pasta criadas anteriormente:


```
$ cd ~/Downloads
$ sudo tar -zxvf fer_environment.tar.gz -C /opt/ferret/fer_env
$ sudo tar -zxvf fer_dsets.tar.gz -C /opt/ferret/fer_dsets
```


Feito isto, entre na pasta /opt/ferret/fer_env/bin e execute o script de instalação Finstall (como super usuário):


```
$ cd /opt/ferret/fer_env/bin
$ sudo su
# ./Finstall
```


Siga as instruções do script, mas execute apenas a etapa 1. Depois de saia do script com a opção 3.

Feito isto, basta configurar o arquivo com as variáveis de ambiente do Ferret para ser iniciado no carregamento do Bash:


```
$ cd /opt/ferret/fer_env/bin
$ sudo cp -pvfr ferret_paths_template.sh /opt/ferret/ferret_paths
```


Abra o arquivo copiado ferret_paths e altere o valor da variável FER_DIR para "**/opt/ferret/fer_env**"

Com isto, basta incluir basta incluir o comando "**source /opt/ferret/ferret_paths**" no seu **/home/$USER/.bashrc** e reiniciar o shell (**source .bashrc**).
