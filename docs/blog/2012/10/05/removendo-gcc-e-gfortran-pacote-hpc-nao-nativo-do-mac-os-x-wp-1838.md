---
title: Removendo GCC e GFORTRAN (pacote HPC, não nativo) do Mac OS X
date: '2012-10-05 20:20:03'
tags:
- Ciência
- GCC
- GFORTRAN
- HPC
- Mac OS X
- Tudo
- Tutoriais
categories:
- Ciência
- Tudo
- Tutoriais
wordpress_id: 1838
original_url: https://craftmind.wordpress.com/2012/10/05/removendo-gcc-e-gfortran-pacote-hpc-nao-nativo-do-mac-os-x/
---

# Removendo GCC e GFORTRAN (pacote HPC, não nativo) do Mac OS X

Se você instalou os pacotes do gcc e do gfortran no seu Mac OS X disponíveis no site <http://hpc.sourceforge.net> deve ter percebido que a instalação é bastante simples, mas a desinstalação é um pouco mais complicada. Como os pacotes estão no formato .tar.gz, então não é um desinstalador que remova todos os arquivos que foram instaladas. No site <http://web.mit.edu/mfloyd/www/computing/mac/gfortran/> é uma dica que é a seguinte:


```
$ sudo rm -f `tar tfz [tar-file]`
```


Este comando lista todo o conteúdo do arquivo [tar-file] (eg., gcc-mtlion.tar.gz) e executa o comando rm -rf com permissão de superusuário. Mas há uma falha: o comando não é bem executado porque a listagem dos arquivos que estão dentro do arquivo tar não inclui a barra "/" no início, fazendo com que o arquivo "usr/local/bin/gcc" seja apagado ao invés do arquivo "/usr/local/bin/gcc". Portanto, esse comando não funciona porque o arquivo "/usr/local/bin/gcc" não existe!

Para resolver isso, utilize o comando abaixo:


```
$ for i in `tar tfz [tar-file]`; do sudo rm -rf '/'$i; done
```


No comando acima, listamos o conteúdo do arquivo [tar-file] (eg., gcc-mtlion.tar.gz) e utilizamos o comando for para executar o comando "sudo rm -rf '/'$i" em todos os arquivos que forem listados, incluindo a barra "/" no início.

**Referências**

- <http://web.mit.edu/mfloyd/www/computing/mac/gfortran/>
- <http://hpc.sourceforge.net>
