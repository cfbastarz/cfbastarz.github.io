# Blog

O blog mantém os endereços `docs/blog/AAAA/MM/DD/arquivo.md`. A data vem
da pasta; datas inválidas interrompem a construção. O menu agrupa os posts
por ano, mês e dia, do mais recente ao mais antigo. Os grupos abrem por clique,
toque ou teclado e o caminho do post atual fica expandido.

Para publicar, crie um Markdown nessa estrutura, com título e tags opcionais:

```markdown
---
tags:
  - Python
  - Meteorologia
---

# Meu novo post

Conteúdo do post.
```

`hooks/blog.py` gera o arquivo cronológico em `/blog/`, a lista em `/blog/tags/`
e uma página para cada tag, sem dependência de um tema específico. Os links de
tags aparecem no final dos posts. Não crie páginas manualmente em
`docs/blog/index.md` ou `docs/blog/tags/`: esses caminhos são reservados.
As tags distinguem maiúsculas de minúsculas. As tags iniciais podem ser editadas
no cabeçalho de cada post.

Requer MkDocs >=1.6,<2. O workflow instala essa versão e não utiliza mais
`mkdocs-blog-plugin`. Execute `mkdocs build` antes de publicar.

## Indexação por buscadores

Todas as páginas em `blog/` (incluindo arquivo e tags gerados) recebem
`<meta name="robots" content="noindex, noimageindex">` no tema Cinder. Isso
solicita que os buscadores compatíveis não indexem as páginas e as imagens
nelas exibidas. As demais seções do site continuam com o comportamento anterior.

Não bloqueie `/blog/` no `robots.txt`: os buscadores precisam acessar o HTML
para ler o `noindex`. URLs já indexadas podem demorar a sair dos resultados.
A regra não se aplica ao WordPress antigo, ao repositório público nem impede
acesso direto, cópias, robôs que ignorem a instrução ou indexação de arquivos
por outros links. Conteúdo que precise ser privado exige controle de acesso.

## Compartilhar apresentações

O template `presentation.html` exibe slides locais, com setas, seletor de página,
tela cheia quando suportada pelo navegador, link para um slide específico e
abertura/download do PDF original. O conteúdo e o layout do PDF são preservados.
O texto extraído fica disponível em uma seção expansível para consulta.

1. Coloque o PDF na pasta do post.
2. Instale Pillow e Poppler (`pdfinfo`, `pdftoppm`, `pdftotext`) para preparar os
   slides localmente. Essas ferramentas não são necessárias no deploy, pois os
   arquivos gerados ficam no repositório.
3. Execute `python scripts/prepare_presentation.py docs/blog/AAAA/MM/DD/talk.pdf`.
4. Use os metadados abaixo no post e escreva sua introdução normalmente:

```yaml
---
template: presentation.html
presentation:
  event: Nome do evento · Cidade
  date: DD/MM/AAAA
  pdf: talk.pdf
  slides: talk-slides
  size: 1,3 MB
tags:
  - Apresentações
---
```

O preparo gera imagens WebP e `manifest.json`, com uma página do PDF por slide.
Publique também essa pasta. Se alterar o PDF, gere novamente os slides. Para
PDFs digitalizados, a extração de texto pode ficar vazia: revise o manifesto e
adicione uma transcrição manual quando necessário. O PDF original permanece
acessível mesmo sem JavaScript. Este visualizador usa as imagens preparadas,
portanto links e seleção de texto dentro dos slides estão disponíveis no PDF.

Use `last_slide` nos metadados para encerrar a navegação antes de páginas finais
vazias. No exemplo de 2009, o visualizador mostra os 26 slides numerados e omite
a última página preta do PDF; o download mantém o arquivo integral.

## Data de publicação

Todos os posts em `blog/AAAA/MM/DD/arquivo.md` exibem a data de publicação logo
abaixo do título, incluindo apresentações. A data vem da pasta, a mesma fonte
usada no arquivo cronológico e no menu. O hook gera um elemento HTML `time`
com data ISO e texto em português. Arquivos e páginas de tags não recebem data
de publicação. Novos posts recebem essa informação automaticamente.
