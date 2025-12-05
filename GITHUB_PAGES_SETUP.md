# Como publicar no GitHub Pages

## Passo a passo

### 1. Criar/Verificar repositório Git

Se ainda não tiver um repositório Git inicializado:

```bash
git init
git add .
git commit -m "Initial commit: Geological workflow visualizations"
```

### 2. Criar repositório no GitHub

1. Acesse https://github.com/new
2. Crie um novo repositório (ex: `geological-workflows`)
3. **NÃO** inicialize com README, .gitignore ou license (já temos)

### 3. Conectar repositório local ao GitHub

```bash
git remote add origin https://github.com/SEU-USUARIO/geological-workflows.git
git branch -M main
git push -u origin main
```

### 4. Ativar GitHub Pages

1. No GitHub, vá em **Settings** do repositório
2. Role até **Pages** (no menu lateral esquerdo)
3. Em **Source**, selecione:
   - Branch: `main`
   - Folder: `/ (root)`
4. Clique em **Save**

### 5. Acessar sua visualização

Após alguns minutos, sua visualização estará disponível em:

```
https://SEU-USUARIO.github.io/geological-workflows/
```

Ou diretamente:
- Main page: `https://SEU-USUARIO.github.io/geological-workflows/index.html`
- Heuristic Reasoning: `https://SEU-USUARIO.github.io/geological-workflows/simple_growth.html`
- Neo4j Graph Explorer: `https://SEU-USUARIO.github.io/geological-workflows/neo4j_graphs.html`

## Estrutura de arquivos

Certifique-se de que todos estes arquivos estão no repositório:

```
├── index.html                    # Página principal com tabs
├── simple_growth.html            # Visualização de raciocínio heurístico
├── neo4j_graphs.html             # Explorador de grafos Neo4j
├── simple_growth_graph.json      # Dados para simple_growth.html
├── estimation_workflow_structured.json  # Dados para neo4j_graphs.html
└── README.md                     # Documentação
```

## Atualizações futuras

Para atualizar o site:

```bash
git add .
git commit -m "Descrição das mudanças"
git push origin main
```

O GitHub Pages atualiza automaticamente em alguns minutos.

## Notas importantes

- GitHub Pages serve arquivos estáticos (HTML, CSS, JS, JSON)
- Não há necessidade de servidor backend
- Os arquivos JSON são carregados via `fetch()` e funcionam no GitHub Pages
- Certifique-se de que todos os caminhos de arquivos são relativos (não absolutos)

