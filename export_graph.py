import sqlite3
import json

def export_workflow_graph():
    """Exporta dados do SQLite para formato D3.js"""
    conn = sqlite3.connect("workflow.db")
    
    # Buscar steps
    cursor = conn.cursor()
    cursor.execute("SELECT step_id, name, description, status FROM steps")
    steps = cursor.fetchall()
    
    # Buscar dependencies
    cursor.execute("SELECT step_id, predecessor_id FROM dependencies")
    dependencies = cursor.fetchall()
    
    conn.close()
    
    # Formato D3.js: nodes + links
    nodes = []
    for step_id, name, desc, status in steps:
        nodes.append({
            "id": step_id,
            "name": name,
            "description": desc or "",
            "status": status or "pending",
            "group": 1 if status == "completed" else 2
        })
    
    links = []
    for step_id, pred_id in dependencies:
        links.append({
            "source": pred_id,
            "target": step_id,
            "value": 1
        })
    
    graph_data = {
        "nodes": nodes,
        "links": links
    }
    
    # Salvar JSON
    with open("workflow_graph.json", "w", encoding="utf-8") as f:
        json.dump(graph_data, f, indent=2, ensure_ascii=False)
    
    print("✓ Dados exportados para workflow_graph.json")
    return graph_data

if __name__ == "__main__":
    export_workflow_graph()
