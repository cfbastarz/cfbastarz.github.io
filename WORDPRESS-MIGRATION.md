# Migração do Aleph Zero

Importação do WXR de 21/10/2026, com mídias do TAR fornecido pelo autor.

- 198 posts publicados de 2010 a 2018, em `docs/blog/AAAA/MM/DD/`.
- 42 rascunhos excluídos da publicação. Páginas, menus, comentários e dados de
  comentaristas não são importados.
- 215 arquivos de mídia referenciados pelos posts (aproximadamente 73 MiB).
  Arquivos sem referência nos posts publicados não foram copiados.
- Datas locais, títulos, categorias, tags e URL original preservados nos metadados.
  Categorias também entram nas tags para permitir navegação por assunto.
- Cada slug recebe `-wp-ID`, evitando colisões com os posts já existentes.
  O artigo em português sobre copiar o caminho no shell foi mantido junto à
  versão em inglês já existente no site.
- Links entre posts importados e links de mídias locais foram reescritos.
- Legendas e galeria convertidas para imagens e texto; blocos de código mantidos.
- Vídeos do YouTube e SoundCloud convertidos para links identificados.
- Áudios usam controles HTML e link de download. Os 12 MP3 do Dropbox não estão
  no TAR e continuam externos; a disponibilidade desses serviços não é garantida.
  Uma imagem de relatório anual do WordPress também continua externa.
- Fórmulas `$latex ...$` convertidas para Arithmatex, com MathJax 3.2.2 via CDN.

`wordpress-migration.json` lista os posts e mídias externas para auditoria. Os
arquivos originais da exportação não são publicados. A migração não configura
redirecionamentos no WordPress: isso depende de configuração no serviço antigo.

## Reproduzir

Com Python, instale `beautifulsoup4`, `markdownify` e `PyYAML` em um ambiente virtual.
Na raiz do repositório, execute:

```sh
python scripts/import_wordpress.py /caminho/export.xml /caminho/media.tar
mkdocs build
```

O importador recusa sobrescrever posts que tenham sido alterados. Os arquivos
são gerados deterministicamente, e os caminhos de mídia são validados antes da
cópia. O TAR não é extraído diretamente no repositório.

## Validação realizada

Build completo com os plugins do site, todos os 198 posts renderizados,
metadados e IDs conferidos, 216 referências a imagens e todos os links locais
dos posts verificados. Os 32 blocos `code/sourcecode` foram comparados com o XML.
Nenhuma mídia referenciada do próprio blog ficou ausente no TAR. Os únicos
avisos do build são as duas âncoras preexistentes na página de teste de Markdown.
