---
title: Obtendo informações de hardware com o comando dmidecode
date: '2011-03-25 17:22:52'
tags:
- Hardware
- Tudo
- Tutoriais
- dmidecode
categories:
- Tudo
- Tutoriais
wordpress_id: 1124
original_url: https://craftmind.wordpress.com/2011/03/25/obtendo-informacoes-de-hardware-com-o-comando-dmidecode/
---

# Obtendo informações de hardware com o comando dmidecode

O comando “dmidecode” é bastante útil quando se quer obter informações sobre o hardware do computador. Com ele é possível descobrir o nome do fabricante (especialmente nos casos dos barebones!), o número dos chassis, número de série da placa-mão etc. Para rodar, basta instalar (pelo seu gerenciador de pacotes do linux) e rodar no terminal como root:


```
[root@arch carlos]# dmidecode
 # dmidecode 2.11
 SMBIOS 2.6 present.
 37 structures occupying 1663 bytes.
 Table at 0x000E9620.
Handle 0x0000, DMI type 0, 24 bytes
 BIOS Information
 Vendor: Hewlett-Packard
 Version: F.17
 Release Date: 07/05/2010
 ROM Size: 1536 kB
 Characteristics:
 PCI is supported
 BIOS is upgradeable
 BIOS shadowing is allowed
 Boot from CD is supported
 Selectable boot is supported
 EDD is supported
 Japanese floppy for NEC 9800 1.2 MB is supported (int 13h)
 Japanese floppy for Toshiba 1.2 MB is supported (int 13h)
 5.25"/360 kB floppy services are supported (int 13h)
 5.25"/1.2 MB floppy services are supported (int 13h)
 3.5"/720 kB floppy services are supported (int 13h)
 ...
```


E por aí vai…
