---
title: VPN no Mac OS X Lion
date: '2012-05-03 22:48:56'
tags:
- Fink
- Internet
- Mac OS X Lion
- Mac OS X Snow Leopard
- OpenVPN
- Tudo
- TunnelBlick
- Tutoriais
- VPN
categories:
- Internet
- Tudo
- Tutoriais
wordpress_id: 1488
original_url: https://craftmind.wordpress.com/2012/05/03/vpn-no-mac-os-x-lion/
---

# VPN no Mac OS X Lion

Dica rápida:

Esses dias precisei usar uma VPN no Mac OS X Lion e o administrado de sistemas da minha rede recomendou instalar o software [TunnelBlick](http://code.google.com/p/tunnelblick/) para fazer a conexão. Quando instalei o TunnelBlick e fui testar a VPN com o script que ele me forneceu, apareceu o seguinte:
> openvpn not found

Então pensei... isso só pode ser alguma coisa do Lion. Bem, não sei se era ou não, mas pensei isso porque a maioria dos Mac OSs que usam essa VPN estão rodando o Snow Leopard, por isso minha suspeita.

Mas para resolver, instalei o [Fink](http://www.finkproject.org/) e através dele o OpenVPN com o comando


```
$ fink install openvpn
```


Esperei terminar a instalação e Voilá, fuincionou como esperado.

~~Não me pergunte se o TunnelBlick fornece o openvpn.~~
**ATUALIZAÇÃO:**

Depois de olhar com um pouco mais de calma, descobri que o executável openvpn estava junto com a pasta de instalação do TunelBlick. Acontece que quando você instala um programa no Mac OS arrastando o .app para a pasta Applications, nâo necessariamente serão criados os links simbólicos para a pasta /usr/local/bin ou mesmo é incrementada a variável PATH (como PATH="/algum/lugar/bin":$PATH). Então, depois de ter descoberto isso, adaptei o meu script da VPN e passei a usar o executável openvpn que vem junto com ele. Funcionou da mesma forma. Se você ainda quiser utilizar o openvpn instalado pelo fink - se isso atender às suas necessidades, está correto também :)

Té!
