---
title: Consumo excessivo de memória RAM no Linux
date: '2011-10-17 08:55:09'
tags:
- Linux
- RAM
- Tudo
- Tutoriais
- Ubuntu 11.04
- cache
- kernal 2.6.26
- sysctl
categories:
- Tudo
- Tutoriais
wordpress_id: 1261
original_url: https://craftmind.wordpress.com/2011/10/17/consumo-excessivo-de-memoria-ram-no-linux/
---

# Consumo excessivo de memória RAM no Linux

Minha máquina de trabalho possui 16GB de memória RAM. Tenho nela o Ubuntu 11.04, o qual consegue consumir - sem a menor cerimônia, 6GB de memória depois de alguns dias ligada. Isso ocorre porque qualquer sistema operacional (principalmente o Linux) faz o cache dos programas que você mais usa. Essa atividade do sistema operacional, permite que você possa acessar mais rápidos os seus programas.

A partir do kernel 2.6.16, foi adicionada uma função que permite limitar o consumo de memória para esse tipo de cache. Para limitar o consumo de memória para cache no sistema, basta usar o comando

# sysctl -w vm.drop_caches=3

Esse comando irá alterar o valor (conteúdo) do arquivo /proc/sys/vm/drop_caches de "0" para "3".

O comando acima limpa o arquivo de paginação (caso exista uma partição swap), arquivos, pastas e "ponteiros" armazenado naquele local.

Para limpar apenas o arquivo de paginação, execute o comando:

# sysctl -w vm.drop_caches=1

Para limpar apenas os arquivos, pastas e "ponteiros", execute o comando:

# sysctl -w vm.drop_caches=2

Veja o resultado, antes e depois, com o comando "free -m":

Antes:


```
carlos ~ $ free -m
             total       used       free     shared    buffers     cached
Mem:         16064      15840        223          0       1093       8369
-/+ buffers/cache:       6377       9687
Swap:            0          0          0
```


Depois:


```
root /home/carlos # free -m
             total       used       free     shared    buffers     cached
Mem:         16064       5843      10220          0         18        193
-/+ buffers/cache:       5632      10431
Swap:            0          0          0
```


Se você tem pouca memória RAM e quer destruir tudo o que está em cache (swap!), basta "desligar/ligar" sua aprtição swap:


```
$ swapoff -a
$ swapon -a
```


**Referências:**

- <http://blog.aeciopires.com/consumo-abusivo-de-memoria-pelo-ubuntu/>
- <http://linux-mm.org/Drop_Caches>
- <http://unix.stackexchange.com/questions/6267/how-to-unswap-my-desktop>
