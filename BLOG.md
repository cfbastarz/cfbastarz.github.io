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
