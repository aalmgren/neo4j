# Best Practices - Mineral Resource Estimation

Visualização interativa de boas práticas para estimativa de recursos minerais.

## 📊 Visualização

Acesse a visualização interativa: [hybrid_workflow_knowledge.html](https://aalmgren.github.io/neo4j/hybrid_workflow_knowledge.html)

## 📁 Estrutura

- `hybrid_workflow_knowledge.html` - Visualização principal do grafo de conhecimento
- `best_practices_structured.json` - Dados estruturados das boas práticas
- `boas_praticas_estimativa_recursos.md` - Documento fonte em Markdown
- `parse_best_practices_to_json.py` - Script para converter MD para JSON

## 🔄 Atualização

Para atualizar os dados:

1. Edite `boas_praticas_estimativa_recursos.md`
2. Execute: `python parse_best_practices_to_json.py`
3. Faça commit e push das alterações

## 🚀 Como rodar localmente

```bash
python -m http.server 8000
```

Acesse: http://localhost:8000/hybrid_workflow_knowledge.html
