# Estimation Workflow - Mineral Resource Estimation

Visualização interativa do workflow de estimativa de recursos minerais.

## 📊 Visualização

Acesse a visualização interativa: [neo4j_graphs.html](https://aalmgren.github.io/neo4j/neo4j_graphs.html)

## 📁 Estrutura

- `neo4j_graphs.html` - Visualização principal do grafo de conhecimento
- `estimation_workflow_structured.json` - Dados estruturados do workflow
- `estimation_workflow.md` - Documento fonte em Markdown
- `parse_to_json.py` - Script para converter MD para JSON

## 🔄 Atualização

Para atualizar os dados:

1. Edite `estimation_workflow.md`
2. Execute: `python parse_to_json.py`
3. Faça commit e push das alterações

## 🚀 Como rodar localmente

```bash
python -m http.server 8000
```

Acesse: http://localhost:8000/neo4j_graphs.html
